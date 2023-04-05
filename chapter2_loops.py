# For loops
degrees = [0, 10, 20, 40, 100]
for C in degrees:
    print('list element:', C)
print('the degrees list has', len(degrees), 'elements')

# print tables with for loops using old formatting
Cdegrees = [-20, -15, -10, 0, 5, 10, 15, 20]
for C in Cdegrees:
    F = (9.0 / 5) * C + 32
    print('%5d %5.1f' % (C, F))


# Implementation of For loops as While loops
from math import pi
radii = [1, 3, 5, 7, 9, 11]
index = 0
print('    R     A')
while index < len(radii):
    R = radii[index]
    A = (1 / 2) * pi * R ** 2
    print('%5d %5.1f' % (R, A))
    index += 1

# storing table columns as a list
import numpy as np
x_axis = [1, 1.1, 1.2, 2, 2.2, 2.4, 3, 3.3, 3.6, 4, 4.4, 4.8]
y_axis = []  # start with an empty list
for X in x_axis:
    Y = 5 * np.exp(X)
    y_axis.append(Y)
    print('%5.1f %5.1f' % (X, Y))
print(x_axis)
print(y_axis)

# Loops with list indices
from math import pi
Perimeter = range(2, 20, 2)
Area = [0.0] * len(Perimeter)
for i in range(len(Perimeter)):
    Area[i] = Perimeter[i] ** 2 / (4 * pi)
    print('%5.0f %5.1f' % (Perimeter[i], Area[i]))
Area.append(Area)
print(Area)

# Loops over Real Numbers, growing lists
step = 0.4
start = 1
n = 17
jumps = [0.0] * n
distance = [0.0] * n
for i in range(n):
    jumps[i] = start + i * step
    distance[i] = np.sqrt(jumps[i]) ** 3 + 8
    # print table with column 1: jumps at a given indice i, and column 2: at their corresponding calculated distance
    print('%5.1f %5.1f' % (jumps[i], distance[i]))
# if you want to create an array with step = 0.4, start = 1, and lenght = 17
print(jumps)
# print the list corresponding to all the calculated distances.
print(distance)

# while loop with growing lists
C_start = -5
C_step = 0.5
C_stop = 20
C = C_start
Cdegrees = []
Fdegrees = []
while C <= C_stop:
    Cdegrees.append(C)
    F = (9.0 / 5) * C + 32
    Fdegrees.append(F)
    C = C + C_step
print(Cdegrees)
print(Fdegrees)

# Changing list
for i in range(len(Cdegrees)):
    Cdegrees[i] += 7
print(Cdegrees)

# transversing a list with indice and element for each loop pass
for i, c in enumerate(Cdegrees):
    Cdegrees[i] = c + 15
print(Cdegrees)

# List Comprehension
from math import pi
Radii = [2 + i * 0.7 for i in range(n)]
Areas = [pi * R ** 2 for R in Radii]
R_plus_4 = [R + 4 for R in Radii]
for i in range(len(Radii)):
    print('%5.1f %5.1f %5.1f' % (Radii[i], Areas[i], R_plus_4[i]))
# this can be also be written as follows and it's better to iterate over list elements (R, A, Q) than over list indices:
for R, A, Q in zip(Radii, Areas, R_plus_4):
    print('%5.1f %5.1f %5.1f' % (R, A, Q))
    print('-------------------')
print(Radii)
print(Areas)
print(R_plus_4)
