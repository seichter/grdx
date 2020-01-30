#!/usr/bin/env python3
#
# CSV Generator fuer IDENT.TXT der Pool Pruefungen
#
# (c) Copyrights 2016-2018 Hartmut Seichter
#
# Licensed under BSD-2-Clause (https://opensource.org/licenses/BSD-2-Clause)
#

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from sqlalchemy_utils import create_database, database_exists

Base = declarative_base()

class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    course = Column(String)
    year = Column(Integer)


    """Student holder"""
    def __init__(self,id,**kwargs):
        super()
        self.id =  id
        self.name = kwargs['name']
        self.year = kwargs['year']
        self.course = kwargs['course']

    """calculate the result with bonus adjustment"""
    def csv(self):
        return ",".join([str(self.id),str(self.name),str(self.year),str(self.field)])

    """ returns in json"""
    def json(self):
        return {'id' : str(self.id), 'name' : str(self.name), 'year' : str(self.year), 'course' : str(self.course) }

    def __repr__(self):
        return "<student %i %s %s/>" % (self.id, self.name, self.course)
 


class Exam(Base):

    __tablename__ = 'exam'

    id = Column(Integer,primary_key=True)
    name = Column(String)

    def __init__(self,**kwargs):
        super()
    

class Task(Base):
    
    __tablename__ = 'task'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    
    




def main():

    s1 = Student(30303,name='Hans Muster',year='2010',course='INF')
    s2 = Student(40404,name='Erna Muster',year='2011',course='INF')

    # print(s)

    global engine

    url = 'sqlite:///data/test.db'
    engine = create_engine(url, echo=True)

   
    if not database_exists(url):
        create_database(url)

    engine = create_engine(url, echo=False)
    
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Debugging
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session.add(s1)
    session.add(s2)

    session.commit()
 
    qs = session.query(Student).filter(Student.course.in_(['INF'])).all()

    print(qs)

    qs[0].name = 'Lord Voldemort'

    session.commit()


    qs = session.query(Student).filter(Student.course.in_(['INF'])).all()


    for s in qs:
        print(s.json())
	
if __name__ == '__main__':
    main()

