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
## Week 0: 1/25/2021
{: .text-gamma }

Infosession
: **Infosession**{: .label .label-yellow}[ocf.io/decalzoom](https://ocf.io/decalzoom)
    : [Slides](https://docs.google.com/presentation/d/1gnrplHLppSMhJiZniV3MSoZ8AbeEOLOs0T1EsclftQw/edit)
: **Lab**{: .label .label-yellow}[Lab 0](https://docs.google.com/forms/d/e/1FAIpQLSfY53eBRA8e1NfR2GcwsMDL9AS1Pj1cSJh-I0j_jKOEE1o7iQ/viewform)
    : **Lab due Sat. 1/30**
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
</div>
{% endfor %}


<div class="module" markdown="1">
## Week 11
{: .text-gamma }
Extra Lab! (Optional)
: **Lab**{: .label .label-yellow} Lab 11
    : **Lab due Sun. 5/9**

Special Guest Lecture
: **Lecture**{: .label .label-yellow} Careers in Systems Administration
    : Date/Details TBA
</div>


    