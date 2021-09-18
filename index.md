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
[Announcements](announcements.md){: .btn .btn-outline .fs-3 }
{% endif %}

## Weekly Schedule
{% for schedule in site.schedules %}
{{ schedule }}
{% endfor %}

# Calendar

<div class="module" markdown="1">
## Week 0: 8/30/2021
{: .text-gamma }

Infosession
: **Infosession**{: .label .label-yellow}[ocf.io/decalzoom](https://ocf.io/decalzoom)
   : [Slides](https://docs.google.com/presentation/u/4/d/1reHYTzb-19HYRSWwZkmXI8Oa-r328vqJ28VtHmNazGA/edit)
: **Lab**{: .label .label-yellow}[Lab 0](https://docs.google.com/forms/d/10O6C7dWiRRc1O-q46jx_q-3IIWQobwFdn9TmyQ8qt5M/edit)
    : **Lab due Sat. 9/4**
</div>
{% for week in site.data.materials %}
<div class="module" markdown="1">
## Week {{week.id}}: {{week.date}}
{: .text-gamma }

{% if week.hidelink %}
Beginner Track
: **Lecture**{: .label .label-green}{{week.beginner-name}}
: **Lab**{: .label .label-blue}Lab b{{week.id}}
    : **Lab due {{week.labdue}}**

Advanced Track
: **Lecture**{: .label .label-purple }{{week.advanced-name}}
: **Lab**{: .label .label-red}Lab a{{week.id}}
    : **Lab due {{week.labdue}}**
    
{% elsif week.beginner-solutions %}
Beginner Track
: **Lecture**{: .label .label-green}[{{week.beginner-name}}]({{week.beginner-video}}) 
    : [Slides]({{week.beginner-slides}}){:target="_blank"}
: **Lab**{: .label .label-blue}[Lab b{{week.id}}](/labs/b{{week.id}}) [(Solution)]({{week.beginner-solutions}})
    : **Lab due {{week.labdue}}**

Advanced Track
: **Lecture**{: .label .label-purple }[{{week.advanced-name}}]({{week.advanced-video}})
    : [Slides]({{week.advanced-slides}}){:target="_blank"}
: **Lab**{: .label .label-red}[Lab a{{week.id}}](/labs/a{{week.id}}) [(Solution)]({{week.advanced-solutions}})
    : **Lab due {{week.labdue}}**
{% else %}
Beginner Track
: **Lecture**{: .label .label-green}[{{week.beginner-name}}]({{week.beginner-video}}) 
    : [Slides]({{week.beginner-slides}})
: **Lab**{: .label .label-blue}[Lab b{{week.id}}](/labs/b{{week.id}})
    : **Lab due {{week.labdue}}**

Advanced Track
: **Lecture**{: .label .label-purple }[{{week.advanced-name}}]({{week.advanced-video}})
    : [Slides]({{week.advanced-slides}}){:target="_blank"}
: **Lab**{: .label .label-red}[Lab a{{week.id}}](/labs/a{{week.id}})
    : **Lab due {{week.labdue}}**
{% endif %}

## Communication
Official course communications will primarily be sent via email, and mirrored on the front page of the course website.

There are several ways you can get in contact with course facilitators:
1. Send a message on the course Piazza. (best for conceptual/debugging/content help)
2. Send a message to #decal-general (or as a private message to a facilitator) either on [Slack][slack] or [Discord][discord]. (best for realtime communications)
3. Send an email to [decal@ocf.berkeley.edu][email]. (best for prospective students and matters that need to go on official record)

See the [about page](about.md) for more information.

[email]: mailto:decal@ocf.berkeley.edu
[slack]: https://ocf.io/slack
[discord]: https://ocf.io/discord

</div>
{% endfor %}


