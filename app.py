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

class Course(db.Model):
    id = db.Column(db.String(4),primary_key=True)
    name = db.Column(db.String(20))

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    course_id = db.Column(db.String,db.ForeignKey('course.id'))
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
    weight=db.Column(db.Number)
    name = db.Column(db.String(80))
    description = db.Column(db.String)
    points = db.Column(db.Integer)
    exam_id = db.Column(db.Integer,db.ForeignKey('exam.id'))

class Solution(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task_id = db.Column(db.Integer,db.ForeignKey('task.id'))
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))
    points = db.Column(db.Integer)
    comment = db.Column(db.String)


@app.route('/')
def index():
    db.create_all()
    return redirect('/students')

##
## Student
##
@app.route('/students',methods=['GET', 'POST'])
def students():
    if request.form:
        s = Student(id=request.form.get('student_id'),
            firstname=request.form.get('firstname'),
            lastname=request.form.get('lastname'),
            year=request.form.get('year'),
            course_id=request.form.get('course_id'))
        
        db.session.add(s)
        db.session.commit()

        print(request.form)

    template = env.get_template('index.html')

    out = template.render(students=Student.query.all(),courses=Course.query.all(),task='students')
    
    return out

@app.route('/student/delete', methods=['POST'])
def student_delete():
    s_id = request.form.get('student_id')
    s = Student.query.filter_by(id=s_id).first()
    db.session.delete(s)
    db.session.commit()
    
    return redirect('/')

##
## Course
##

@app.route('/course/delete', methods=['POST'])
def course_deleter():
    s_id = request.form.get('course_id')
    s = Course.query.filter_by(id=s_id).first()
    db.session.delete(s)
    db.session.commit()
    
    return redirect('/courses')


@app.route('/courses',methods=['GET', 'POST'])
def courses():
 
    if request.form:
        c = Course(id=request.form.get('course_id'),name=request.form.get('name'))
        db.session.add(c)
        db.session.commit()

    template = env.get_template('index.html')
    out = template.render(courses=Course.query.all(),task='courses')
    
    return out

##
## Exams
##

@app.route('/exams',methods=['GET','POST'])
def exams():

    if request.form:
        e = Exam(name=request.form.get('name'),description=request.form.get('description'))
        db.session.add(e)
        db.session.commit()
        print(e)

    template = env.get_template('index.html')
    out = template.render(exams=Exam.query.all(),task='exams')

    return out

@app.route('/exam/delete', methods=['POST'])
def exam_deleter():
    e_id = request.form.get('exam_id')
    e = Exam.query.filter_by(id=e_id).first()
    db.session.delete(e)
    db.session.commit()
    
    return redirect('/exams')

##
## Task
## 

@app.route('/task',methods=['GET','POST'])
def task():

    if request.form:
        e = Task(name=request.form.get('name'),
            description=request.form.get('description'))
        db.session.add(e)
        db.session.commit()
        print(e)

    template = env.get_template('index.html')
    out = template.render(exams=Exam.query.all(),task='exams')
    return out


# @app.route('/edit/id/<int:identifier>')
# def student_edit(identifier):
#     print(identifier)
#     return "test! " + str(identifier)
