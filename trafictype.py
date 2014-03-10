import csv
import re
#with open('sweden/trips.txt', 'r') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print row
# https://api.trafiklab.se/samtrafiken/gtfs/sweden.zip?key=wItxkyLvncTsCYzXUwADmAIAvX4kWPES

trips = {}
ftrips = {}
with open('sweden/trips.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
	if not row[0] == 'route_id':
       		trips[row[2]] = re.sub('_|[0-9]', '', row[0])
		ftrips[row[2]] = row
route = {}
with open('sweden/routes.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
	if not row[0] == 'route_id':
        	route[row[0]] = row

stops = {}
types = {}
with open('sweden/stop_times.txt', 'r') as f:
    reader = csv.reader(f) 
    for row in reader:
	if not row[0] == 'trip_id':
		try:
			if not row[3] in stops:
				stops[row[3]] = {}
				stops[row[3]]['id'] = row[3]
			stops[row[3]][trips[row[0]]] = 1
			thisroute = route[ftrips[row[0]][0]]
			stops[row[3]]['op'+thisroute[1]] = 1
			stops[row[3]]['type'+thisroute[5]] = 1
			types['op'+thisroute[1]] = 'op'+thisroute[1]
			types['type'+thisroute[5]] = 'type'+thisroute[5]
			types[trips[row[0]]] = trips[row[0]]
		except:
			print 'Hoppar rubrikrader'

f = open('travelmodes.csv','w')

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
			f.write(',0')
	f.write('\n')
f.close()

