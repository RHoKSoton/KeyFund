#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import random

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

def pick_random_coordinates(rows, required_number):
    if required_number == 1:
        random_index = [0]
    else:
        number_rows = len(rows)
        random_index = []
        while required_number > 0:
            random_index.append(random.randrange(number_rows))
            required_number -= 1
    coordinate_list = []
    for i in random_index:
        coordinate_list.append(rows[i])
    return coordinate_list

def find_coordinates(dbCursor, 
                     postcode_blk1, postcode_blk2=' '):
    if postcode_blk2 == ' ':
        cmd = """select * from postcode_location_data
              where postcode_blk1 = '%s'
              """ % postcode_blk1
    else:
        cmd = """select * from postcode_location_data
              where postcode_blk1 = '%s'
              and postcode_blk2 LIKE '%s'""" % (postcode_blk1, 
                                                postcode_blk2 + '%') 
    dbCursor.execute(cmd)
    return dbCursor.fetchall()

def count_people(dbCursor, postcode_blk1, postcode_blk2=' '):
    """Return the number of people with corresponding postcode fragments"""
    cmd = """select count(*) from rhok_keyfund_data
          where postcode_blk1 = '%s'
          and postcode_blk2 like '%s'
          """ % (postcode_blk1, postcode_blk2 + '%')
    dbCursor.execute(cmd)
    return dbCursor.fetchone()[0]


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

    try:
        con = lite.connect(dbFilename)
        con2 = lite.connect(dbFilename)
        cur = con.cursor()
        cur2 = con2.cursor()
        con_pc = lite.connect('postcode_data.db')
        cur_pc = con_pc.cursor()

        ## Program logic
        
        #cur.execute("""ATTACH 'postcode_data.db' AS postcodes;""")

        cur.execute("""SELECT person_id, postcode_blk1, postcode_blk2  
                     FROM rhok_keyfund_data;""")

    
        while True:
            row = cur.fetchone()
            if row == None:
                break
            #if row[2] == ' ':
            #    print "None"
            else:
                print row
                coordinate_rows = find_coordinates(cur_pc,row[1],row[2])
                required_number = count_people(cur2,row[1],row[2])
                print required_number 
                coordinate_list = pick_random_coordinates(coordinate_rows,
                                                       required_number)
                print coordinate_list 


    except lite.Error, e:
        if con:
            con.rollback()

        print "Error %s: " % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()

if __name__=='__main__':
    main()
