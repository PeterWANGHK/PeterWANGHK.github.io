---
layout: about
title: about
permalink: /
subtitle: MPhil student · Data and Systems Engineering · The University of Hong Kong
profile:
  align: right
  image: profile.jpeg
  image_circular: false
  more_info: >
    <p>103M, Haking Wong Building</p>
    <p>The University of Hong Kong</p>
    <p>Hong Kong</p>
selected_papers: false
social: true
announcements:
  enabled: false
  scrollable: true
  limit: 5
latest_posts:
  enabled: false
---

<nav class="site-quick-links" aria-label="Explore my work">
  <a href="{{ '/publications/' | relative_url }}">Publications</a>
  <a href="{{ '/projects/' | relative_url }}">Research projects</a>
  <a href="{{ '/cv/' | relative_url }}">CV & experience</a>
  <a href="mailto:peterwang.dase@connect.hku.hk">Get in touch</a>
</nav>

I am **Zian Wang (Peter)** (<span lang="zh-Hant">王梓安</span>; Cantonese: **Wong Tsz On**). I am currently pursuing an M.Phil. degree with [Department of Data and Systems Engineering](https://www.dase.hku.hk/) at the University of Hong Kong, supervised by [Prof. Chen Sun](https://scholar.google.com/citations?user=LdBn-p4AAAAJ&hl=zh-CN). Our research group directed by Prof. Sun is called [HKU-SAIL Lab](https://github.com/SAS-HKU). It is a multidisciplinary research team that combines expertise in artificial intelligence, robotics, computer vision, and human-machine interaction to create breakthrough technologies that advance the field of autonomous systems. My research now focuses on integration of data-driven methods with risk-aware frameworks for improved prediction and safe planning in autonomous driving, and interdisciplinary topics within intelligent transportation systems.

Prior to joining HKU, I received the B.Eng. degree (with Honors) in Electronic and Information Engineering from [Department of Electrical and Electronic Engineering](https://www.polyu.edu.hk/eee/?sc_lang=en), The Hong Kong Polytechnic University in 2025, with thesis titled ["Advancing Cooperative Autonomous Navigation in Dynamic Environments with DRL-Optimized SLAM Hyperparameters for Enhanced Map Merging"](https://youtu.be/Ie8hh0jGMl4?si=hccqarMKl35nDsyU), supervised by [Prof. Ivan Ho Wang-Hei](https://www.polyu.edu.hk/eee/people/academic-staff-and-teaching-staff/prof-ho-ivan/).

💬 My research philosophy is: pursuing 100% open-source research outputs with reproducibility, credibility, and transparency; looking for real world deployment with sim-to-real.

💻 My senior colleagues who work closely with me: [Dr. Zejian Deng](https://scholar.google.com/citations?user=zA_fv-QAAAAJ&hl=zh-CN); [Ms. Yiming Shu](https://github.com/YimingShu-teay); [Ms. Jiahui Xu](https://scholar.google.com/citations?user=MHa9ts4AAAAJ&hl=zh-CN).

## [News]({{ '/news/' | relative_url }})

<div class="news table-responsive">
  <table class="table table-sm table-borderless">
    {% assign updates = site.news | reverse %}
    {% for update in updates limit:5 %}
    <tr>
      <th scope="row" style="width: 20%">{{ update.date | date: '%b %Y' }}</th>
      <td>{{ update.content | remove: '<p>' | remove: '</p>' | emojify }}</td>
    </tr>
    {% endfor %}
  </table>
</div>

## [Selected publications]({{ '/publications/' | relative_url }})

{% include selected_papers.liquid %}

### Research hierarchy · 2026

An overview of my research hierarchy for the recent year.

{% include figure.liquid path="assets/img/research_timeline.jpg" class="img-fluid rounded" alt="Research hierarchy for 2026" zoomable=true %}

### HKU-SAIL Lab research demo · 2025–2026

<figure>
  <a class="d-block position-relative" href="https://youtu.be/dx-rVhpalp4" target="_blank" rel="noopener noreferrer" aria-label="Watch the HKU-SAIL Lab Research Demo 2025–2026 on YouTube">
    <img class="img-fluid rounded w-100" src="https://i.ytimg.com/vi/dx-rVhpalp4/maxresdefault.jpg" alt="HKU-SAIL Lab Research Demo 2025–2026 video preview" width="1280" height="720" loading="lazy">
    <span class="position-absolute" aria-hidden="true" style="top: 50%; left: 50%; transform: translate(-50%, -50%); background: #c00; color: white; border-radius: 0.75rem; padding: 0.6rem 1.5rem; font-size: 2rem; line-height: 1;">▶</span>
  </a>
  <figcaption class="caption">Watch the research demo on YouTube.</figcaption>
</figure>

## [Honors and awards]({{ '/awards/' | relative_url }})

{% assign awards_page = site.pages | where: 'permalink', '/awards/' | first %}
{{ awards_page.content | markdownify }}
