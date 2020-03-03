from pprint import pprint
import csv
with open("test2.csv") as f:
    reader = csv.DictReader(f)

    for row in reader:
        pprint(row)