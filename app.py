#!/usr/bin/env python3

from datetime import datetime

from flask import Flask, escape, request 
from flask_sqlalchemy import SQLAlchemy

from jinja2 import Template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/test2.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))
    course = db.Column(db.String(80))

    def __repr(self):
        return '<Student %i>' % self.id

class Exam(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    tasks = db.relationship('Task',backref=db.backref('exam',lazy=True))

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String())
    points = db.Column(db.Integer)
    exam_id = db.Column(db.Integer,db.ForeignKey('exam.id'))



@app.route('/debug/new')
def student_new():
    s1 = Student(id=30030,name='Erna Muster',course='INF')
    db.session.add(s1)
    db.session.commit()
    return "Done"


@app.route('/')
def web_main():

    db.create_all()

    with open('html/index.html.jinja2') as file_:
        name = request.args.get("name", "World")
        print(name)
        template = Template(file_.read())
        
        passed = 1
        checked = 100
        
        out = template.render()
        return out

        # return f'Hello, {escape(name)}!'
