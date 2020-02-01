#!/usr/bin/env python3

from flask import Flask, escape, request 
from flask_sqlalchemy import SQLAlchemy

from jinja2 import Template

app = Flask(__name__)


@app.route('/')
def web_main():
    with open('html/index.html.jinja2') as file_:
        name = request.args.get("name", "World")
        template = Template(file_.read())
        
        passed = 1
        checked = 100
        
        out = template.render()

        return out

        # return f'Hello, {escape(name)}!'
