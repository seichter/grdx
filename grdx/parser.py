#!/usr/bin/env python3
#
# CSV Generator fuer IDENT.TXT der Pool Pruefungen
#
# (c) Copyrights 2016-2018 Hartmut Seichter
#
# Licensed under BSD-2-Clause (https://opensource.org/licenses/BSD-2-Clause)
#
# Nutzung (im Pruefungsverzeichnis): ./gen_usercsv.py > PART_INF.csv
#

import os
import fnmatch

from grdx.student import Student

class Parser:
    """Student holder"""
    def __init__(self,exam,grades):
        self.students = []
        self.exam = exam
        self.grades = grades

    """traverses the tree of exam folders and collecting id information"""
    def start(self,dirname):
        for root, dirnames, filenames in os.walk(dirname):
            for filename in fnmatch.filter(filenames, 'IDENT.TXT'):
                ident_file = os.path.join(root, filename)
                point_file = os.path.join(root, 'POINT.TXT')

                score = 0.0
                score_valid = False # flag to differentiate

                if os.path.isfile(point_file):
                    with open(point_file) as f:
                        for line in f:
                            score = self.exam.score(line)
                            score_valid = True

                with open(ident_file) as f:
                    for line in f:
                        s = Student.parse(line)
                        s.score = self.grades.lookup(score)
                        s.score_valid = score_valid
                        self.students.append(s)
                #


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
