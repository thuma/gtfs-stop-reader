import csv
import re
#with open('sweden/trips.txt', 'r') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print row

trips = {}
with open('sweden/trips.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        trips[row[2]] = re.sub('_|[0-9]', '', row[0])

stops = {}
types = {}
with open('sweden/stop_times.txt', 'r') as f:
    reader = csv.reader(f) 
    for row in reader:
	try:
		if not row[3] in stops:
			stops[row[3]] = {}
			stops[row[3]]['id'] = row[3]
		stops[row[3]][trips[row[0]]] = 1
		types[trips[row[0]]] = trips[row[0]]
	except:
		print 'Hoppar rubrikrader'

f = open('travelmodes.csv','w')

f.write('ID')
for typ in types:
	 f.write(',' + typ)
f.write('\n')

for row in stops:
	f.write(row)
	for typ in types:
		if typ in stops[row]:
			f.write(',1')
		else:
			f.write(',0')
	f.write('\n')
f.close()

