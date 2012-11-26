#not python 3.2x?
import csv

counts = []
frequencies = []

for d in csv.DictReader(open('/home/dennis/Desktop/tst.csv'), delimiter='\t'):
    counts.append(int(d['Counts']))
    frequencies.append(int(d['frequency']))

print ('Counts = ', counts)
print ('frequency = ', frequencies)
