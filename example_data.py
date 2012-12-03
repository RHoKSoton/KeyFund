import sys
import os
import csv

def write_data(lat, longt):
    lat_label = '"lat"'+':'+ '"'+ lat +'",'
    longt_label = '"long"'+':'+ '"'+ longt +'",'
    f = open('outfile.dat', 'a')
    f.write('\n')
    f.write('},{')
    f.write('"GroupProjectID": "0002"',)
    f.write('"Gender": "0",')
    f.write(lat_label),
    f.write(longt_label)
    f.write('},{')

def processCSV(filename):
    f = open(filename)
    for line in csv.reader(f):
        lat = line[1]
        longt = line[2]
        write_data(lat,longt)

filename = sys.argv[1]
processCSV(filename)



"""
class Data:
    datas = [{
             "GroupProjectID": "0001",
             "GroupProjectMemberID": "10001",
             "GROUPID": "200",
             "KeyFundStage": "1",
             "Gender": "1",
             "Postcode": "SO17 2HQ",
             "lat" : "51.9241468414",
             "long" : "-1939086340051"
    }, {
        "GroupProjectID": "0002",
        "GroupProjectMemberID": "10001",
        "GROUPID": "201",
        "KeyFundStage": "3",
        "Gender": "0",
        "Postcode": "SO17 2LB",
        "lat" : "50.9241468414",
        "long" : "-1.39086340051"
    }, {
        "GroupProjectID": "0003",
        "GroupProjectMemberID": "10001",
        "GROUPID": "202",
        "KeyFundStage": "4",
        "Gender": "1",
        "Postcode": "SO15 2DB",
        "lat" : "49.9241468414",
        "long" : "-0.39086340051"
    }]

sys.argv 

"""
