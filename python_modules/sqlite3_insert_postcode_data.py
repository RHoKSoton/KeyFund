#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import glob
import csv
import sqlite3 as lite

"""
set textwidth=79
This module reads in postcode location data from data from dat files that
comprise the following columns:

postcode, easting, northing, latitude, longitude

e.g.
RG1 1AF,471712,173672,51.4569905029,-0.96773525291

Some entries may not have a space in the post code: 

RG270AA,468095,158215,51.3184577181,-1.02275724123
RG279ZZ,472784,153937,51.2794121113,-0.956348909928

The data is to be placed in an SQLite table, created as follows:

create table postcode_location_data
(
    location_id INT AUTOINCREMENT PRIMARY KEY,
    postcode_blk1 TEXT,
    postcode_blk2 TEXT,
    easting INT,
    northing INT,
    latitude REAL,
    longitude REAL
);
"""

# first we need to read in the file
def dbInsertCSV(filename,dbCursor):
    f = open(filename)
    for line in csv.reader(f):
        postcode = line[0]
        postcode_blk1 = postcode[:-3].strip(' ')
        postcode_blk2 = postcode[-3:]
        easting = line[1]
        northing = line[2]
        latitude = line[3]
        longitude = line[4]
        #print postcode_blk1, postcode_blk2, easting, northing, latitude, \
        #        longitude
        dbCursor.execute(
            """INSERT INTO postcode_location_data (
                postcode_blk1, postcode_blk2, easting,
                northing, latitude, longitude)
            VALUES
            (?, ?, ?, ?, ?, ?)""",
            (postcode_blk1, postcode_blk2, easting, northing, latitude,
             longitude)
        )

def usage_message():
    print "\n\nExpected usage:\n"
    print sys.argv[0], "database_file.db datafile.dat"
    print "\n\t or"
    print sys.argv[0], "database_file.db *.dat"


def main():

    try:

        dbFilename = sys.argv[1]
        filenames = sys.argv[2:]
    except IndexError:
        usage_message()
        sys.exit(1)

    try:
        con = lite.connect(dbFilename)
        dbCursor = con.cursor()

        for filename in filenames:
            print "Current file:", filename
            dbInsertCSV(filename,dbCursor)

        con.commit()

    except lite.Error, e:

        if con:
            con.rollback()
        
        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:

        if con:
            con.close()


if __name__ == "__main__":
    main()


