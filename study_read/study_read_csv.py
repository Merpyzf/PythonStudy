import csv

with open("test.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    reader
    print type(reader)
    for row in reader:
        print type(row)

