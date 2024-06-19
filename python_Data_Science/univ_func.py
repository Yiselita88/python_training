# specifying outputs
import numpy as np
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)

z = np.zeros(10)
np.power(3, x, out=z[::2])
print(z)
print('---------------------')


# # Agregates # #
b = np.arange(1, 6)
print(b)
print(np.sum(b))
print(np.add.reduce(b))  # similar to previous
print(np.prod(b))
print(np.multiply.reduce(b))  # similar to previous
print(np.cumsum(b))
print(np.add.accumulate(b))  # similar to previous
print(np.cumprod(b))
print(np.multiply.accumulate(b))  # similar to previous

print(np.multiply.outer(b, b))
print(np.add.outer(b, b))

c = np.array([2, 3, 5])
print(np.add.outer(c, c))
print(np.multiply.outer(c, c))

# similarly, it can be done with different arrays, as it creates matrices using arithmetic operations with them
print(np.multiply.outer(b, c))

print('----------------------')
# Min and Max
d = np.random.rand(1000000)
print(min(d), max(d))
print(np.min(d), np.max(d))  # this is faster than the previous one
print(d.min(), d.max(), d.sum())

print('----------------------')
# multidimensional aggregates
g_array = np.random.random((3, 4))
print(g_array)
print(g_array.sum())
print(g_array.min(axis=0))  # it returns the minimum value within each column
print(g_array.min(axis=1))  # it returns the minimum value within each row
