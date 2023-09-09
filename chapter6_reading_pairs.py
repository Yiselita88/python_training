# Reading pair of numbers
# read all line objects and indicates which ones are starting in the next line
lines = open('read_pairs1.dat', 'r').readlines()
# print(lines)
pairs = []
for line in lines:
    words = line.split()  # it splits the lines and gives them separated
    # print(words)
    for word in words:
        word = word[1:-1]  # strip off parentheses
        # print(word)
        # as it splits the words, it also assigns values to n1 and n2 variables
        n1, n2 = word.split(',')
        # print(n1, n2)
        n1 = float(n1)
        n2 = float(n2)
        pair = (n1, n2)
        print(pair)  # this prints the columns of all pairs
        # after converting the numbers into words, then it appends them into the list of pairs
        pairs.append(pair)
print(pairs)  # this prints the list of all pairs


# Reading pair of numbers when white spaces between parentheses are present
infile = open('read_pairs2.dat', 'r')
lines2 = infile.readlines()

pairs2 = []
for line2 in lines2:
    line2 = line2.strip()
    # this is the important part, where we're eliminating the blank spaces
    line2 = line2.replace(' ', '')
    # here we're eliminating the ')(' that separates the pair
    words = line2.split(')(')
    # here, for the first ford we're eliminating the leading parenthesis
    words[0] = words[0][1:]
    # here we're eliminating the last parenthesis of the last object in the line
    words[-1] = words[-1][:-1]
    for word in words:
        n1, n2, = word.split(',')
        n1 = float(n1)
        n2 = float(n2)
        pair = (n1, n2)
        pairs2.append(pair)
        print(pair)
print(pairs2)

print('-------------Reading coordinates-------------')
# Reading coordinates, files with (x, y, z)
# There are several solutions but here we present 2 solutions
# solution 1: String search
infile3 = open('xyz.dat', 'r')
coord = []
for line3 in infile3:
    x_start = line3.find('x=')
    y_start = line3.find('y=')
    z_start = line3.find('z=')
    x = line3[x_start + 2:y_start]
    y = line3[y_start + 2:z_start]
    z = line3[z_start + 2:]
    print(float(x), float(y), float(z))
    coord.append((float(x), float(y), float(z)))
infile3.close()
from numpy import *
coord = array(coord)
print(coord.shape, coord)

print('----------Solution 2: String split---------------')
infile4 = open('xyz.dat', 'r')
coord4 = []
for line4 in infile4:
    words4 = line4.split('=')   # split with respect to the '='
    # print(words4)
    x = float(words4[1][:-1])
    y = float(words4[2][:-1])
    z = float(words4[3])
    coord4.append((x, y, z))
infile4.close()
from numpy import *
coord4 = array(coord4)
print(coord4.shape, coord4)
