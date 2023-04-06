# nested lists
Cdegrees = range(-20, 41, 5)
Fdegrees = [(9.0 / 5) * C + 32 for C in Cdegrees]
table = [Cdegrees, Fdegrees]
print(table)
table2 = []
for C, F in zip(Cdegrees, Fdegrees):
    table2.append([C, F])
print(table2)  # print the pairwise
# the whole code can be printed as list comprehension:
table3 = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]
print(table3)  # tables 2 & 3 are the same
# to access elements of the table:
print(table3[1])
print(table3[1][0])
print(table3[1][1])
import pprint
print(pprint.pprint(table3))  # print table in columns
print('----------------')
# using the old way of printing columns with formatting
for C, F in table3:
    print('%5d %5.1f' % (C, F))

#sublist or slices
print(table3[2:9])
print(table3[8:-1])  # print from index 8 to the end of the table
print('--------------------')

# to extract sublist or subtables at a given element range, in this case, the range is given by element C
for C, F in table3[Cdegrees.index(10):Cdegrees.index(35)]:
    print('%5d %5.1f' % (C, F))
print('--------------------')

# to extract sublist or subtable at given indices range
for C, F in table3[7:-1]:
    print('%5d %5.1f' % (C, F))
