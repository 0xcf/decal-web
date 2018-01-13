# OCF/XCF DeCal Website

This is the source of the OCF/XCF Unix System Administration DeCal website, 
currently available at [decal.ocf.berkeley.edu](https://decal.ocf.berkeley.edu). 

The current iteration uses Jekyll to produce pages. 

### Preparation

Make sure to run these commands in the project root!
Install ruby and bundler: `sudo apt-get install ruby-dev && sudo gem install bundler`
Install gems: `mkdir -p vendor/bundle && bundle install --path vendor/bundle`

### Running webserver

`bundle exec jekyll serve`

When adding new lab markdown files, please don't forget to add the front matter
at the top of the document, otherwise the markdown will not be rendered. e.g.

    ---
    title: Lab 1 - Unix, the Shell, OSS
    layout: lab
    ---
    
Lab materials should be stored, as much as possible, in Puppet, which is located
in the [decal-puppet](https://github.com/0xcf/decal-puppet) repository. 
