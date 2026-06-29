# thanks to alessio Tonioni for this script
# https://github.com/AlessioTonioni/AlessioTonioni.github.io/blob/master/scripts/update_publications.py

import os
import datetime
from scholarly import scholarly
import yaml
import re

# Configuration
SCHOLAR_ID = "Ao6WHDgAAAAJ"  # Lorenzo Lamberti
OUTPUT_DIR = "_publications"
IMAGE_DIR = "assets/images/papers"

def normalize_text(text):
    """Normalize text for comparison: lowercase, alphanumeric only."""
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def clean_filename(title):
    """Creates a clean filename from the paper title."""
    clean = re.sub(r'[^\w\s-]', '', title).strip().lower()
    clean = re.sub(r'[-\s]+', '-', clean)
    return clean

def format_authors(author_str):
    """Formats author string from Scholar format ('Author A and Author B')."""
    if not author_str:
        return "Unknown Authors"

    author_list = author_str.split(' and ')
    formatted = []
    for author in author_list:
        # Simple bolding of target author
        if "Tonioni" in author or "tonioni" in author.lower():
            formatted.append(f"**{author}**")
        else:
            formatted.append(author)

    if len(formatted) > 5:
        # If too many authors, use et al style for citation but maybe full for 'authors' field
        return ", ".join(formatted)
    return ", ".join(formatted)

def is_noise(title, venue):
    """Checks if the entry is research noise (supplements, reviews, patents)."""
    t = title.lower()
    v = venue.lower() if venue else ""

    noise_keywords = [
        'supplementary', 'material', 'reviewer', 'erratum',
        'patent', 'metodo per', 'procedimento', 'emergency'
    ]

    for kw in noise_keywords:
        if kw in t or kw in v:
            return True
    return False

