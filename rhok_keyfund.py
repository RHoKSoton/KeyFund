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

#def extract_location(filename, location_dict):
#    """Return {nexy: [(latt, longt),]"""
#    f = open(filename)
#    for line in csv.reader(f):
#        if line[0][0] == 'G':
#            pass
#        else:
#            temp = []
#            lead_block = line[0][:-3].strip().lower()
#            latt = line[1]
#            longt = line[2]
#            coord = (latt, longt)
#            if location_dict.has_key(lead_block):
#                location_dict[lead_block].append(coord)
#            else:
#                location_dict[lead_block] = [coord]


def count_list_dict_item(in_list_dict, item):
    """Return frequency of key"""
    hist = {}
    for i in in_list_dict:
        key = i.get(item)
        hist[key] = hist.get(key, 0) + 1
    return hist

#def add_lat_longt(dict_field,latt,longt):
#    dict_field['latt'] = latt
#    dict_field['longt'] = longt

#def location_add(filename, in_list_dict, item, location_dict):
#    """Add Longitude and Latitude data and return updated list_dictionary
    
#location dict"""
#    for i in in_list_dict:
#        postcode = i.get(item)
#        lead_block = postcode[:-3].strip()
#        file_prefix = lead_block[:2].lower()
#        if location_dict.has_key(file_prefix):
#            add_lat_long(i, location_dict[file_prefix][0][0],
#                         location_dict[file_prefix][0][1])
#        else:
#            extract_location(filename,location_dict)
#            print(location_dict)
#            #add_lat_longt(i, location_dict[file_prefix][0][0],
#             #            location_dict[file_prefix][0][1])



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
    """Reads in the program-generated list of records and returns prompt int"""
    print("The records are as follows:\n")
    for x, y in record_list:
        n = 4 - len(str(x))
        print(x,n*'.', y)
    query_number = raw_input('\nPlease enter Query Number (0 or Q to quit): ')
    if query_number == 'q' or query_number =='Q' or query_number == '0':
        exit()
    else:
        try:
            query_number = int(query_number)
            if query_number in range(len(record_list)):
                return query_number
            else:
                program_prompt(record_list)
        except ValueError:
            program_prompt(record_list)

def question(fields):
    question = raw_input("\nTry again (Y, n, q)?: ")
    if question.lower() == 'y':
        program_prompt(fields)
    else:
        exit()

def plot_question(output_hist, query_number, fields):
    question = raw_input("\nWould you like to plot a histogram (Y, n, q)?: ")
    if question.lower() == 'y':
        rhok_hist_plot.plot_hist(output_hist, fields[query_number], 'Frequency')
    elif question.lower() == 'n':
        print(output_hist)
    else:
        exit()
    
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
    new_dict = {}
    location_add(filename, my_list,fields_dict.get(5),new_dict)

    #print(fields_dict)

    #print('No. records: ', len(my_list))

    #for i in my_list:
    #    print('No. Key-Value pairs: ', len(i))
    #    print(')
    #for k  in enumerate(my_list[1].keys()):
    #    print(k,)


    #plot_age = rhok_hist_plot.get_data(age_freq)

    #rhok_hist_plot.plot_hist(age_freq, fields_dict[11], 'Frequency')
    #print(key_values_dict['ISMALE'])
    #gender_test = is_male(my_list,fields_dict[key_values_dict['ISMALE']])
    #gender_test = count_list_dict_item(my_list, fields_dict[7])
    #print(gender_test)
    """
    query_number = program_prompt(fields)
    if fields_dict.get(query_number) == 'ISMALE':
        output_hist = is_male(my_list,fields_dict[key_values_dict['ISMALE']])
    else: 
        if fields_dict.get(query_number) != None:
            output_hist = count_list_dict_item(my_list,fields_dict[query_number])
    plot_question(output_hist, query_number, fields)
    print(output_hist)
    """

    
    


if __name__ == '__main__':
    main()
