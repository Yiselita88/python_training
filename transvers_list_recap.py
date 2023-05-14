# # this is a script to calculate the temperatures according to geometric progression given initial and third (T_2) temperatures
# the formulas for the calculating the constants of a geometric progression is:
import numpy as np
a = 269.5
T_2 = 300.0
r = np.sqrt(T_2 / a)
# a = (T_2 - T_0) / (((T_2 / T_0) ** 3) - 1)
print(r, a)
print('%5.1f %5.1f' % (r, a))
print('-----------')

# now that we have the constants, we'll calculate the temperatures corresponding to the geometric progression
s = 1  # step
start = 0
n = 16
k_values = [0.0] * n
Temp_k = [0.0] * n
for i in range(n):
    k_values[i] = start + i * s
    Temp_k[i] = a * r ** k_values[i]
    print('%5.1f' % (Temp_k[i]))
# print(Temp_k)
# print(len(Temp_k))

# # the former code is useful to calculate the needed temperatures for Replica Exchange Molecular Dynamics # #
# let's use these to recap the nested_list content with the ideal gas law
n = 2
V = 6.2
R = 8.314

Pressure = [(n * R * T) / V for T in Temp_k]
# print(Pressure)
table1 = [Temp_k, Pressure]
print(table1)

table2 = []
for T, P in zip(Temp_k, Pressure):
    table2.append([T, P])
print(table2)

table3 = [[T, P] for T, P in zip(Temp_k, Pressure)]
print(table3)

# notice tables 2 & 3 are equals, meaning there are different ways of having the same resuls. Here, we're having a list of [T, P] pairs.
# if we want to print them as a table with defined columns:
print('  T       P')
for T, P in table3:
    print('%5.1f   %5.1f' % (T, P))

# slicing the table
# This following script could yield some issues if some of the numbers are not in the list
print('----------------------')
for T, P in table3[Temp_k.index(269.5):Temp_k.index(300.0)]:
    print('%5.1f   %5.1f' % (T, P))

print('----------------------')
# the equivalence to the former is:
for T, P in table3[8:]:
    print('%5.1f   %5.1f' % (T, P))

# # transversion nested lists
scores = []
scores.append([12, 16, 11, 12])
scores.append([9])
scores.append([6, 9, 11, 14, 17, 15, 14, 20])
print(scores)
print(len(scores))
print(len(scores[0]), len(scores[1]), len(scores[2]))
print('-------------')
# p: are the players (rows), g: for games (columns)
for p in range(len(scores)):
    for g in range(len(scores[p])):
        score = scores[p][g]
        print('%4d' % (score))

print('---------------')

for player in scores:
    for game in player:
        print('%4d' % (game))

print('-------------')
# exercise 2.58:
n = 3
for i in range(-1, n):
    if i != 0:
        print(i)
print('-------------')
for i in range(1, 13, 2 * n):
    for j in range(n):
        print(i, j)
print('-------------')
for i in range(1, n + 1):
    for j in range(i):
        print(i, j)

print('-------------')
for i in range(1, n + 1):
    for j in range(i):
        if j:
            print(i, j)
print('-------------')
for i in range(2, 13, 2 * n):
    for j in range(0, i, 2):
        for k in range(2, j, 1):
            b = 1 > j > k
            if b:
                print(i, j, k)
