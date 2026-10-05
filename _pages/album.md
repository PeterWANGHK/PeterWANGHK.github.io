---
layout: page
title: album
permalink: /album/
description: Moments from different years, on campus and beyond.
nav: true
nav_order: 4
periods: ["2026", "2025", "2024", "2023", "2022"]
---

{% assign album_files = site.static_files | where_exp: "file", "file.path contains '/assets/album/'" | sort: "path" %}
{% assign album_images = "" | split: "," %}
{% assign discovered_periods = "" | split: "," %}
{% assign image_extensions = ".jpg,.jpeg,.png,.webp,.gif" | split: "," %}
{% for file in album_files %}
{% assign extension = file.extname | downcase %}
{% if image_extensions contains extension %}
{% assign album_images = album_images | push: file %}
{% assign path_parts = file.path | split: "/" %}
{% assign discovered_periods = discovered_periods | push: path_parts[3] %}
{% endif %}
{% endfor %}
{% assign periods = page.periods | concat: discovered_periods | uniq | sort | reverse | where_exp: "period", "period != 'undated'" %}
{% assign periods = periods | push: "undated" %}

<nav aria-label="Album periods" style="display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 2rem;">
  {% for period in periods %}
    {% assign label = period | replace: "-", " " | replace: "_", " " | capitalize %}
    {% if period == "undated" %}{% assign label = "Undated" %}{% endif %}
    <a href="#album-{{ period | slugify }}" style="border: 1px solid var(--global-divider-color); border-radius: 2rem; padding: 0.4rem 1rem;">{{ label | escape }}</a>
  {% endfor %}
</nav>

{% for period in periods %}
{% assign period_path = "/assets/album/" | append: period | append: "/" %}
{% assign photos = album_images | where_exp: "photo", "photo.path contains period_path" %}
{% assign label = period | replace: "-", " " | replace: "_", " " | capitalize %}
{% if period == "undated" %}{% assign label = "Undated" %}{% endif %}

  <section id="album-{{ period | slugify }}" aria-label="{{ label | escape }} photos" style="scroll-margin-top: 6rem; margin-bottom: 2rem;">
    <h2>{{ label | escape }} <small style="font-size: 0.55em; color: var(--global-text-color-light);">{{ photos.size }} {% if photos.size == 1 %}photo{% else %}photos{% endif %}</small></h2>
    {% if photos.size > 0 %}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 1.25rem;">
        {% for photo in photos %}
          {% assign caption = photo.name | remove: photo.extname | replace: "-", " " | replace: "_", " " | capitalize %}
          <figure style="margin: 0; padding: 0.75rem; border: 1px solid var(--global-divider-color); border-radius: 0.75rem;">
            <img src="{{ photo.path | relative_url }}" alt="{{ caption | escape }}" data-zoomable loading="lazy" decoding="async" style="display: block; width: 100%; height: 320px; object-fit: contain; border-radius: 0.4rem;">
            <figcaption class="caption" style="margin-top: 0.75rem;">{{ caption | escape }}</figcaption>
          </figure>
        {% endfor %}
      </div>
    {% else %}
      <p style="color: var(--global-text-color-light);">Photos to come.</p>
    {% endif %}
  </section>
{% endfor %}
