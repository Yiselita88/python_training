# C = [-6, -3, 0, 3, 6, 12]
# C.append(15)
# C = C + [18, 21]
# C.insert(5, 9)
# C.insert(-2, 18)
# del(C[-3])
# print(C)
# print(len(C))
# print(C.index(12))

# Cdegrees = C
# print(Cdegrees)
# for C in Cdegrees:
#     print('list element:', C)
# print('the list has', len(Cdegrees), 'elements')

# for C in Cdegrees:
#     F = (9 / 5) * C + 32
#     print('%5.0f %5.1f' % (C, F))
# print('-------------------------')

# print(Cdegrees)
# index = 0
# while index < len(Cdegrees):
#     C = Cdegrees[index]
#     P = 2 * 3.14 * C
#     print('%5.0f %5.2f' % (C, P))
#     index += 1

# Cdegrees = Cdegrees + [24, 27]
# print(Cdegrees)
# print(len(Cdegrees))
# Area = []
# for C in Cdegrees:
#     A = 2 * C ** 2
#     Area.append(A)
# print(Area)

Radio = range(-6, 27, 3)
Area = [0.0] * len(Radio)
for i in range(len(Area)):
    Area[i] = 3.14 * Radio[i] ** 2
    print('%5.0f %5.1f' % (Radio[i], Area[i]))
print(len(Area))
Area.append(2000)
print(Area)

step = 0.7
start = -7
n = 21
list1 = [0.0] * n
list2 = [0.0] * n
for i in range(n):
    list1[i] = start + i * step
    list2[i] = 3.14 * list1[i] ** 2 + 200
    print('%5.1f %5.2f' % (list1[i], list2[i]))

print(list1)
print(list2)

for e in list1:
    e += 5
print(list1)

for i in range(len(list1)):
    list1[i] += 5
print(list1)

# same as before
for i in range(n):
    list1[i] += 5
print(list1)

for i, e in enumerate(list2):
    list2[i] = e + 5
print(list2)

m = 10
list3 = [-5 + i * 0.5 for i in range(m)]
print(list3)

triangle = [0.0] * len(list3)
for i in range(len(list3)):
    triangle[i] = (1 / 2) * list3[i] ** 2
    print(list3[i], triangle[i])

# chpater 2
print('----------------')
C = -20
dC = 5
while C <= 40:
    F = 9 / 5 * C + 32
    print(C, F)
    C += dC
print('----------------')

# lists
C = [20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
print(C)
C.append(35)
C = C + [40, 45]
C.insert(3, -7.5)
print(C)
del(C[3])
print(C)
print(len(C))
print(C.index(25))  # find index for element 10
print(10 in C)
print(18 in C)
print(C[-1])
animals = ['abeja', 'burro', 'caballo']
ab, bu, ca = animals
print(ab)
print(bu)
print(ca)
print(animals[-1])
print(animals[-2])
print(type(animals))
print(type(animals[-2]))

# for loops
degrees = [0, 10, 20, 40, 100]
for C in degrees:
    print('list element:', C)
print('the degrees list has', len(degrees), 'elements')

Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
for C in Cdegrees:
    F = 9 / 5 * C + 32
    print('%5d %5.1f' % (C, F))

# while loop
Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
index = 0
print('   C     F')
while index < len(Cdegrees):
    C = Cdegrees[index]
    F = 9 / 5 * C + 32
    print('%5d %5.1f' % (C, F))
    index += 1

# storing the table column as a list

Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
Cdegrees.insert(0, -25)
Cdegrees = Cdegrees + [45, 50]
del Cdegrees[-1]
Fdegrees = []
for C in Cdegrees:
    F = 9 / 5 * C + 32
    print('%5d %5.1f' % (C, F))
    Fdegrees.append(F)
print(Cdegrees)
print(Fdegrees)
print(len(Cdegrees))
print(Cdegrees.index(10))
print(Cdegrees.index(35))
print(40 in Cdegrees)
print(42 in Cdegrees)

# assigning a sequence of variables to a list
archives = ['excel.xslx', 'adobe.pdf', 'powerpoint.ppt']
calculus, docusign, presentation = archives
print(presentation)
print(docusign)


# while loop implementation of for loop
radii = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(radii))
i = 0
while i < len(radii):
    R = radii[i]
    V = (R ** 3) / 2
    print('%5d %5.1f' % (R, V))
    i += 1

# create lists from columns
radii = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
area = []
for R in radii:
    A = (R ** 2) / 2
    area.append(A)
    print(R, A)
print(area)
print(len(radii))

# generate a list from scratch, its values with range function
from math import pi
radius = range(0, 55, 5)
print(len(radius))
sphere = [0.0] * len(radius)
print(sphere)
for i in range(len(radius)):
    sphere[i] = 4 / 3 * pi * radius[i] ** 3
print(sphere)

from math import pi
step = 0.7
start = -0.7
length = 11
perimeter = [0.0] * length
size = [0.0] * length
for i in range(length):
    perimeter[i] = start + i * step
    size[i] = perimeter[i]**2 / 4 * pi
print(perimeter)
print(size)

C_start = -5
C_step = 0.5
C_stop = 20
C = C_start
Cdegrees = []
Fdegrees = []
while C <= C_stop:
    Cdegrees.append(C)
    F = 9 / 5 * C + 32
    Fdegrees.append(F)
    C = C + C_step
print(Cdegrees, Fdegrees)
