---
layout: page
title: About
nav_order: 2
description: >-
    Course policies and information.
---

# About
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

# Course Description

This course covers the basics of setting up and administering a production-quality Linux server environment. By the end of this course, we expect that you will...

* be comfortable using GNU/Linux
* understand how different parts of the OS work together, e.g. init, processes, daemons, filesystems, etc.
* understand basic networking on Linux
* have a good sense about maintaining system security
* understand system administration essentials
* get a practical taste of what sysadmins do in industry.

The course will be taught in two sections: a "Beginner" section for students with minimal background in GNU/Linux or system administration, and an "Advanced" section for students with more experience.

While we expect many students will have a CS background, **the only real prerequisite is a desire to learn** about new and unfamiliar technologies, which is a critical skill for sysadmins. The Beginner section has been designed to introduce new users to Linux, and the Advanced section has been designed to give more experienced users a taste of what Linux is capable of.

# Administrivia

## Enrollment
This is a **2 unit DeCal**. Since it is a DeCal, the course is P/NP. **You must complete Lab 0 to apply.** If you are selected for the course, we will send you a course enrollment code by January 30.

## Communication
Official course communications will primarily be sent via email (through Piazza announcements), and mirrored on the front page of the course website.

There are several ways you can get in contact with course facilitators:
1. Send a message on the course Piazza. (best for conceptual/debugging/content help)
2. Send a message to #decal-general (or as a private message to a facilitator) either on [Slack][slack] or [Discord][discord]. (best for realtime communications)
3. Send an email to [decal@ocf.berkeley.edu][email]. (best for prospective students and matters that need to go on official record)

## Lecture

Lectures for this course are asynchronous, and videos will be released at the beginning of each week. There will be 10 total lectures for each track, as well as one optional guest lecture (details TBD).

A short assignment will be released with every lecture with some questions to check your understanding. To receive participation credit for that week, you may either complete this assignment or attend a lab section (see [live labs](#live-labs)).

All lab assignments will assume that you have already viewed the lecture in its entirety, and may be difficult to complete without watching lecture first.

## Lab Assignments
The primary assignment in this course will be **weekly lab work**. Labs are designed to be be significantly hands-on. You will be working on real systems, configuring and fixing things, setting up services, and so on.

Each lecture corresponds with a lab, labeled by a "b" or "a" (for Beginner or Advanced) and the week number. Labs will be released at the same time as the lectures on Sundays. 

Each lab will be due by the **Saturday, 11:59pm PST** after the lab section unless otherwise stated. Labs (and lectures) will be released the prior Sunday, so you will have a week to complete them.

**You must complete 10 labs to receive credit for taking the course.** The late due date for labs is 2 weeks after the original due date. You may submit up to 2 labs late throughout the semester without penalty.

If you need to request an **excused lab extension or drop**, please fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSde6CIiaA1Z-U3vSxDU_AbmyyWKEVPKa-vhHEysltLsG2de3A/viewform). Doing so will not affect your two unexcused late labs.

You are *highly encouraged* to look over the lab, and try to start it, *before* coming to live lab sections each week. This will allow you to better utilize the help of the facilitators.

## Live Labs
During the scheduled Tuesday and Thursday class times from 8:10-9pm, we will host live lab sections, where facilitators will give additional information, demos related to the lab, walk through solutions to participation assignments, and hold office hours to answer any questions that may arise. Lab sections will be held in the OCF lab (171 MLK, [click here](https://www.ocf.berkeley.edu/docs/services/lab/) for directions).  If you are unable to attend for any reason, you may also complete an alternate participation assignment. 7 out of 10 attendance assignments must be completed over the semester (either by attending, or completing the assignment).


## Grading
The following are required to receive credit for the course:
* 10 completed lab assignments
    * Lab assignments are graded on completion, *not* correctness. Blank or otherwise extremely low-effort submissions (i.e. no visible attempt at answering the questions asked) will be considered incomplete.
* 7 completed participation assignments
    * You will have the option of either attending live lab or answering questions about the lecture to receive credit for these assignments.

# FAQ

## Will the DeCal be offered next semester?
The DeCal has been approved for Spring 2022 and will be happening! There will be more information on how to enroll closer to the start of the semester; in the meantime, please fill out our [interest form](https://docs.google.com/forms/d/e/1FAIpQLSdGESPxNAGEhbrzhterrEi_sT3idf3TjTLjOC0UbEcj0WeqsA/viewform) to stay updated.

The DeCal will likely not be offered in Fall 2022, but this is subject to change.

## How do I know which track is best for me?
**Beginner Track** is intended for those who have little to no prior experience of using Linux-based systems. We will be providing an overview to several important concepts in systems administration, such as networking, shell scripting, version control, and security. It's perfectly OK if you've never worked with or heard of these concepts before- but if you're familiar with them, we recommend you opt for the advanced track. Overall, we welcome everyone to this track!

**Advanced Track** is intended for those who have used Linux-based systems before and are at least somewhat familiar with some of the concepts mentioned in the beginner track description above. While there are no hard/enforced prerequisites, we do recommend that you have experience with one or more of the following:

 - Using Linux as a primary/secondary OS
 - Using a package manager such as `apt` or `pacman`
 - Writing scripts to automate basic tasks
 - Basic networking (such as working with IP addresses)

If you are still unsure about which track to choose, you can email us at [decal@ocf.berkeley.edu][email].

## I don't want units / wasn't accepted / am not a student. Can I audit this course?
We are working hard to get all of our materials online this semester for everyone to access! Feel free to view our lectures or complete any of the labs on your own. (You will
need your own Linux VM though- you can [install one locally](https://blog.storagecraft.com/the-dead-simple-guide-to-installing-a-linux-virtual-machine-on-windows/) or get one from a provider such as [DigitalOcean](https://www.digitalocean.com/).)

## I'm stuck on a lab/concept! Where can I find help?
The best way to get support with course content is to ask during scheduled lab times. If you need help at another time, feel free to ask on Piazza, on our Slack channel at [#decal-general][slack], or on our [Discord channel][discord]. Logistics questions are best suited for email ([decal@ocf.berkeley.edu][email]).

## I have another question!
Email us at [decal@ocf.berkeley.edu][email].

[email]: mailto:decal@ocf.berkeley.edu
[slack]: https://ocf.io/slack
[discord]: https://ocf.io/discord

# After this Course

There's no substitute for real-world experience. If you'd like to get experience in a low-risk but real-world setting, consider [joining the OCF](https://ocf.io/getinvolved) as a volunteer staff member. There, you'll be able to put the things you learn in this course to use, and help other students while you're at it. Best of all- **there's no application process**! Just drop by and say hi :)

Weekly staff meetings are held Wednesdays at 8pm at the OCF lab.
