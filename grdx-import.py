#!/usr/bin/env python3

import os
import argparse
import fnmatch
import re
import json
import csv

def parse_identfile_data(line,use_separator=','):
    # muster:333333:I17 Muster Hans Peter:IP209:A:1
    fs = line.split(':') # first split
    # print(fs[1],fs[4].split(' ')[0],fs[4].split(' ')[1])
    s_id = fs[1]
    s_group = fs[4].split(' ')[0]
    s_name = fs[4].split(' ')[1]
    s_year = re.search(r'\d+',s_group)[0]
    s_group = s_group.replace(s_year,'')

    return { 'id':int(s_id), 'name':s_name, 'year':int(s_year), 'group':s_group } 

def parse_pointfile_data(self,line,use_separator=','):
    return list(map(float,line.split(use_separator)))

def scan_metafiles(dirname):
    data = []
    for root, dirnames, filenames in os.walk(dirname):
        for filename in fnmatch.filter(filenames, 'IDENT.TXT'):
            ident_file = os.path.join(root, filename)
#            point_file = os.path.join(root, 'POINT.TXT')
            # student = None
            # fetch identity
            with open(ident_file) as f:
                for line in f:
                    item = parse_identfile_data(line)
                    item['root'] = root
                data.append(item)

        #     with open(point_file) as f:
        #         for line in f:
        #             student['points'] = self.parse_pointfile_data(line)
        # except Exception as e:


    return data

    # def json(self):
    #     r = []
    #     for s in self.students:
    #         r.append(s.json())
    #     return r


def generate_csv_output(data):
    for item in data:
        line = ''
        print(item.__class__)
        line = str(item.values())    
        print(line)
    

def main():
    parser = argparse.ArgumentParser(description='GRDX importer')
    parser.add_argument("--input", default="",
                        help="path to traverse for input")

    args = parser.parse_args()

    r = scan_metafiles(args.input)

    generate_csv_output(r)


if __name__ == '__main__':
    main()