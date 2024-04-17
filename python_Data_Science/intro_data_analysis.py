# random refreshing from first python tutorial
def func1(a, b):
    return a / b


print(func1(20, 4))
y1 = func1(36, 6)
print(y1)


def func2(x):
    a = x
    b = x - 1
    return func1(a, b)


print(func2(2))


# # # Intro to NumPy # # #
import numpy as np
print(np.__version__)  # to know which numpy version we have installed

# create integer list
L1 = list(range(10))
print(L1)

# create string list
L2 = [str(c) for c in L1]
print(L2)

# example of heterogeneous list
L3 = [True, "2", 3.0, 4]
print([type(item) for item in L3])

# create numpy arrays from python lists
b1 = np.array([1, 4, 2, 5, 3], dtype='float32')
print(b1)
print(type(b1))

b2 = np.array([range(i, i + 3) for i in range(10)])
print(b2)

# # creating arrange from scratch # #
# 1- create a lenght-10 integer array filled with zeros
a1 = np.zeros(10, dtype=int)
print(a1, type(a1))

# 2- create a 3x5 floating-point array filled with 1s
a2 = np.ones((3, 5), dtype=float)
print(a2, type(a2))

# 3- create 4x7 array filled with 3.14
a3 = np.full((4, 7), 3.14)
print(a3, type(a3))

# 4- create a linear sequence array
a4 = np.arange(0, 20, 2)
print(a4, type(a4))

# 5- five value evenly spaced array, between 0 and 1
a5 = np.linspace(0, 1, 5)
print(a5)

#  6- create a 3x3 (rowxcolumn) array of uniformly distributed random values between 0 and 1 (every time is going to give different values)
a6 = np.random.random((3, 3))
print(a6)

# 7- create a 4x2 (rowxcolumn) array of normally distributed random values with mean 0 and standard deviation 1 (every time is going to give different values)
a7 = np.random.normal(0, 1, (4, 2))
print(a7)

# 8- create 5x6 (rowxcolumn) array of random integers in the interval [0, 10)
a8 = np.random.randint(0, 30, (5, 6))
print(a8)

# create a 7x7 (rowxcolumn) identity matrix
a9 = np.eye(7)
print(a9)

# create an uninitialized array of three integers
a10 = np.empty(8)
print(a10)

# # Numpy Array Attributes # #
# generate random array but with the same set of value every time with seed(0)
import numpy as np
np.random.seed(0)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))

# print attributes
print(x3.ndim, x3.shape, x3.size, x3.dtype, x3.itemsize, x3.nbytes)
print(x2)


# # Array Indexing: Accessing single elements: this is similar to the list part in python intro
print(x1)
print(x1[0])
print(x1[4])
print(x1[-2])
print(x2[0, 0])
print(x2[2, 0])
print(x2[2, -1])

# # array slicing: accessing subarrays: x[start:stop:step]
# 1D subarray
z = np.arange(10)
print(z)
print(z[:5])
print(z[5:])
print(z[4:7])
print(z[::2])
print(z[1::2])
print(z[::-1])  # all elements reversed
print(z[5::-2])

# multidimensional subarrays
print(x2[:2, :3])
print(x2[:3, ::2])
print(x2[::-1, ::-1])

print('-----------')
# accesing array rows and columns
print(x2)
print(x2[:, 0])  # first column of x2
print(x2[0, :])  # first row of x2
print(x2[0])     # equivalent to print(x2[0, :])

# changing arrays by changing their sub-arrays
x2_sub = x2[:2, :2]
print(x2_sub)

x2_sub[0, 0] = 99
print(x2_sub)

print(x2)

# # create copies of arrays
# step 1: create subcopy of the array
x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)

# step 2: assign new element to a given postion of the copy
x2_sub_copy[0, 0] = 42
print(x2_sub_copy)

# # array reshaping
omh = np.array([1, 2, 3])

# row vector via reshape
print(omh.reshape((1, 3)), omh.dtype)

# row vector via newaxis
print(omh[np.newaxis, :], omh.dtype)

# column vector via reshape
print(omh.reshape((3, 1)))

# column vector via newaxis
print(omh[:, np.newaxis])

# # array concatenation
delta = np.array([7, 8, 9])
gamma = np.array([125, 131, 99])
iota = np.array([88, 88, 88])

dg = np.concatenate([delta, gamma])
print(dg)

dgi = np.concatenate([delta, iota, gamma])
print(dgi)

grid = np.array([[1, 2, 3],
                 [4, 5, 6]])

# concatenate along the first axis
gridx2 = np.concatenate([grid, grid])
print(gridx2)

# concatenate along the second axis (zero-indexed)
gridx3 = np.concatenate([grid, grid], axis=1)
print(gridx3)

# # working with arrays of different dimensions, how to concatenate them
# vertical stach
print(np.vstack([grid, delta]))
theta = np.array([[99],
                  [99]])

# horizontal stack
print(np.hstack([grid, theta]))

# # Splitting arrays
print(dgi)
dgi1, dgi2, dgi3 = np.split(dgi, [3, 5])
print(dgi1, dgi2, dgi3)

grid1 = np.arange(16).reshape((4, 4))
print(grid1)

# similarly to np.split we can pass indices giving the split points
# vertical split
upper, lower = np.vsplit(grid1, [2])
print(upper)
print(lower)

# horizontal split
left, right = np.hsplit(grid1, [2])
print(left)
print(right)
