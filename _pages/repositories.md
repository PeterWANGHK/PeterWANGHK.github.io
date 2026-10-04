---
layout: page
permalink: /repositories/
title: repositories
description: Open-source research code and collaborations.
---

{% if site.data.repositories.github_repos %}

## Highlighted repositories

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>
{% endif %}
