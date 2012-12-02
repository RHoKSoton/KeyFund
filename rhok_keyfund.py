#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function

import os
import sys
import csv
import rhok_hist_plot


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
        key = i.get(item)
        hist[key] = hist.get(key, 0) + 1
    return hist

def is_male(in_list_dict, item):
    temp_gender_hist = count_list_dict_item(in_list_dict,item)
    gender_hist = {}
    gender_hist['male'] = temp_gender_hist.get('1')
    gender_hist['female'] = temp_gender_hist.get('0')
    return gender_hist

def pmf(hist, my_list):
    """Takes hist from count_list_dict_item and data as input"""
    pmf_hist = {}
    n = float(len(my_list))
    for item, frequency in hist.items():
        pmf_hist[item] = frequency/n
    return pmf_hist

def program_prompt(record_list):
    """Reads in the program-generated list of records and asks for prompt"""
    print("The records are as follows:\n")
    for x, y in record_list:
        print(x, ':\t', y)


def main():
    try:
        filename = sys.argv[1]
    except:
        print('\nNo input file provided:\n' +
              'Usage: python %s filename\n' % sys.argv[0])
        exit()

    my_list = []
    fields = []
    value_fields = []
    listBigFile(filename, my_list)
    for k in enumerate(my_list[1].keys()):
        fields.append(k)
    for num, key_val in fields:
        value_fields.append((key_val, num))
    fields_dict = dict(fields)
    key_values_dict = dict(value_fields)
    #print(fields_dict)

    #print('No. records: ', len(my_list))

    #for i in my_list:
    #    print('No. Key-Value pairs: ', len(i))
    #    print(')
    #for k  in enumerate(my_list[1].keys()):
    #    print(k,)

    #print(fields_dict[11])
    age_freq = count_list_dict_item(my_list, fields_dict[11])
#    print(age_freq)

    age_pmf = pmf(age_freq, my_list)
#    print(age_pmf)

    #plot_age = rhok_hist_plot.get_data(age_freq)

    #rhok_hist_plot.plot_hist(age_freq, fields_dict[11], 'Frequency')
    #print(key_values_dict['ISMALE'])
    #gender_test = is_male(my_list,fields_dict[key_values_dict['ISMALE']])
    #gender_test = count_list_dict_item(my_list, fields_dict[7])
    #print(gender_test)



if __name__ == '__main__':
    main()
