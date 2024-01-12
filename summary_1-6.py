# # Chapter 1
# print('when the code is too long \n break it into several lines. \n For example, this print has \n 4 lines')
# t = 16
# w_0 = 166
# less = 2 * t
# w_f = w_0 - less
# print('cuando pierda %g libras despues de %g semanas, mi peso sera de %.2f kilogramos' %
#       (less, t, w_f / 2.2))
# print('actualmente, mi peso es de %.2f kilogramos' % (w_0 / 2.2))
# print(round(w_0 / 2.2))
# print('-------------------------------------------------')
# # Chapter 2
# print('while loop')
# C = -20
# dC = 5
# while C <= 40:
#     F = (9 / 5) * C + 32
#     print(round(C), round(F))
#     C += dC
# print('-------------------------------------------------')
# print('Ejemplo 2')
# lb = 134
# w = 2
# while lb <= 166:
#     kg = lb / 2.2
#     print(round(kg), lb)
#     lb += w
# print('-------------------------------------------------')
# C = [1, 13, 4, 2, 17, 3, 5, 8, 12, 7, 6]
# C = sorted(C)
# print(C)
# del C[-1]
# C.remove(13)
# del C[-1:]
# C.append(10)
# C.insert(-1, 9)
# print(len(C), min(C), max(C), C[-1], C[1:5],
#       sum(C), 3 in C, 78 in C, C.count(1))
# print(C)
# print(isinstance(C, tuple))
# print(isinstance(C, list))
# print(10 in C)

# data = ['Yisel', 35, 'brown']
# name, age, eyes = data
# print(name)
# print(age)
# print(eyes)

# from math import *
# radii = [1, 2, 3, 4, 5, 6, 7]
# for R in radii:
#       A_circle = pi * R ** 2
#       Vol_sphere = (4 / 3) * pi * R ** 3
#       print(R, round(A_circle), round(Vol_sphere))

# A_square = []
# for R in radii:
#       Area = R ** 2
#       A_square.append(Area)
# print(A_square)

# step = 0.5
# start = 2
# n = 16
# radii = [0.0] * n
# Area = [0.0] * n
# for i in range(n):
#       radii[i] = start + i * step
#       Area[i] = radii[i] ** 2
#       print(radii[i], round(Area[i]))

# radii = range(2, 10, 2)
# area = [0.0] * len(radii)
# for i in range(len(radii)):
#       area[i] = radii[i] ** 2
# print(area)

# # Modifying elements in a list
# side_1 = [1, 2, 3, 4, 5, 6]
# for i, e in enumerate(side_1):
#       side_1[i] = e + 5
# print(side_1)

# for i, e in enumerate(side_1):
#       side_1[i] /= 5
# print(side_1)


# old = [1, 2, 6, 24, 120, 720]
# new_1 = [round(sqrt(e)) for e in old]
# new_2 = [e + 5 for e in old]
# print(new_1, new_2)
# for i in range(len(old)):
#       print(old[i], new_1[i], new_2[i])

# # converting list into table
# for a, b, c in zip(old, new_1, new_2):
#       print(a, b, c)

# for A, B, C in zip(old, new_1, new_2):
#       A = round(A ** 2)
#       B = round(B / 2)
#       C = round(4 / 3 * pi * C ** 3)
#       print(A, B, C)

# # nested list
# table_1 = []
# table_2 = []
# for a, b, c in zip(old, new_1, new_2):
#       table_1.append([a, b, c])
# print(table_1)

# grades = []
# grades.append([1, 2, 3, 4])
# grades.append([5, 6])
# grades.append([7, 8, 9])
# # print(grades)
# # print(grades[0][1])

# for student in grades:
#       for grade in student:
#             print(grade)
#       print()

# for s in range(len(grades)):
#       for g in range(len(grades[s])):
#             grade = grades[s][g]
#             print(grade)
#       print()

# # possible isotop table
# isotops = []
# isotops.append(['H', 'He'])
# isotops.append(['Na', 'Be', 'B', 'C', 'O'])
# print(isotops[0][0])
# del isotops[0][0]
# print(isotops[0][0])
# isotops[0].insert(0, ['hydrogen', 'deuterium', 'tritium'])
# # following these steps, we can create a table within a table of isotops
# print(isotops[0])

# # Basic function or 1-variable function
# def F(C):
#       return (9 / 5) * C + 32


# print(F(4))

# # using functions for lists
# Radii = [1, 2, 3, 4, 5]


# def A(r):
#       return pi * r ** 2


# Area = [round(A(r)) for r in Radii]
# print(Area)


# def Vol(r):
#       V_sphere = (4 / 3) * pi * r ** 3
#       return (r, round(V_sphere))


# r1 = 20
# Volume_1 = Vol(r1)
# print(Volume_1)


# Vol_total = [Vol(r) for r in Radii]
# print(Vol_total)


# def makelist(start, stop, inc):
#       value = start
#       list_1 = []
#       while value <= stop:
#             list_1.append(value)
#             value += inc
#       return list_1


# new_list = makelist(start=4, stop=10, inc=0.5)
# print(new_list)


