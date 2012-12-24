#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

def usage_msg():
    print "\n\nExpected usage:\n"
    print sys.argv[0], " databasefile.db"
    print "\n"


def main():

    try:
        dbFilename = sys.argv[1]
    except IndexError:
        usage_msg()
        sys.exit(1)

    con = lite.connect(dbFilename)
    cur = con.cursor()

    cur.execute("SELECT person_id, postcode_blk1, postcode_blk2 FROM rhok_keyfund_data")

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
