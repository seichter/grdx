#!/usr/bin/env python3

import os
import argparse
import fnmatch
import re
import json

class IDENT_Import:
    """importer for PC test"""
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

        return { 'id':int(s_id), 'name':s_name, 'year':int(s_year), 'group':s_group } 

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
                    students.append(student)

            #     with open(point_file) as f:
            #         for line in f:
            #             student['points'] = self.parse_pointfile_data(line)
            # except Exception as e:


        return students

    # def json(self):
    #     r = []
    #     for s in self.students:
    #         r.append(s.json())
    #     return r

    # def csv(self):
    #     r = ''
    #     for s in self.students:
    #         r = r + s.csv() + '\n'
    #     return r



def main():
    parser = argparse.ArgumentParser(description='GRDX importer')
    parser.add_argument("--input", default="",
                        help="path to traverse for input")

    args = parser.parse_args()

    print(args.input)

    i = IDENT_Import()

    r = i.scan(args.input)

    print(r)


if __name__ == '__main__':
    main()