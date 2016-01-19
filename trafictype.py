import csv
import re

trips = {}
ftrips = {}

# Load all trips to hash
with open('../sweden/trips.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0] == 'route_id':
            trips[row[2]] = row

# Load all routes to hach
route = {}
with open('../sweden/routes.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0] == 'route_id':
            route[row[0]] = row

# Map all trimes -> trip -> route and add type to new data
stops = {}
types = {}
with open('../sweden/stop_times.txt', 'r') as f:
    reader = csv.reader(f) 
    for row in reader:
        if not row[0] == 'trip_id':
            if not row[3] in stops:
                stops[row[3]] = {}
                stops[row[3]]['id'] = row[3]

            thisroute = route[trips[row[0]][0]]
            stops[row[3]]['agency_'+thisroute[1]] = 1
            stops[row[3]]['type_'+thisroute[4]] = 1
            types['agency_'+thisroute[1]] = 'agency_'+thisroute[1]
            types['type_'+thisroute[4]] = 'type_'+thisroute[4]

# Make new file.
f = open('travelmodes.csv','w')

# Write to file:
f.write('ID')
for typ in sorted(types.iterkeys()):
     f.write(',' + typ)
f.write('\n')

for row in stops:
    f.write(row)
    for typ in sorted(types.iterkeys()):
        if typ in stops[row]:
            f.write(',1')
        else:
            f.write(',')
    f.write('\n')
f.close()

