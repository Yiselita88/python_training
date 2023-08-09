# # This chapter objectives are files, strings, and dictionaries
# 6.1 Reading a file line by line
import numpy as np
infile = open('data1.txt', 'r')
lines1 = infile.readline()
print(lines1)

lines = []
for line in infile:
    lines.append(line)
print(lines)

lines2 = [line for line in infile]
print(lines2)

print(type(lines))

# mean = 0
# for number in lines:
#     mean = mean + number
# mean = mean / len(lines)     # this yields an error since the lines are considered strings and not numbers

mean = 0
for line in lines:
    number = float(line)
    mean = mean + number
mean = mean / len(lines)

print(mean)

mean1 = sum([float(line) for line in lines]) / len(lines)
print(mean1)

infile2 = open('data1.txt', 'r')
numbers = [float(line) for line in infile2.readlines()]
infile2.close()
mean2 = sum(numbers) / len(numbers)
print(mean2)


# Using while loop for the same goal
infile3 = open('data1.txt', 'r')
mean3 = 0
n = 0
while True:
    line3 = infile3.readline()
    if not line3:
        break
    mean3 += float(line3)
    n += 1
mean3 = mean3 / float(n)
print(mean3)


# Reading a file into a string
infile4 = open('data1.txt', 'r')
filestr4 = infile4.read()
words4 = filestr4.split()
print(words4)
numbers4 = [float(w) for w in words4]
mean4 = sum(numbers4) / len(numbers4)
print(mean4)

# equivalent to the former block
infile5 = open('data1.txt', 'r')
numbers5 = [float(w) for w in infile5.read().split()]
mean5 = sum(numbers5) / len(numbers5)
print(mean5)

print('-------------------------------------------')
# Reading a mixture of text and numbers


def extract_data(filename):
    infile6 = open(filename, 'r')
    infile6.readline()
    numbers6 = []
    for line in infile6:
        words6 = line.split()
        number = float(words6[1])
        numbers6.append(number)
    infile6.close()
    return numbers6


values = extract_data('rainfall.dat')
print(values)

# same code as before using list comprehension


def extract_data2(filename):
    infile7 = open(filename, 'r')
    infile7.readline()
    numbers7 = [float(line.split()[1]) for line in infile7]
    infile7.close()
    return numbers7


values2 = extract_data2('rainfall.dat')
print(values2)
