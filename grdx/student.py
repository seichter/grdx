#!/usr/bin/env python3
#
# CSV Generator fuer IDENT.TXT der Pool Pruefungen
#
# (c) Copyrights 2016-2018 Hartmut Seichter
#
# Licensed under BSD-2-Clause (https://opensource.org/licenses/BSD-2-Clause)
#


class Student:
    """Student holder"""
    def __init__(self,id,name,year,group,root):
        self.id = id
        self.name = name
        self.year = year
        self.group = group
        self.score = 0.0
        self.score_valid = False
        self.submission_root = root



    """calculate the result with bonus adjustment"""
    def csv(self):
        # just a test ,str(self.submission_root)
        return ",".join([str(self.id),str(self.name),str(self.year),str(self.group),str(self.score),str(self.score_valid)])

    def json(self):
        return {'id' : str(self.id), 'name' : str(self.name), 'year' : str(self.year), 'group' : str(self.group), 'score' : float(self.score), 'valid' : self.score_valid }
