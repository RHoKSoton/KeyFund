#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

"""
This program's purpose is to read in person_id, postcode_blk1, and 
postcode_blk2 from an sqlite3 database. The postcodes are incomplete. A list of
E/N, lat/Long coordinates will be generated that are possible correlations with
the postcode fragment. One of these coordinate sets will be randomly assigned
to the person_id in a new table in the database.

We make a temporary dict structure to avoid duplicating the same sqlite
searches for each row with an identical postcode fragment:

    {'AB99 9':[(E,N,Lat., Long.), ...], ...}

We look up the list of possible coordinates for the person_id, generate a
random number to select one of those values, and enter it (together with the
person_id) into the allocated_location table.



"""

def usage_msg():
    print "\n\nExpected usage:\n"
    print sys.argv[0], " databasefile.db"
    print "\n"

def create_table(dbCursor):
    dbCursor.executescript(
    """
        DROP TABLE IF EXISTS allocated_location;
        CREATE TABLE allocated_location(
        person_id INTEGER,
        easting INTEGER,
        northing INTEGER,
        latitude REAL,
        longitude REAL);
    """
    )

def insert_data(dbCursor,param_tuple):
    dbCursor.execute(
        """INSERT INTO allocated_location (
        person_id, easting, northing, latitude, longitude)
        VALUES
        (?, ?, ?, ?, ?)
        """, param_tuple
    )

def dict_key(postcode_blk1, postcode_blk2):
    if postcode_blk2 == ' ':
        return postcode_blk1
    else:
        return ' '.join((postcode_blk1, postcode_blk2))






def main():

    try:
        dbFilename = sys.argv[1]
    except IndexError:
        usage_msg()
        sys.exit(1)

    con = lite.connect(dbFilename)
    cur = con.cursor()

    cur.execute("SELECT person_id, postcode_blk1, postcode_blk2 
                 FROM rhok_keyfund_data")

    while True:
        row = cur.fetchone()
        if row == None:
            break
        if row[2] == ' ':
            print "None"
        else:
            print row[2]

if __name__=='__main__':
    main()
