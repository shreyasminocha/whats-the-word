import Clustering
import numpy as np
import csv

with open('test-class2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    rowcount = 0
    for row in csv_reader:
        if rowcount < 10:
            print(float(row))
        rowcount += 1
    print(f'Processed {rowcount} lines.')
    print()
