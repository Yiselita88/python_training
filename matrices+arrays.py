import numpy as np
from math import pi
# Matrices and Arrays (Higher-dimensional arrays)
a = 4
radii = [2 + i * 4 for i in range(3)]
perimeter = [2 * (a + R) for R in radii]
print(radii)
print(perimeter)
table = [[R, P] for R, P in zip(radii, perimeter)]
print(table)

# converting the nested list named "table" into a 2D-array (or array of rank 2)
table_array = np.array(table)
print(table_array)
print(type(table))
print(type(table_array))


print(table[1][0])
print(table_array[1][0])
print(table_array[1, 0])    # similar to print(table_array[1][0])
print(table_array.shape)

# A script to access every single element of the array
for i in range(table_array.shape[0]):
    for j in range(table_array.shape[1]):
        print('table_array[%d,%d] = %g' % (i, j, table_array[i, j]))


# similar way using single for loop
for index_tuple, value in np.ndenumerate(table_array):
    print('index %s has value %g' % (index_tuple, table_array[index_tuple]))


# Slicing arrays
print(table_array[0:table_array.shape[0], 1])    # 2nd column
print(table_array[0:, 1])
print(table_array[:, 1])

big_arr = np.linspace(1, 30, 30).reshape(5, 6)
print(big_arr)
print(big_arr[1:-1:2, 2:])
print(big_arr[:-2, :-1:2])

print('--------------')
# Matrix objects
x1 = np.array([1, 2, 3], float)
x2 = np.matrix(x1)
x3 = np.mat(x1).transpose()
print(x1)
print(x2)
print(x3, type(x3))
print(isinstance(x3, np.matrix))

A = np.eye(3)
print(A)
A = np.mat(A)
print(A)
y2 = x2 * A
print(y2)
y3 = A * x3
print('------')
print(y3)