# # multiple return value
# def Geometrics(radius, height, base):
#       """Calculate the Area and Volume of an object"""
#       A = 1 / 2 * base * radius
#       V = 1 / 2 * base * radius * height
#       return A, V


# a, v = Geometrics(2, 3, 4)
# print(a, v)

# base_values = [0.5 * i for i in range(5)]
# for b in base_values:
#       Area, Volume = Geometrics(2, 3, b)
#       print('Para una base de %.2f el are es igual a %.2f y el volumen del prisma es %2.f' % (
#             b, Area, Volume))

# print(Geometrics.__doc__)

# # if test
# from math import *


# def f(x):
#       if 0 <= x <= pi:
#             value = cos(x)
#       else:
#             value = 0
#       return value


# x0 = 0
# x1 = 0.4
# x2 = 5
# print(f(x0), f(x1), f(x2))

# # arrays
# import numpy as np
# radii = [1, 2, 3, 4, 5]
# a1 = np.array(radii)
# print(a1)
# print(type(a1))

# a2 = np.linspace(1, 10, 4)
# print(a2)

# # vectorization


# def f(x):
#       return x ** 4 * np.exp(-x)


# x = np.linspace(-3, 3, 11)
# y = f(x)

# print(y)

# y_array = y.copy()
# print(y_array)


# def f(t):
#       return t ** 2 * np.exp(-t**2)


# t = np.linspace(0, 3, 21)
# y = np.zeros(len(t))
# for i in np.arange(len(t)):
#       y[i] = f(t[i])


# rho_array = np.zeros(9)
# print(rho_array)

# list_init = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# eta_array = np.asarray(list_init)
# print(isinstance(eta_array, np.ndarray))
# print(isinstance(eta_array, (float, int)))
# print(eta_array.size)
# eta_array.shape = (3, 3)
# print(eta_array)
# print(type(eta_array))
# print(eta_array.shape, len(eta_array))

# # faster way of creating an array
# t_array = np.linspace(1, 30, 30).reshape(5, 6)
# print(t_array)

# xota_array = np.linspace(1, 27, 27).reshape(3, 9)
# print(xota_array)

# epsilon_array = np.array([4, 5, 6], float)
# print(epsilon_array)
# epsilon_matrix = np.mat(epsilon_array)
# print(epsilon_matrix)
# epsilon_transpose = np.mat(epsilon_matrix).transpose()
# print(epsilon_transpose)
# epsilon_mult = epsilon_matrix * epsilon_transpose
# print(epsilon_mult, type(epsilon_mult))

# dictionaries
# data_6a = open('data_6a.txt', 'r')
# lines = data_6a.readlines()
# print(lines)

# lines_b = []
# for line in data_6a:
#       lines_b.append(line)
# print(lines_b)

# lines_c = [line for line in data_6a]
# print(lines_c)

# mean = 0
# for line in lines_c:
#       numb = float(line)
#       mean += numb
# mean = mean / len(lines_c)
# print(mean)

# mean_b = sum([float(line) for line in lines_c]) / len(lines_c)
# print(round(mean_b))

# numb_b = [float(line) for line in data_6a.readlines()]
# data_6a.close()
# mean_c = sum(numb_b) / len(numb_b)
# print(round(mean_c))

# data_6b = open('data_6b.txt', 'r')
# mean = 0
# n = 0
# while True:
#       line = data_6b.readline()
#       if not line:
#             break
#       mean += float(line)
#       n += 1
# mean = mean / float(n)
# print(mean)

# # Text and numbers mixture
# def extract_age(filename):
#       infile = open(filename, 'r')
#       infile.readline()
#       ages = []
#       for line in infile:
#             members = line.split()
#             age = round(float(members[1]))
#             ages.append(age)
#       infile.close()
#       return ages


# family_age = extract_age('family_age.txt')
# print(family_age)

# # using same data for dictionaries
# age_of_family = {'Mom': 58, 'Dad': 62, 'Brother': 30}
# print(age_of_family['Brother'])

# if 'Aunt' in age_of_family:
#       print('Aunt:', age_of_family['Aunt'])
# else:
#       print('No age data for Aunt')

# print(age_of_family.keys())
# age_of_family['Uncle'] = 61
# print(age_of_family)

# # Convert file of string and numbers into dictionaries
# def read_file(filename):
#       infile = open(filename, 'r')
#       infile.readline()
#       age_dictionary = {}
#       for line in infile:
#             words = line.split()
#             value = float(words[-1])
#             if len(words[:-1]) == 2:
#                   key = words[0] + '' + words[1]
#             else:
#                   key = words[0]
#             age_dictionary[key] = value
#       infile.close()
#       return age_dictionary


# age_data = read_file('family_age.txt')
# print(age_data)

# file data in nested dictionaries

infile = open('data_6c.txt', 'r')
lines = infile.readlines()
infile.close()
data = {}  # data[property][measure_no] = property_value
first_line = lines[0]
properties = first_line.split()
for p in properties:
      data[p] = {}

for line in lines[1:]:
      words = line.split()
      i = int(words[0])
      values = words[1:]
      for p, v in zip(properties, values):
            if v != 'no':
                  data[p][i] = float(v)
