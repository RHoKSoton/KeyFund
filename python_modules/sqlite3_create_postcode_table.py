#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
    dbFilename = sys.argv[1]

except IndexError:

    print "\n\nExpected usage:\n"
    print sys.argv[0], "filename.db\n\n"

con = lite.connect(dbFilename)

with con:

    cur = con.cursor()

    cur.execute(
        """
    create table postcode_location_data
    (
        location_id INTEGER PRIMARY KEY AUTOINCREMENT,
        postcode_blk1 TEXT,
        postcode_blk2 TEXT,
        easting INTEGER, 
        northing INTEGER,
        latitude REAL,
        longitude REAL
    );
        """
    )


