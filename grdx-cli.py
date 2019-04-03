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

import glob, os, sys
import re
import math
import yaml

from grdx.exam import Exam
from grdx.parser import Parser
from grdx.grades import Grades

# PROJECT_ROOT = abspath()
sys.path.insert(0,os.path.dirname(__file__))

# load configuration
config = yaml.safe_load(open("config/config.yml"))

#
# entry point
#
if __name__ == "__main__":
    # print(grdx)
    e = Exam(config['points'], (0.8,1) )
    g = Grades(config['grades_min'],config['grades_max'])
    p = Parser(e,g)
    p.start(config['path'])
    print(p.csv())
