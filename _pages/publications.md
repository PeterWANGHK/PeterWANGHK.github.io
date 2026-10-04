---
layout: page
title: publications
permalink: /publications/
description: Publications and manuscripts in autonomous driving, robotics, and intelligent systems.
nav: true
nav_order: 1
---

_An asterisk (\*) indicates the corresponding author; a dagger (†) indicates a co-first author._

{% include bib_search.liquid %}

## First-authored and co-first-authored

<div class="publications">
{% bibliography --query @*[category=lead] %}
</div>

## Collaborative work

<div class="publications publications--collaborative">
{% bibliography --query @*[category=collaborative] %}
</div>
