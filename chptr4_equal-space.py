import numpy as np
for i in range(1, 500):
    a = np.arange(0, 1, 1.0 / i)
print(i, a[-1])

# compact syntax for array generation
a = np.r_[-5:5:11j]    # it includes the upper limit
b = np.r_[-5:5:41j]    # it's gonna yield 41 equally spaced numbers
c = np.r_[-5:5:1.0]    # it does not include upper limit
d = np.r_[-5:5:0.25]   # equivalent to b
print(a)
print(b)
print(c)
print(d)
# shape manipulation
a = np.linspace(-1, 1, 6)
print(a.shape)
print(a.size)
a.shape = (2, 3)
print(a)
print(a.shape)          # prints the shape of the array
print(a.size)           # prints the total number of elements
a.shape = (a.size,)     # reset shape to its original one
print(a.shape)
a = a.reshape(3, 2)     # now instead it's having 3 rows and 2 columns
print(a)
print(len(a))           # print number of rows


# combining compact syntax with shape manipulation
m = np.r_[-11:11:28j]
print(m)
print(len(m))
m = m.reshape(7, 4)     # this numbers should be multiples of 28
print(m)

# another way of writing m:
o = np.linspace(-11, 11, 28)
o = o.reshape(7, 4)
print(o)
print(o == m)    # comparing elements of both array o and array m


# another way, depending of what it's desired
n = np.r_[-144:144:12.0]    # upper limit is not included
print(len(n))
n = n.reshape(8, 3)
print(n)
