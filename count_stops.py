#!/usr/bin/env python3
import json
import pprint
import sys
import s2sphere


from collections import defaultdict, OrderedDict

class Cell():
    def __init__(self,cell_id, name):
        self.cell_id = cell_id
        self.name = name
    
    def __hash__(self):
        return hash(self.cell_id)

    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return self.cell_id == other.cell_id

def lat_lng_to_cell(lat, lng, level):
    latlng = s2sphere.LatLng.from_degrees(lat,lng)
    cell = s2sphere.Cell.from_lat_lng(latlng)
    cell_id = cell.id()
    return cell_id.parent(level)

def count_stops(filename):
    with open(filename,"r") as f:
        js = json.load(f)
    cells = defaultdict(int)

    for stop in js["gyms"].values():
        name = stop["name"]
        lat = stop["lat"]
        lng = stop["lng"]
        cell_id = lat_lng_to_cell(lat, lng, 14)
        cell = Cell(cell_id, name)
        cells[cell] += 1
    for stop in js["pokestops"].values():
        name = stop["name"]
        if "First John Missionary Baptist Church".lower() in name.lower():
            continue
        lat = stop["lat"]
        lng = stop["lng"]
        cell_id = lat_lng_to_cell(lat, lng, 14)
        cell = Cell(cell_id, name)
        cells[cell] += 1

    keys = sorted(cells,key=cells.get)
    d = OrderedDict({key:cells[key] for key in keys })
    pprint.pprint(d)


if __name__=="__main__":
    if len(sys.argv)<2:
        print("usage: count_stops.py [filename]\ncount stops")
        exit(0)
    count_stops(sys.argv[1])
