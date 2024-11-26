import csv

with open("username.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)