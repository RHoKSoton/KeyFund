#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import glob
import csv

from mapnik2 import Projection, Coord

"""
To read in postcode data, extract the postcodes and Easting/Northing Data

We require columns 0, 2 and 3.

Output will be 

postcode    coord1 coord2

"""

def translateName(inputName, fileSuffix):
	newName = os.path.splitext(inputName) # returns tuple ('name','.ext')
	return newName[0] + fileSuffix	# slice tuple & add suffix

def convert_loc(line):
    britishProj = Projection('+init=epsg:27700') # British National Grid

    c = Coord(float(line[2]), float(line[3]))
    c = britishProj.inverse(c)  ## Coord now in Lat/Lng
    return c

def writeData(outfilename, mos_data):
    output = open(outfilename, 'wt')
    for k in mos_data:
        output.write(k[0] + ',' + k[1] + ',' + k[2] + '\n')
    output.close()


def processCSV(filename, table_list):
    f = open(filename)
    for line in csv.reader(f):
        temp = []
        c = convert_loc(line)
        temp.append(line[0])
        temp.append(str(c.y))
        temp.append(str(c.x))
        table_list.append(temp)



sys.argv = [item for arg in sys.argv for item in glob.glob(arg)]

filenames = sys.argv[1:]

for filename in filenames:
    table_list = []
    processCSV(filename, table_list)
    outputName = translateName(filename, '.dat')
    writeData(outputName, table_list)
    #print(table_list)
    #csv.writer(open(outputName, 'w').writerows(table_list)

    






