# chapter 2 of Scientific_Python book
# this chapter treats the conversion of temperatures in C degree to F degree
# # while loops
# Example 1
print('-----------------')
C = -20
dC = 5
while C <= 40:
    F = (9 / 5.0) * C + 32
    print(C, F)  # this is going to print a table where column 1 is the C degrees (in increments of 5) and column 2 is the F degrees
    C = C + dC
print('------------------')

# Example 2: same procedure, with radii and areas of circles
from math import pi
R = 0
dR = 3
while R <= 30:
    A = pi * R ** 2
    print(R, A)  # so far, there is no formatting
    R += dR
print('_______________________')

# # lists
# Example 3
C = [-20, -15, -5, 0, 5, 10, 15, 20, 25, 30]
C.append(35)  # add a new element to the list at the end
C = C + [40, 45, 50]  # extend at the end
C.insert(2, -10)  # insert a new element in the list as index 2
del C[-1]  # delete the last element, -1 indicates the index backwards
print(C)
print(len(C))  # print the length, a.k.a. amount of elements in the list
print(C.index(10))  # print index corresponding to element 10
print(14 in C)  # verify if element 14 is in list C. it returns a T or F value

# creating a compact list of various variables with its corresponding elements
# for this, I'm going to asign the 3 letter residues (element) to 1 letter residues (variable)
amino_acids = ['ARG', 'HIS', 'LYS', 'ASP', 'GLU', 'SER', 'THR', 'ASN', 'GLN', 'CYS',
               'GLY', 'PRO', 'ALA', 'VAL', 'ILE', 'LEU', 'MET', 'PHE', 'TYR', 'TRP']
print(amino_acids)
R, H, K, D, E, S, T, N, Q, C, G, P, A, V, I, L, M, F, Y, W = amino_acids
print(Y, I, S, E, L)
