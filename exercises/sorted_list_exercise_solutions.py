import csv
import operator


with open('names.csv') as names_file:
    data = list(csv.DictReader(names_file))

# Sort by last name
sorted_by_last_name = sorted(data, key=operator.itemgetter('lastname'))
# Length
len(sorted_by_last_name)

# Divide into 3 groups by last name
# A-G (56) H-N (57-120),
