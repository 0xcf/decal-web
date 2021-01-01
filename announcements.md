---
layout: page
title: Announcements
description: A feed containing all of the class announcements.
---

# Announcements

Check back to this page periodically to find out about new assignments, special events, and more!

{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements %}
{{ announcement }}
{% endfor %}
