#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import glob
import csv
import MySQLdb
import time

"""
set textwidth=79
This module reads in keyfund data from final_data_demographics.csv 

postcode, easting, northing, latitude, longitude

e.g.
RG1 1AF,471712,173672,51.4569905029,-0.96773525291

Some entries may not have a space in the post code: 

RG270AA,468095,158215,51.3184577181,-1.02275724123
RG279ZZ,472784,153937,51.2794121113,-0.956348909928

The data is to be placed in a MySQL table, created as follows:


create table rhok_demo_data
(
    person_id INT NOT NULL auto_increment primary key,
    groupprojectid INT,
    groupmemberid INT,
    groupprojectmemberskillwheelid INT,
    groupprojectmemberid INT,
    time_stamp DATE,        -- Feb 6 2012 1.55PM, we'll drop time
    isbefore INT(1),
    old_keyfunstage INT(1),
    new_keyfunstage INT(1),
    typename VARCHAR(30),
    sum_typo1 INT(3),
    sum_typo2 INT(3),
    sum_typo3 INT(3),
    facilitator_type VARCHAR(32),
    approxtime YEAR(4),            -- just the year
    time_diff INT(2),
    ismale INT(1),
    dob DATE,                   -- Dec 12 1991, also need to strip time
    ethnicityref INT(2),
    disabilityref INT(2),
    postcode_blk1 VARCHAR(4),
    postcode_blk2 VARCHAR(3),
    approx_age INT(3)
)engine=InnoDB;

The database is called rhok_keyfund_test

"""

# first we need to read in the file
def dbInsertCSV(filename,dbCursor):
    f = open(filename)
    for line in csv.reader(f):
        if line[0][0] == 'G':
            continue
        groupprojectid = line[0]
        groupmemberid = line[1]
        groupprojectmemberskillwheelid = line[2]
        groupprojectmemberid = line[3]
        j = time.strptime(line[4],"%b %d %Y %I:%M%p") 
        time_stamp = "%s-%s-%s" % (j.tm_year, j.tm_mon, j.tm_mday)
        isbefore = line[5]
        old_keyfunstage = line[6]
        new_keyfunstage = line[7]
        typename = line[8]
        sum_typo1 = line[9]
        sum_typo2 = line[10]
        sum_typo3 = line[11]
        facilitator_type = line[12]
        approxtime = line[13]
        time_diff = line[14]
        ismale = line[15]
        k = time.strptime(line[16],"%b %d %Y %I:%M%p") 
        dob = "%s-%s-%s" % (k.tm_year, k.tm_mon, k.tm_mday)
        ethnicityref = line[17]
        disabilityref = line[18]
        postcode = line[19]
        m = postcode.split()
        if len(m) == 0:
            postcode_blk1 = ' '
            postcode_blk2 = ' '
        elif len(m) == 1:
            postcode_blk1 = m[0]
            postcode_blk2 = ' '
        else:
            postcode_blk1 = m[0]
            postcode_blk2 = m[1]

        approx_age = line[20]

        #print line
        #postcode = line[0]
        #postcode_blk1 = postcode[:-3].strip(' ')
        #postcode_blk2 = postcode[-3:]

        dbCursor.execute(
            """INSERT INTO rhok_demo_data (
                groupprojectid,
                groupmemberid,
                groupprojectmemberskillwheelid,
                groupprojectmemberid,
                time_stamp,
                isbefore,
                old_keyfunstage,
                new_keyfunstage,
                typename,
                sum_typo1,
                sum_typo2,
                sum_typo3,
                facilitator_type,
                approxtime,
                time_diff,
                ismale,
                dob,
                ethnicityref,
                disabilityref,
                postcode_blk1,
                postcode_blk2,
                approx_age)
            VALUES
            (%s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, 
            %s, %s )""",
            (groupprojectid, groupmemberid, groupprojectmemberskillwheelid,
             groupprojectmemberid, time_stamp, isbefore, old_keyfunstage,
             new_keyfunstage, typename, sum_typo1, sum_typo2, sum_typo3,
             facilitator_type, approxtime, time_diff, ismale, dob,
             ethnicityref, disabilityref, postcode_blk1, postcode_blk2, approx_age)
        )

def main():
    db = MySQLdb.connect(user = "user1", host = "localhost",
                         passwd = "WhEg2012",
                         db = "rhok_keyfund_test")
    c = db.cursor()

    filenames = sys.argv[1:]

    for filename in filenames:
        print "Current file:", filename
        dbInsertCSV(filename,c)

    db.commit()

if __name__ == "__main__":
    main()


