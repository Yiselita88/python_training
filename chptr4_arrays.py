def f(x):
    return x ** 3


n = 5
dx = 1.0 / (n - 1)
xlist = [i * dx for i in range(n)]
ylist = [f(x) for x in xlist]
pairs = [[x, y] for x, y in zip(xlist, ylist)]
print(xlist)
print(ylist)
print(pairs)

r = xlist

from numpy import *
a1 = array(r)  # convert a list to an array
a2 = zeros(n)
# creates an array with 5 elements in a range 0 <= x <= 10, equally distributed
a3 = linspace(0, 10, 5)

print(a1)
print(a2)
print(a3)


# Computing coordinates and function values

x2 = array(xlist)
y2 = array(ylist)
print(x2)
print(y2)

# computing arrays directly
from numpy import *
n = len(xlist)
x2 = linspace(0, 1, n)
y2 = zeros(n)
for i in range(n):
    y2[i] = f(x2[i])

print(y2)

# Copying arrays
x = array([1, 2, 3.5])
print(x)
a = x
a[-1] = 3
print(x)

b = x.copy()
b[-1] = 9
print(b)
print(x)

# in-place arithmetics
t = array([1, 2, 3], dtype='float')
c = (3 * t ** 4 + 2 * t + 4) / (t + 1)
print(c)

d = t.copy()
d **= 4
print(d)
d *= 3
print(d)
d += 2 * t
print(d)
d += 4
d /= (t + 1)
print(c)
print(d)

# Allocating arrays
m = zeros(10)
v = m.copy()
w = zeros(m.shape, x.dtype)
print(v)
print(w)

k = [1, 1.5, 2, 2.5, 3, -8, -13.7, 0, 4.8, -9.1, 17.4, -25]
k_1 = asarray(k)  # convert a list into an array
print(k_1)

j = linspace(1, 8, 8)
print(j)
j[[1, 6, 7]] = 10
print(j)

# test for array type
import numpy as np
u = np.linspace(-1, 1, 3)
print(u)
print(type(u))
print(isinstance(u, np.ndarray))
print(type(u) == np.ndarray)
print(isinstance(u, (float, int)))


def f(x):
    return np.zeros(u.shape, u.dtype) + 2


def g(u):
    if isinstance(u, (float, int)):
        return 2
    elif isinstance(u, np.ndarray):
        return np.zeros(u.shape, u.dtype) + 2
    else:
        raise TypeError('u must be int, float or ndarray, not %s' % type(u))


g('circulo')
