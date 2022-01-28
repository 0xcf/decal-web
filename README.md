# OCF/XCF Linux SysAdmin DeCal Website

[![Build Status](https://jenkins.ocf.berkeley.edu/buildStatus/icon?job=decal-web/master)](https://jenkins.ocf.berkeley.edu/job/decal-web/)

This is the source of the OCF/XCF Unix System Administration DeCal website, currently available at [decal.ocf.berkeley.edu](https://decal.ocf.berkeley.edu).

The current iteration uses Jekyll to produce pages.

## Development

decal-web is built for [Jekyll](https://jekyllrb.com), a static site generator. View the [quick start guide](https://jekyllrb.com/docs/) for more information.

### Developing on Supernova

This is the recommended method of development. 

1. SSH into supernova
```bash
$ ssh <ocf-username>@supernova.ocf.berkeley.edu
```
1. Clone this repository
```bash
$ git clone https://github.com/0xcf/decal-web
```
1. Start the Jekyll server on supernova with:
```bash
$ cd decal-web
$ make supernova
```

The console should ouput a web address (`http://supernova.ocf.berkeley.edu:8xxx/`). This web-page will update as you make changes, reload your browser tab to preview the changes.

### Developing on your local machine

You will need Ruby 2 to build the site (it has been tested on Ruby2.7.4). 
* On Ubuntu 20.04, Ruby can be installed using `sudo apt install ruby-full`.
* If using Arch, [follow this guide](https://gist.github.com/jhass/8839655bb038e829fba1) to install it.
* [ruby-install](https://github.com/postmodern/ruby-install) is a helpful script- you can run `ruby-install 2.7.4` if Ruby is on the wrong version in your package manager.

You may also need to install Bundler 2.2.25: `gem install bundler:2.2.25`

1. Install Jekyll
```bash
$ bundle install
```
1. Start your local Jekyll server. You can also use `make local-dev`.
```bash
$ bundle exec jekyll serve
```
1. The console should output a server address (`localhost:8xxx`). Open that address in your browser.
1. Reload your web browser after making a change to preview its effect.

For more information, refer to [Just the Docs](https://pmarsceill.github.io/just-the-docs/).
