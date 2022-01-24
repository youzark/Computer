#!/usr/bin/env python
import csv

with open("name.csv", "r") as name_file:
    csvreader = csv.reader(name_file)
    for line in csvreader:
        print(line)
    with open("new_name.csv","w") as new_file:
        csv_writer = csv.writer(new_file,delimiter='|')
        # next(csvreader)   # get ride of the first line
        for line in csvreader:
            csv_writer.writerow(line[0:2])

with open("name.csv", "r") as name_file:
    csvreader = csv.DictReader(name_file)
    for line in csvreader:
        print(line)
    with open("last_name.csv", "w") as new_file:
        fieldnames = ["first_name", "last_name","email"]
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter="|")
        csv_writer.writeheader()
        for line in csvreader:
            csv_writer.writerow(line)

