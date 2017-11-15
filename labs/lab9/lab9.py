# -*- coding: utf-8 -*-
# A simple Flask demo app that demonstrates one basic route, favicons,
# and static files. Written for my tutorial,
# Deploying Python Web Applications with nginx and uWSGI Emperor.
# <https://go.chriswarrick.com/pyweb>
# Copyright © 2016-2017, Chris Warrick.  All rights reserved.
# Licensed under the 2-clause BSD license.

from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
        return ('<!DOCTYPE html>\n'
                            '<meta charset="utf-8">\n<title>Hello from Flask!</title>\n'
                                        '<h1>Hello from Flask!</h1>\n<img src="/static/hello.png">\n')


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5001)

