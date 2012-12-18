#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import glob
import csv
import MySQLdb

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

The data is to be placed in a MySQL table, created as follows:

create table postcode_location_data
(
    location_id int not null auto_increment primary key,
    postcode_blk1 varchar(4) not null,
    postcode_blk2 varchar(3) not null,
    easting int(10),
    northing int(10),
    latitude dec(14,11),
    longitude dec(14,11)
)engine=InnoDB;

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
            (%s, %s, %s, %s, %s, %s)""",
            (postcode_blk1, postcode_blk2, easting, northing, latitude,
             longitude)
        )

def main():
    db = MySQLdb.connect(user = "user1", host = "localhost",
                         passwd = "WhEg2012",
                         db = "postcode_coords")
    c = db.cursor()

    filenames = sys.argv[1:]

    for filename in filenames:
        print "Current file:", filename
        dbInsertCSV(filename,c)

    db.commit()

if __name__ == "__main__":
    main()


