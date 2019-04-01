#!/usr/bin/env python3
#
# grdx - grading tool
#
# (c) Copyrights 2016-2018 Hartmut Seichter
#
# Licensed under BSD-2-Clause (https://opensource.org/licenses/BSD-2-Clause)
#

from sanic import Sanic
from sanic import response
from jinja2 import Template

import grdx
import os
import yaml

app = Sanic()

config = yaml.safe_load(open("config/config.yml"))

print('grdx-web ',config['path'])
print('grdx-web ',config['points'])
print('grdx-web ',config['bonus'])

@app.route("/")
async def index(request):
    with open('html/template.html.jinja2') as file_:
        template = Template(file_.read())
        return response.html(template.render())

@app.route("/data")
async def test(request):
    e = grdx.Exam([4, 10, 10, 10, 4], (0.8,1) )
    g = grdx.Grades(0.40,0.95)
    
    p = Parser(e,g)
    
    p.start()
    # p.start(os.getcwd())
    return response.json( p.json() )


# @app.route("/test2")
# async def test(request):
#     return response.html('<p>Hello world!</p>')
#
# @app.route("/test3")
# async def test(request):
#     return response.html(template.render())
#
# @app.route("/other")
# async def test(request):
#     async def sample_streaming_fn(response):
#         await response.write(await template.render_async(key='<b>foo</b>'))
#         await asyncio.sleep(1) # just for checking if it's indeed streamed
#         await response.write(await template.render_async(key='<b>bar</b>'))
#     return response.stream(sample_streaming_fn, content_type='text/html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)