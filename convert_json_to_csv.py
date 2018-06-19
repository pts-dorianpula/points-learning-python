import json
import csv

with open('exercises/rn.json') as f:
    data = json.load(f)


with open('exercises/names.csv',  'w') as g:
    csv_writer = csv.DictWriter(g, ['firstname', 'lastname'])
    csv_writer.writeheader()
    for row in data:
        csv_writer.writerow(row)
