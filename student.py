#!/usr/bin/env python3
#
# CSV Generator fuer IDENT.TXT der Pool Pruefungen
#
# (c) Copyrights 2016-2018 Hartmut Seichter
#
# Licensed under BSD-2-Clause (https://opensource.org/licenses/BSD-2-Clause)
#

import re

from exam import Exam

class Student:
    """Student holder"""
    def __init__(self,id,name,year,group):
        self.id = id
        self.name = name
        self.year = year
        self.group = group
        self.score = 0.0
        self.score_valid = False
        
    """make a student instance from the line"""
    def parse(line):
        # muster:333333:I17 Muster Hans Peter:IP209:A:1
        fs = line.split(':') # first split
        # print(fs[1],fs[4].split(' ')[0],fs[4].split(' ')[1])
        s_id = fs[1]
        s_group = fs[4].split(' ')[0]
        s_name = fs[4].split(' ')[1]
        
        s_year = re.search(r'\d+',s_group)[0]
        s_group = s_group.replace(s_year,'')
        return Student(s_id,s_name,s_year,s_group)

    """calculate the result with bonus adjustment"""
    def csv(self):
        return ",".join([str(self.id),str(self.name),str(self.year),str(self.group),str(self.score),str(self.score_valid)])
        
    def json(self):
        return {'id' : str(self.id), 'name' : str(self.name), 'year' : str(self.year), 'group' : str(self.group), 'score' : float(self.score), 'valid' : str(self.score_valid) }
#
# entry point
#
if __name__ == "__main__":
    pass   
    
    
    