def get_existing_titles():
    """Reads all existing publication files and returns normalized titles."""
    existing = {}
    if not os.path.exists(OUTPUT_DIR):
        return existing

    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(OUTPUT_DIR, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Extract front matter between ---
                    parts = content.split('---')
                    if len(parts) >= 3:
                        try:
                            fm = yaml.safe_load(parts[1])
                            if fm and 'title' in fm:
                                norm_title = normalize_text(fm['title'])
                                existing[norm_title] = filename
                        except:
                            continue
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return existing

def create_markdown(pub, existing_titles):
    """Creates a markdown file for a publication."""
    bib = pub['bib']
    title = bib.get('title', 'Untitled')
    year = bib.get('pub_year')
    venue = bib.get('venue') or bib.get('journal') or bib.get('publisher') or 'Preprint'

    # Check for Noise
    if is_noise(title, venue):
        return None

    # Check for Year
    if not year or int(year) < 2026:
        return None

    # Check for Duplicates
    norm_title = normalize_text(title)
    if norm_title in existing_titles:
        return None

    # Fetch details
    try:
        scholarly.fill(pub)
    except:
        pass

    # Re-extract with filled data
    bib = pub['bib']
    abstract = bib.get('abstract', 'Abstract not available.')
    formatted_authors = format_authors(bib.get('author', ''))

    # Project specific front matter
    clean_title = clean_filename(title)
    filename = f"{year}-{clean_title}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Convert ArXiv abs to pdf
    paper_url = pub.get('pub_url', '')
    if 'arxiv.org/abs/' in paper_url:
        paper_url = paper_url.replace('arxiv.org/abs/', 'arxiv.org/pdf/') + '.pdf'

    # Preprint handling
    pub_type = 'conference'
    if 'preprint' in venue.lower():
        venue = 'ArXiv'
        pub_type = 'review'

    front_matter = {
        'title': title,
        'authors': bib.get('author', '').replace(' and ', ', '),
        'collection': 'publications',
        'permalink': f"/publication/{clean_title}",
        'excerpt': abstract[:150].replace('\n', ' ') + '...' if abstract else '',
        'date': datetime.date.today(), # Using today's date as 'last modified' proxy
        'venue': venue,
        'paperurl': paper_url,
        'citation': f"{formatted_authors}. \"{title}.\" {venue}, {year}.",
        'pubtype': pub_type
    }

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("---\n")
        yaml.dump(front_matter, f, sort_keys=False, width=float('inf'))
        f.write("---\n\n")
        f.write(f"## Abstract\n\n{abstract}\n\n")
        if paper_url:
            f.write(f"| [Paper]({paper_url}) |\n")

    # Add News Entry
    news_content = create_news(title, clean_title, bib.get('author', ''), abstract)

    return {"title": title, "news": news_content}

def generate_with_gemini(title, abstract, first_author, clean_title):
    """Uses Gemini to generate a catchy short title and news snippet."""
    from google import genai
    import time
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None, None

    print(f"Generating news for: {title[:50]}...")
    for attempt in range(3):
        try:
            client = genai.Client(api_key=api_key)
            prompt = f"""
            Paper Title: {title}
            Abstract: {abstract}
            First Author (first name only): {first_author}

            Task:
            1. Extract the project acronym or a very short catchy title (max 3 words).
            2. Write a single-sentence news announcement (max 280 chars).
            3. Tone: "funny but not overly enthusiastic", human-like, slightly self-deprecating but proud.
            4. Requirements:
               - Start with a tiny, catchy "hook" or teaser about what the paper actually does.
               - Reference the paper link as: [SHORT_TITLE](/publication/{clean_title})
               - Credit the first author {first_author} using ONLY their first name.

            Return ONLY a raw JSON object:
            {{
                "short_title": "...",
                "snippet": "..."
            }}
            """
            # Add a safety timeout via context if possible, or just rely on the bounded loop
            response = client.models.generate_content(
                model='gemini-3-flash-preview',
                contents=prompt,
            )

            import json
            text = response.text.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[1].split("```")[0].strip()

            data = json.loads(text)
            return data.get("short_title"), data.get("snippet")
        except Exception as e:
            print(f"Gemini attempt {attempt+1} failed: {e}")
            if "429" in str(e) or "500" in str(e):
                time.sleep(10)
                continue
            break
    print("Gemini failed after retries, using fallback.")
    return None, None

def extract_short_title(title):
    """Fallback: Extracts a catchy acronym or short version of the title."""
    # If there is a colon, take the part before it (usually the acronym)
    if ':' in title:
        short = title.split(':')[0].strip()
        if len(short) > 2:
            return short

    # Fallback: first 4-5 words
    words = title.split()
    if len(words) > 5:
        return " ".join(words[:4]) + "..."
    return title

def create_news(title, clean_title, author_str, abstract=""):
    """Appends a catchy news entry to _data/news.yml."""
    news_file = "_data/news.yml"
    import random

    authors = author_str.split(' and ')
    if authors:
        # Extract first name only
        a = authors[0].split(',')
        full_name = a[1].strip() if len(a) > 1 else a[0].strip()
        first_name = full_name.split()[0]
    else:
        first_name = "the team"

    # Try Gemini first
    short_title, content = generate_with_gemini(title, abstract, first_name, clean_title)
    is_ai = True if content else False

    # Fallback if Gemini fails or no API key
    if not content:
        short_title = extract_short_title(title)
        templates = [
            f"A bit late to the party, but [{short_title}](publication/{clean_title}) is finally online. Big thanks to **{first_name}** for taking the lead on this one!",
            f"New paper alert! [{short_title}](publication/{clean_title}) just hit Arxiv. Check it out to see what **{first_name}** and the team have been brewing recently.",
            f"Just uploaded [{short_title}](publication/{clean_title}) to Arxiv. Pleasure working with **{first_name}** on this—I did some stuff too, but they did the heavy lifting.",
            f"Happy to share our latest work on [{short_title}](publication/{clean_title}). A huge shoutout to **{first_name}** for pushing this across the finish line!",
            f"If you are into this kind of thing, our new work [{short_title}](publication/{clean_title}) is now online. Congrats to **{first_name}** and everyone involved!"
        ]
        content = random.choice(templates)

    new_entry = {
        'date': datetime.date.today(),
        'content': content,
        'highlight': False,
        'ai_generated': is_ai
    }

    try:
        existing_news = []
        if os.path.exists(news_file):
            with open(news_file, 'r', encoding='utf-8') as f:
                existing_news = yaml.safe_load(f) or []

        # Avoid duplicate news for the same title if run multiple times
        if any(clean_title in str(item.get('content', '')) for item in existing_news):
            return content

        # Prepend to keep latest at top
        updated_news = [new_entry] + existing_news

        with open(news_file, 'w', encoding='utf-8') as f:
            yaml.dump(updated_news, f, sort_keys=False, default_flow_style=False)
        print(f"Added news for {short_title} (by {first_name})")
        return content
    except Exception:
        return content

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    existing_titles = get_existing_titles()
    updates = []

    try:
        print(f"Searching for author ID: {SCHOLAR_ID}...")
        author = scholarly.search_author_id(SCHOLAR_ID)
        print("Filling author data (this may take a minute)...")
        author_data = scholarly.fill(author, sections=['publications'])
        publications = author_data['publications']
        print(f"Found {len(publications)} total publications. Checking for new ones...")

        for i, pub in enumerate(publications):
            title = pub.get('bib', {}).get('title', 'Unknown Title')
            # Only log progress to keep terminal informative
            if i % 5 == 0:
                print(f"Processing publication {i+1}/{len(publications)}: {title[:50]}...")

            res = create_markdown(pub, existing_titles)
            if res:
                updates.append(res)

        if updates:
            print(f"Update finished. Processed {len(updates)} new entries.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()