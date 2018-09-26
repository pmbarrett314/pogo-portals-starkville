#!/usr/bin/env python3

import json
import sys

def sort_json(filename):
    with open(filename,"r") as f:
        js=json.load(f)
    with open(filename,"w+") as f:
        json.dump(js,f,sort_keys=True,indent=1)

if __name__=="__main__":
    if len(sys.argv)<2:
        print("usage: sort_json.py [filename]\nsort a json file in place")
        exit(0)
    sort_json(sys.argv[1])
