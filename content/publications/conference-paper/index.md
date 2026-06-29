---
title: 'TinyDEVO: Deep Event-based Visual Odometry on Ultra-low-power Multi-core Microcontrollers'

# Authors
# If you created a profile for a user (e.g. the default `me` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Alessandro Marchei
  - lorenzo-lamberti
  - Daniele Palossi
  - Luca Benini

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

date: '2016-06-01T00:00:00Z'

# Schedule page publish date (NOT publication's date).
# publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication metadata — structured fields used by citation styles and BibTeX export.
publication:
  name: "Embedded Vision Workshop 2026 In Conjunction With CVPR/ICCV"
  short_name: "EVW CVPR2026"

peer_reviewed: true
open_access: true
# license: CC-BY-4.0

# Awards, honors, and recognitions. Surfaced as badges on the page and in listings.
awards:
  - name: "Best Paper Award"
    level: winner
    note: "Top 5 of 8000 submissions"
  - name: "Oral Presentation"
    level: selected

# Funders and grants. Required by many funders for compliance reporting.
funding:
  - funder: "SNSF Robomix2 project"
    grant: "10004854"

abstract: A key task in embedded vision is visual odometry (VO), which estimates camera motion from visual sensors, and it is a core component in many embedded power-constrained systems, from autonomous robots to augmented and virtual reality wearable devices. The newest class of VO systems combines deep learning models with bio-inspired event-based cameras, which are robust to motion blur and lighting conditions. However, state-of-the-art (SoA) event-based VO algorithms require significant memory and computation. For example, the leading approach DEVO requires 733 MB of memory and 155 billion multiply-accumulate (MAC) operations per frame. We present TinyDEVO, an event-based VO deep learning model designed for resource-constrained microcontroller units (MCUs). We deploy TinyDEVO on an ultra-low-power (ULP) 9-core RISC-V-based MCU, achieving a throughput of approximately 1.2 frames per second with an average power consumption of only 86 mW. Thanks to our neural network architectural optimizations and hyperparameter tuning, TinyDEVO reduces the memory footprint by 11.5x (to 63.8 MB) and the number of operations per frame by 29.7x (to 5.2 billion MACs per frame) compared to DEVO, while maintaining an average trajectory error of 27 cm, i.e., only 19 cm higher than DEVO, on three state-of-the-art datasets. Our work demonstrates, for the first time, the feasibility of an event-based VO pipeline on ultra-low-power devices.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# tags:
#   - Large Language Models

# Display this page in the Featured widget?
featured: true

# Standard identifiers for auto-linking
# hugoblox:
#   ids:
#     doi: 10.5555/123456

# Custom links
links:
  - type: pdf
    url: ""
  - type: code
    url: https://github.com/HugoBlox/kit
  - type: dataset
    url: https://github.com/HugoBlox/kit
  - type: slides
    url: https://www.slideshare.net/
  - type: source
    url: https://github.com/HugoBlox/kit
  - type: video
    url: https://youtube.com

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
#   focal_point: ''
#   preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/projects/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
#   - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

<!-- > [!NOTE]
> Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.

> [!NOTE]
> Create your slides in Markdown - click the _Slides_ button to check out the example. -->

<!-- Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/). -->
