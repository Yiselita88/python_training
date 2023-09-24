# Standar input and output objects
infile = open('budget.csv', 'r')
import csv
table = []
for row in csv.reader(infile):
    table.append(row)
infile.close()

# using list comprehension to write de same
infile2 = open('budget.csv', 'r')
import csv
table2 = [row for row in csv.reader(infile2)]


import pprint
pprint.pprint(table2)

# converting numbers into float

for r in range(1, len(table2)):
    for c in range(1, len(table2[0])):
        table2[r][c] = float(table2[r][c])

pprint.pprint(table2)

# processing data
row = [0.0] * len(table2[0])
row[0] = 'sum'
for c in range(1, len(row)):
    s = 0
    for r in range(1, len(table2)):
        s += table2[r][c]
    row[c] = s

outfile = open('budget2.csv', 'w')
writer = csv.writer(outfile)
for row in table2:
    writer.writerow(row)
outfile.close()
