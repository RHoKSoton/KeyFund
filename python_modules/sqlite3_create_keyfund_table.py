#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
    dbFilename = sys.argv[1]

except IndexError:

    print "\nExpected usage:"
    print sys.argv[0], "filename.db\n"
    sys.exit(1)

con = lite.connect(dbFilename)

with con:

    cur = con.cursor()

    cur.execute(
        """
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
    )

