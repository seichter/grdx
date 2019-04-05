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
    def __init__(self):
        self.bonus = { 'percent': 0.8, 'point': 1 }
        self.tasks = {}

    """calculate the result with bonus adjustment"""
    def get_bonus_points(self,points):
        if len(points) < len(list(self.tasks.keys())):
            return 0
        bonus = 0
        for i,e in enumerate(self.tasks):
            ratio = float(points[i] / self.tasks[e])
            if ratio >= self.bonus['percent']:
                bonus += self.bonus['point']
        return bonus

    def get_max_score(self):
        return sum(list(self.tasks.values()))

    def get_points(self,points):
        return sum(points) + self.get_bonus_points(points)

    def get_points_ratio(self,points):
        return max(0,min(self.get_points(points) / self.get_max_score(),1.0))
