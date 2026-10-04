---
layout: page
title: news
permalink: /news/
description: Research updates, events, and milestones.
---

<div class="news table-responsive">
  <table class="table table-sm table-borderless">
    {% assign updates = site.news | reverse %}
    {% for update in updates %}
    <tr>
      <th scope="row" style="width: 20%">{{ update.date | date: '%b %Y' }}</th>
      <td>{{ update.content | remove: '<p>' | remove: '</p>' | emojify }}</td>
    </tr>
    {% endfor %}
  </table>
</div>
