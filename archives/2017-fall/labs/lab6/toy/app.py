#!/usr/bin/env python3
from flask import Flask


app = Flask(__name__)
n = 0

@app.route('/')
def main():
    global n
    n += 1
    if n % 20 == 0:
        print('visitor', n, 'visited', flush=True)
    return 'congratulations, you are visitor #{}'.format(n)
