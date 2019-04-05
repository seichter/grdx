#!/usr/bin/env python3
#
# CSV Generator fuer IDENT.TXT der Pool Pruefungen
#
# (c) Copyrights 2016-2018 Hartmut Seichter
#
# Licensed under BSD-2-Clause (https://opensource.org/licenses/BSD-2-Clause)
#

class Exam:
    """Exam holder"""
    def __init__(self,scores,bonus = (1.0,1) ):
        self.scores = scores
        self.bonus = bonus
        self.separator = ','
        self.tasks = []

    def score(self,line):
        points = list(map(float,line.split(self.separator)))
        return self.result(points)

    """calculate the result with bonus adjustment"""
    def result(self,points):
        points_adjusted = []
        for i,e in enumerate(points):
            task_ratio = float(e)  / self.scores[i]
            points_adjusted.append(e)
            if task_ratio >= self.bonus[0]:
                points_adjusted.append(self.bonus[1])
        return max(0, min(float(sum(points_adjusted)) / sum(self.scores), 1))
#
# entry point
#
if __name__ == "__main__":
    e = Exam([4, 10, 10, 10, 4], (0.8,1) )

    r = e.result([4,9,3,9,4])

    print(r)
