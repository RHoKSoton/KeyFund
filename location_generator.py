#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import glob
import csv

from mapnik2 import Projection, Coord

"""
To read in postcode data, extract the postcodes and Easting/Northing Data

We require columns 0, 2 and 3 from OS Code-Point(R) Open Data Files 
downloaded from  
http://parlvid.mysociety.org:81/os/

The OS-OpenData License is available from the following url:
http://www.ordnancesurvey.co.uk/oswebsite/docs/licences/os-opendata-licence.pdf

Contains Ordnance Survey data (c) Crown copyright and database right 2012
Contains Royal Mail data (c) Royal Mail copyright and database right 2012  
#Contains National Statistics data (c) Crown copyright and database right 2012 

Output will be 

post code, Easting, Northing, latitude, longitude
Note. Location coordinates are given in OSGB(E/N)
While latitude (+ve North) and longitude (+ve East) are quoted in that order
(WGS84 lat/long).

Note: The lat/long values calculated with mapnik2 do not exactly correspond with 
those from other sources (e.g. Google Maps, mapit.mysociety.org).
TODO: look into this.

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
        output.write(",".join(k) + '\n')
        #output.write(k[0] + ',' + k[1] + ',' + k[2] + + k[3] + + k[4] '\n')
    output.close()


def processCSV(filename, table_list):
    f = open(filename)
    for line in csv.reader(f):
        temp = []
        c = convert_loc(line)
        temp.append(line[0])
        temp.append(line[2])     # Easting 
        temp.append(line[3])     # Northing
        temp.append(str(c.y))           # Lat.
        temp.append(str(c.x))           # Long.
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

    






