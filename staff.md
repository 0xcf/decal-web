---
layout: page
title: Staff
nav_order: 4
description: A listing of all the course staff members.
---

# Staff

## Head Facilitators

{% assign heads = site.staffers | where: 'role', 'Head Facilitator' %}
{% for staffer in heads %}
{{ staffer }}
{% endfor %}

{% assign facilitators = site.staffers | where: 'role', 'Facilitator' %}
{% assign num_facilitators = facilitators | size %}
{% if num_facilitators != 0 %}

## Facilitators

{% for staffer in facilitators %}
{{ staffer }}
{% endfor %}
{% endif %}
