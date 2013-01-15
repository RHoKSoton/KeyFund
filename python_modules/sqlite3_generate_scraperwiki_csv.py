#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import csv

"""
The classic version of Scraperwiki does not allow direct upload of local data.
We can, however, upload a csv file to Dropbox, and use the file url to import
the data into the Scraper SQLite database.

For the initial attempt, we use the following query to extract the most useful
fields from the current sqlite3 database:

select 
rd.person_id,
rd.groupprojectid,
rd.groupmemberid, 
rd.groupprojectmemberskillwheelid,
rd.facilitator_type,
rd.approxtime,
rd.ismale, 
rd.dob,
rd.ethnicityref,
rd.disabilityref,
rd.approx_age,
al.latitude, 
al.longitude 
from rhok_keyfund_data as rd 
inner join allocated_location as al 
on rd.person_id==al.person_id limit 10;

We then write this data to a csv file. 

"""

def usage_msg():
    print "\n\nExpected usage:\n"
    print sys.argv[0], " databasefile.db"
    print "\n"

def appendWriteData(outfilename, row):
    output = open(outfilename, 'at')
    my_list = []
    for k in row:
        my_list.append(str(k))
    output.write(",".join(my_list) + '\n')
    output.close()


def main():

    try:
        dbFilename = sys.argv[1]
    except IndexError:
        usage_msg()
        sys.exit(1)

    con = lite.connect(dbFilename)
    cur = con.cursor()

    cur.execute("""
    select 
    rd.person_id,
    rd.groupprojectid,
    rd.groupmemberid, 
    rd.groupprojectmemberskillwheelid,
    rd.facilitator_type,
    rd.approxtime,
    rd.ismale, 
    rd.dob,
    rd.ethnicityref,
    rd.disabilityref,
    rd.approx_age,
    al.latitude, 
    al.longitude 
    from rhok_keyfund_data as rd 
    inner join allocated_location as al 
    on rd.person_id==al.person_id;
    """)
    
    processed_no = 0

    while True:
        row = cur.fetchone()
        if row == None:
            break
        else:
            appendWriteData("rhok_scraper_data.csv", row)
            processed_no += 1
            sys.stdout.write(
                "Processed records: %s \r" % processed_no)
            sys.stdout.flush()

    print "Processed records: %s" % (processed_no)
           


if __name__=='__main__':
    main()
