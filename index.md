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
## Week 0: 1/22/2023
{: .text-gamma }

Infosession
: **Infosession 1**{: .label .label-yellow} Tuesday 1/24, 9-10pm @ VLSB 2060 / [ocf.io/decalzoom](https://ocf.io/decalzoom)
: **Infosession 2**{: .label .label-yellow} Thursday 1/26, 8-9pm @ OCF / [ocf.io/decalzoom](https://ocf.io/decalzoom)
: **Lab**{: .label .label-blue}[ocf.io/decal/lab0](https://ocf.io/decal/lab0)
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
**Lecture**{: .label .label-green}{{week.name}} : [Recording]({{week.video}}), [Slides]({{week.slides}}){:target="_blank"} <br />
**Lab**{: .label .label-blue}[Lab {{week.id}}](labs/{{week.id}}) {% if week.labdue %}due **{{week.labdue}}**{% endif %}


{% endif %}
</div>
{% endfor %}
