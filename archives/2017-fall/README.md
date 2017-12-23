# OCF/XCF DeCal Website

This is the source of the OCF/XCF Unix System Administration DeCal website, 
currently available at [decal.ocf.berkeley.edu](https://decal.ocf.berkeley.edu). 

The current iteration uses Jekyll to produce pages. 

When adding new lab markdown files, please don't forget to add the front matter
at the top of the document, otherwise the markdown will not be rendered. e.g.

    ---
    title: Lab 1 - Unix, the Shell, OSS
    layout: lab
    ---
    
Lab materials should be stored, as much as possible, in Puppet, which is located
in the [decal-puppet](https://github.com/0xcf/decal-puppet) repository. 
