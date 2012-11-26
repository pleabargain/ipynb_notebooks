#this works
import csv
with open('/home/dennis/Desktop/tst.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)
