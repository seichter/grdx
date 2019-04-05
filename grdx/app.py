#!/usr/bin/env python3
#
# CSV Generator fuer IDENT.TXT der Pool Pruefungen
#
# (c) Copyrights 2016-2018 Hartmut Seichter
#
# Licensed under BSD-2-Clause (https://opensource.org/licenses/BSD-2-Clause)
#

from grdx.exam import Exam
from grdx.parser import Parser
from grdx.grades import Grades

class App:
    def __init__(self,argv):
        self.submissions = []
        self.exam = Exam()
        self.exam.tasks = argv['tasks']
        self.grades = Grades(argv['grades_min'],argv['grades_max'])
        self.parser = Parser()
        self.submissions = self.parser.scan(argv['path'])


    def update_grades(self):
        for s in self.submissions:
            # get ratio
            ratio = self.exam.get_points_ratio(s['points'])
            # lookup grade
            s['grade'] = self.grades.lookup(ratio)

    def histogram(self):
        h = {}
        for g in self.grades.grades:
            h[g] = 0
        for s in self.submissions:
            h[s['grade']] += 1
        return h

    def count(self):
        return len(self.submissions)

    def passed(self):
        p = 0
        for s in self.submissions:
            if s['grade'] <= 4.0:
                p += 1
        return p

    def checked(self):
        c = 0
        for s in self.submissions:
            if s['grade'] > 0:
                c += 1
        return c

    def passed_ratio(self):
        return self.passed() / len(self.submissions)

    def json(self):
        return self.submissions

    def csv(self):
        # slice back of the keys (path and points)
        k = list(self.submissions[0].keys())[0:-2]
        lines = []
        lines.append( ",".join(k) ) # header
        for s in self.submissions:
            v = list(s.values())[0:-2]
            lines.append( ",".join(map(str,v)) )
        return "\n".join(lines)
