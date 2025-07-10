import csv

file_path = 'csvOutput.csv'

with open(file_path, 'r') as file:
    content = csv.reader(file)
    for line in content:
        print(line[0:])