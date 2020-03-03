from pprint import pprint
import csv

with open("test4.csv") as f:
    reader = csv.DictReader(
        f,
        delimiter=";",
        fieldnames=[
            "my_col1",
            "my_col2",
            "my_col3"
        ]
    )

    for row in reader:
        print(row)

