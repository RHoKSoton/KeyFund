#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import glob
import csv
import sqlite3 as lite
import time

"""
set textwidth=79
This module reads in keyfund data from final_data_demographics.csv 

It corrects postcodes entered in lower case, and attempts to 
accommodate for malformed postcode entries. 

Possible postcode formats are as follows:
    A9   9AA
    A9A  9AA (London)
    A99  9AA
    AA9  9AA
    AA9A 9AA (London)
    AA99 9AA

If postcodes are entered without a space, but we know they are complete, 
we can correct for lack of separation by slicing the last 3 characters.

Incomplete postcodes entered without a space are not adequately accommodated
at present. We need to be able to distinguish between AA9 9 and AA99. At
present we assume AA99. Invalid postcode fragments will be rejected by
the location allocation program.

Fragments that are valid and incorrect will present a source of error.

The data is to be placed in an SQLite table, created as follows:

        create table rhok_keyfund_data
    (
        person_id INTEGER NOT NULL primary key AUTOINCREMENT,
        groupprojectid INTEGER,
        groupmemberid INTEGER,
        groupprojectmemberskillwheelid INTEGER,
        groupprojectmemberid INTEGER,
        time_stamp TEXT,        -- Feb 6 2012 1.55PM, we'll drop time
        isbefore INTEGER,
        old_keyfunstage INTEGER,
        new_keyfunstage INTEGER,
        typename TEXT,
        sum_typo1 INTEGER,
        sum_typo2 INTEGER,
        sum_typo3 INTEGER,
        facilitator_type TEXT,
        approxtime TEXT,            -- just the year
        time_diff INTEGER,
        ismale INTEGER,
        dob TEXT,                   -- Dec 12 1991, also need to strip time
        ethnicityref INTEGER,
        disabilityref INTEGER,
        postcode_blk1 TEXT CHECK(length(postcode_blk1<=4)),
        postcode_blk2 TEXT CHECK(length(postcode_blk2<=3)),
        approx_age INTEGER
    );

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
        postcode = line[19].upper()
        m = postcode.split()
        if len(m) == 0:
            postcode_blk1 = ' '
            postcode_blk2 = ' '
        elif len(m) == 1:
            if len(m[0]) >= 6:
                postcode_blk1 = m[0][:-3]
                postcode_blk2 = m[0][-3:]
            elif len(m[0]) <= 4:
                postcode_blk1 = m[0]
                postcode_blk2 = ' '
            else:
                # consider alternatives, but postcodes can = 5 chars (+space)
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
            """INSERT INTO rhok_keyfund_data (
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
            (?,?,?,?,?,
             ?,?,?,?,?,
             ?,?,?,?,?,
             ?,?,?,?,?,
             ?,?
             )""",
            (groupprojectid, groupmemberid, groupprojectmemberskillwheelid,
             groupprojectmemberid, time_stamp, isbefore, old_keyfunstage,
             new_keyfunstage, typename, sum_typo1, sum_typo2, sum_typo3,
             facilitator_type, approxtime, time_diff, ismale, dob,
             ethnicityref, disabilityref, postcode_blk1, postcode_blk2, approx_age)
        )

def usage_message():
    print "\n\nExpected usage:\n"
    print sys.argv[0], "database_file.db datafile.csv"
    print "\n\t or"
    print sys.argv[0], "database_file.db *.csv"

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


