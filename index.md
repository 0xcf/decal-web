---
layout: home
title: Home
nav_order: 1
seo:
  type: Course
  name: Linux Sysadmin Decal
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{% if site.announcements %}
{{ site.announcements.last }}
{% endif %}

## Weekly Schedule
{% for schedule in site.schedules %}
{{ schedule }}
{% endfor %}

# Calendar

<div class="module" markdown="1">
## Week 0: 8/29/2023
{: .text-gamma }

**Infosession**{: .label .label-yellow} Tues 8/29 & Thurs 8/31, 7-9pm @ OCF Lab / [ocf.io/decalzoom](https://ocf.io/decalzoom)
<br />
**Lab**{: .label .label-blue}[Lab 0](lab0) due **Sat 9/2**
</div>



{% for week in site.data.materials %}
<div class="module" markdown="1">
## Week {{week.id}}: {{week.date}}
{: .text-gamma }

{% if week.hidelink %}
**Lecture**{: .label .label-green}{{week.name}} <br />
**Lab**{: .label .label-blue}Lab {{week.id}}

{% elsif week.solutions %}
**Lecture**{: .label .label-green}[{{week.name}}]({{week.video}}) 
    : [Slides]({{week.slides}}){:target="_blank"}
: **Lab**{: .label .label-blue}[Lab {{week.id}}](labs/b{{week.id}}) &nbsp; &nbsp; [(Solution)]({{week.solutions}})
    : **Lab due {{week.labdue}}**

{% else %}
**Lecture**{: .label .label-green}{{week.name}} : {% if week.slides %}[Slides]({{week.slides}}){:target="_blank"}, {% endif %} {% if week.video %}[Recording]({{week.video}}){% endif %} {% if week.video_password %} with password `{{week.video_password}}`` {% endif %}<br />
**Lab**{: .label .label-blue}[Lab {{week.id}}](labs/{{week.id}}){% if week.labdue %} due **{{week.labdue}}**{% endif %}

{% endif %}
</div>
{% endfor %}
