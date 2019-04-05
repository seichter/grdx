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

from sanic.response import text
from sanic.response import json

from grdx.exam import Exam
from grdx.parser import Parser
from grdx.grades import Grades
from grdx.app import App as GradX

import os
import yaml

config = yaml.safe_load(open("config/config.yml"))

app = Sanic()
backend = GradX(config)
#
# e = Exam(config['points'], (0.8,1) )
# g = Grades(config['grades_min'],config['grades_max'])
# p = Parser(e,g)


# print('grdx-web ',config['path'])
# print('grdx-web ',config['points'])
# print('grdx-web ',config['tasks'])
# print('grdx-web ',config['bonus'])

@app.route("/")
async def index(request):
    with open('html/index.html.jinja2') as file_:
        backend.update_grades()
        checked = backend.checked()
        passed = backend.passed()
        all = backend.count()
        template = Template(file_.read())
        # return response.html(template.render())
        return response.html(template.render(num_all = all, num_checked=checked, num_passed = passed, checked_ratio=round(checked/all*100,1), passed_ratio=round(passed/checked*100,1)))

@app.route("/histogram")
async def index(request):
    backend.update_grades()
    return response.json( [ backend.histogram() ] )

@app.route("/data")
async def test(request):
    backend.update_grades()
    return response.json( backend.json() )

@app.route('/student/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    for s in backend.submissions:
        if int(s['id']) == integer_arg:
            with open('html/student.html.jinja2') as file_:
                template = Template(file_.read())
                return response.html(template.render(student=s,tasks = config['tasks']))


# @app.route('/student/update', methods=['POST'])
# async def post_handler(request):
#     # print(request.form['Flappy'])
#     # print(request.form['student_id'])
#
#     for s in p.students:
#         if s.id == request.form['student_id'][0]:
#             # print(os.path.join(s.submission_root,'POINT.TXT'))
#             points = []
#             for t in config['tasks']:
#                 # print(request.form[t][0],t)
#                 points.append(request.form[t][0])
#             print(",".join(points))
#             with open(os.path.join(s.submission_root,'POINT.TXT'),'w') as file:
#                 file.write(",".join(points))
#                 file.close()
#
#     return response.redirect('/student/' + request.form['student_id'][0])
	# return text('POST request - {}'.format(request.form))

	# return text('Integer - {}'.format(integer_arg))

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
    # current_directory = os.path.dirname(os.path.abspath(current_file))
    # js_dir = os.path.join(current_directory, 'js')
    # css_dir = os.path.join(current_directory, 'css')

    app.static('/css','./css')
    app.static('/js','./js')


    app.run(host="0.0.0.0", port=8000)
