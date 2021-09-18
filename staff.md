---
layout: page
title: Staff
nav_order: 4
description: A listing of all the course staff members.
---

# Staff

## Communication
Official course communications will primarily be sent via email and mirrored on the front page of the course website.

There are several ways you can get in contact with course facilitators:
1. Send a message on the course Piazza. (best for conceptual/debugging/content help)
2. Send a message to #decal-general (or as a private message to a facilitator) either on [Slack](https://ocf.io/slack) or [Discord](https://ocf.io/discord). (best for realtime communications)
3. Send an email to [decal@ocf.berkeley.edu](mailto:decal@ocf.berkeley.edu). (best for prospective students and matters that need to go on official record)

See the [about page](/about) for more information.

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
