#!/usr/bin/env python3
#
# CSV Generator fuer IDENT.TXT der Pool Pruefungen
#
# (c) Copyrights 2016-2018 Hartmut Seichter
#
# Licensed under BSD-2-Clause (https://opensource.org/licenses/BSD-2-Clause)
#

import os
import fnmatch
import re


class Parser:
    """Student holder"""
    def __init__(self):
        self.separator = ','


    """make a student instance from the line"""
    def parse_identfile_data(self,line):

        # muster:333333:I17 Muster Hans Peter:IP209:A:1
        fs = line.split(':') # first split
        # print(fs[1],fs[4].split(' ')[0],fs[4].split(' ')[1])
        s_id = fs[1]
        s_group = fs[4].split(' ')[0]
        s_name = fs[4].split(' ')[1]
        s_year = re.search(r'\d+',s_group)[0]
        s_group = s_group.replace(s_year,'')

        return { 'id':int(s_id), 'name':s_name, 'year':int(s_year), 'group':s_group, 'grade': 0  }

    """parse the point file - CSV"""
    def parse_pointfile_data(self,line):
        return list(map(float,line.split(self.separator)))


    """traverses the tree of exam folders and collecting id information"""
    def scan(self,dirname):
        students = []
        for root, dirnames, filenames in os.walk(dirname):
            for filename in fnmatch.filter(filenames, 'IDENT.TXT'):
                ident_file = os.path.join(root, filename)
                point_file = os.path.join(root, 'POINT.TXT')
                student = None
                # fetch identity
                with open(ident_file) as f:
                    for line in f:
                        student = self.parse_identfile_data(line)
                        student['root'] = root

                # fetch points
                with open(point_file) as f:
                    for line in f:
                        student['points'] = self.parse_pointfile_data(line)

                students.append(student)

        return students

    def json(self):
        r = []
        for s in self.students:
            r.append(s.json())
        return r

    def csv(self):
        r = ''
        for s in self.students:
            r = r + s.csv() + '\n'
        return r
