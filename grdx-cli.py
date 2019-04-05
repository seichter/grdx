#!/usr/bin/env python3
#
# CSV Generator fuer IDENT.TXT der Pool Pruefungen
#
# (c) Copyrights 2016-2018 Hartmut Seichter
#
# Licensed under BSD-2-Clause (https://opensource.org/licenses/BSD-2-Clause)
#

import glob, os, sys
import re
import math
import yaml

from grdx.exam import Exam
from grdx.parser import Parser
from grdx.grades import Grades
from grdx.app import App

# PROJECT_ROOT = abspath()
sys.path.insert(0,os.path.dirname(__file__))

#
# entry point
#
if __name__ == "__main__":
    # load configuration
    config = yaml.safe_load(open("config/config.yml"))

    backend = App(config)
    backend.update_grades()

    for arg in sys.argv:
        if arg == '--config':
            print('grdx-cli ',config['path'])
            print('grdx-cli ',config['tasks'])
            print('grdx-cli ',config['bonus'])

        if arg == '--json':
            print(backend.json())

        if arg == '--csv':
            print(backend.csv())

        if arg == '--stats':
            print(backend.histogram())
