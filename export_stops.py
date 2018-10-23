#!/usr/bin/env python3

import csv
import json
import sys

def export_latlon(filename, outfilename):
    with open(filename,"r") as f:
        js=json.load(f)
    with open(outfilename,"w+") as f:
        writer=csv.writer(f)
        writer.writerow(["name","latlon"])
        for stop in js["pokestops"].values():
            name=stop["name"]
            latlon="{},{}".format(stop["lat"],stop["lng"])
            writer.writerow([name,latlon])
            

if __name__=="__main__":
    if len(sys.argv)<3:
        print("usage: export_stops.py [infilename] [outfilename]\ndump the stops")
        exit(0)
    export_latlon(sys.argv[1],sys.argv[2])
