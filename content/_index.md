---
title: ""
summary: ""
date: "2022-10-24"
type: "landing"
sections:
  - block: "resume-biography-3"
    content:
      username: "lorenzo-lamberti"
      text: ""
      button:
        text: "Download CV"
        url: "uploads/resume.pdf"
      headings:
        about: ""
        education: ""
        interests: ""
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: "md"
      avatar:
        size: "medium"
        shape: "circle"
      banner: {}
    ce: "section-a6ecdd43"
    As: "section-35cb60fb"
  - block: "markdown"
    content:
      title: "📚 My Research"
      subtitle: ""
      text: |
        I'm a researcher at ETH Zurich and IDSIA. Currently I am interested in visual odometry, SLAM, event-based cameras, VLM/VLA, TinyML, and more. Reach out to collaborate :)
    design:
      columns: "1"
    ce: "section-4854bbfc"
    As: "section-c61e1c0d"
  - block: "collection"
    content:
      title: "Recent Publications"
      text: ""
      filters:
        folders:
          - "publications"
        exclude_featured: false
    design:
      view: "compact"
    ce: "section-4c38bafb"
    As: "section-e18030e4"
  - block: "collection"
    content:
      title: "Recent & Upcoming Talks"
      filters:
        folders:
          - "events"
    design:
      view: "card"
    ce: "section-talks"
    id: "talks"
    As: "section-ca435d9a"
  - block: "collection"
    content:
      title: "Recent News"
      subtitle: ""
      text: ""
      page_type: "blog"
      count: 10
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      offset: 0
      order: "desc"
    design:
      view: "card"
      spacing:
        padding:
          - 0
          - 0
          - 0
          - 0
    ce: "section-news"
    id: "news"
    As: "section-351839d2"
---
