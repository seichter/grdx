#!/usr/bin/env python3

import os

from datetime import datetime

from flask import Flask, escape, request, redirect
from flask_sqlalchemy import SQLAlchemy

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/test2.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))
    course = db.Column(db.String(80))
    year = db.Column(db.Integer)

    def __repr(self):
        return '<Student %i>' % self.id

class Exam(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    tasks = db.relationship('Task',backref=db.backref('exam',lazy=True))

class Enrollment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    exam_id = db.Column(db.Integer,db.ForeignKey('exam.id'))
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String())
    points = db.Column(db.Integer)
    exam_id = db.Column(db.Integer,db.ForeignKey('exam.id'))

    

@app.route('/debug/new')
def student_new():
    s1 = Student(id=40404,name='Hans Hein',course='INF')
    db.session.add(s1)
    db.session.commit()
    return "Done"


@app.route('/', methods=['GET', 'POST'])
def web_main():

    db.create_all()

    if request.form:
        s = Student(id=request.form.get('student_id'),
            name=request.form.get('name'),
            year=request.form.get('year'),
            course=request.form.get('course'))
        
        db.session.add(s)
        db.session.commit()

        print(request.form)

    template = env.get_template('index.html.jinja2')

    out = template.render(students=Student.query.all())
    
    return out

@app.route('/student/delete', methods=['POST'])
def student_delete():
    s_id = request.form.get('student_id')
    s = Student.query.filter_by(id=s_id).first()
    db.session.delete(s)
    db.session.commit()
    
    return redirect('/')



@app.route('/edit/id/<int:identifier>')
def student_edit(identifier):
    print(identifier)
    return "test! " + str(identifier)
