import csv
spamWriter = csv.writer(open('/home/dennis/Desktop/tst.csv', 'w', newline=''), delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamWriter.writerow(['Spam'] * 5 + ['Baked Beans'])
spamWriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
