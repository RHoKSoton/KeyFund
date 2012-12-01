#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function

import os
import sys
import csv


"""First lets read in some data, the fields are as follows:
(0, 'GROUPMEMBERID')
(1, 'GROUPPROJECTID')
(2, 'SUM_TYPO3')
(3, 'SUM_TYPO2')
(4, 'SUM_TYPO1')
(5, 'POSTALSECTOR')
(6, 'OLD_KEYFUNSTAGE')
(7, 'ISMALE')
(8, 'GROUPPROJECTMEMBERSKILLWHEELID')
(9, 'approxtime')
(10, 'GROUPPROJECTMEMBERID')
(11, 'approx_age')
(12, 'DISABILITYREF')
(13, 'Facilitator_Type')
(14, 'TIMESTAMP')
(15, 'ETHNICITYREF')
(16, 'NEW_KEYFUNSTAGE')
(17, 'TYPENAME')
(18, 'ISBEFORE')
(19, 'time_diff')
(20, 'DOB')
"""

def listBigFile(filename, my_list):
    """The function reads in line-by-line to allow for large files."""
    
    fcsv = open(filename, 'r')
    for line in csv.DictReader(fcsv):
        d = dict(line)
        my_list.append(d)

def count_list_dict_item(in_list_dict, item):
    """Return frequency of key"""
    hist = {}
    for i in in_list_dict:
        key = i[item]
        #print(key)
        hist[key] = hist.get(key, 0) + 1
    return hist

def main():
    try:
        filename = sys.argv[1]
    except:
        print('\nNo input file provided:\n' +
              'Usage: python %s filename\n' % sys.argv[0])
        exit()

    my_list = []
    fields = []
    listBigFile(filename, my_list)
    for k in enumerate(my_list[1].keys()):
        fields.append(k)
    fields_dict = dict(fields)
    #print(fields_dict)

    #print('No. records: ', len(my_list))

    #for i in my_list:
    #    print('No. Key-Value pairs: ', len(i))
    #    print(')
    #for k  in enumerate(my_list[1].keys()):
    #    print(k,)

    #print(fields_dict[11])
    age_freq = count_list_dict_item(my_list, fields_dict[11])
    print(age_freq)




if __name__ == '__main__':
    main()
