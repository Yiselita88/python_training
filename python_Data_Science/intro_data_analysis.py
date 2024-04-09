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
