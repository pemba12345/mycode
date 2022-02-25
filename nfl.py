#!/usr/bin/env python3

#import the csv file
import csv


html_output = ''
names = []

#open the csv data 
with open("nflplayers.txt", "r") as sportfile:
    csv_reader = csv.DictReader(sportfile)
    
    next(csv_reader) #dont want first line of file

    for line in csv_reader:
        names.append(f"{line['name']} {line['college']}")


html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n<ul>'
print(html_output)



