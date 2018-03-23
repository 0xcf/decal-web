# OCF/XCF DeCal Website

[![Build Status](https://jenkins.ocf.berkeley.edu/buildStatus/icon?job=decal-web/master)](https://jenkins.ocf.berkeley.edu/job/decal-web/)

This is the source of the OCF/XCF Unix System Administration DeCal website,
currently available at [decal.ocf.berkeley.edu](https://decal.ocf.berkeley.edu).

The current iteration uses Jekyll to produce pages.

### Preparation

Install ruby development tools and bundler:

`sudo apt-get install ruby-dev && sudo gem install bundler`

### Running webserver

`make dev` or `make local-dev` for local deployments.

When adding new lab markdown files, please don't forget to add the front matter
at the top of the document, otherwise the markdown will not be rendered. e.g.

    ---
    title: Lab 1 - Unix, the Shell, OSS
    layout: lab
    ---

Lab materials should be stored, as much as possible, in Puppet, which is located
in the [decal-puppet](https://github.com/0xcf/decal-puppet) repository.
