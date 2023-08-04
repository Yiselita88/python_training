# if you want to calculate the volume and area of a cyllinder for list of radii
from math import pi
import numpy as np


def cyllinder(pi, R, h=24):
    volume = pi * R ** 2 * h
    area = 2 * pi * R * h + 2 * pi * R ** 2
    return volume, area


Radii = [0.5 * i for i in range(1, 20, 2)]
for R in Radii:
    volume, area = cyllinder(pi, R, h=20)
    print('Radius=%-5g volume=%-10g area=%-10g' % (R, volume, area))


print('--------------------------------------------------------')
# generalizing the implementation of summatories, let's try with an increment of circle perimeter
from math import pi


def sum(R, n):
    P = 0
    for i in range(1, n + 1):
        P += 4 * R * i
    perimeter = P
    print(perimeter)


def all_perimeter(R):
    for n in range(1, 6, 1):
        result = sum(R, n)
    print(result)  # for no return value functions, we can skip this statement
    print(result == None)  # to verify if an object is an "empty data"
    print(result is None)


sum(1, 1)
sum(1, 2)
sum(1, 3)
sum(1, 4)
sum(1, 5)
print('---------')
all_perimeter(3)

print('---------')
a = 1
b = a
print(a is b)
print(a == b)
c = 1.0
print(a is c)
print(a == c)
print('---------')
print('--------------------------------------------------------')
# # keyword arguments
for R in Radii:
    # this adopts as a defult the keyword argument h=24, therefore we can skipt it
    volume, area = cyllinder(pi, R)
    print('Radius=%-5g volume=%-10g area=%-10g' % (R, volume, area))
print('--------------------------------------------------------')


def somefunc(arg1, arg2, kwarg1=True, kwarg2=0):
    print(arg1, arg2, kwarg1, kwarg2)


somefunc('Hello', [1, 2])
somefunc('Hello', [1, 2], kwarg1='Hi')
# somefunc() # If the positional arguments arg1 & arg2 are not specified, it'll yiled and error
somefunc('Hello', [1, 2], kwarg2='Hi')
somefunc('Hello', [1, 2], kwarg2='Hi', kwarg1=6)

somefunc(kwarg2='Hello', arg1='Hi', kwarg1=6, arg2=[1, 2])

from math import pi, exp, sin


def f(t, A=1, a=1, omega=2 * pi):
    return A * exp(-a * t) * sin(omega * t)


v1 = f(0.2)
v2 = f(0.2, omega=1)
v5 = f(0.2, 0.5, 1, 1)
print(v1, v2, v5)

# # Functions as arguments of functions


def diff2(f, x, h=1E-6):
    r = (f(x - h) - 2 * f(x) + f(x + h)) / float(h * h)
    return r


def g(t):
    return t**(-6)


t = 1.2
d2g = diff2(g, t)
print("g''(%f)=%f" % (t, d2g))


print('----------------')

for k in range(1, 15):
    h = 10**(-k)
    d2g = diff2(g, 1, h)
    print('h=%.0e: %.5f' % (h, d2g))

print('-----------------')


def Volume(l, w, h=24):
    v = l(w) * w * h / 2
    return v


from math import pi, sqrt


def width(A):
    return sqrt(A)


A = 49
vol1 = Volume(width, 2)
print(vol1)


for k in range(1, 10):
    w = k ** 2
    vol_seq = Volume(width, w)
    print('for w=%g, the volume is %g' % (w, vol_seq))

# main program: collection of all statements outside functions, + definition of functions. Example:
from math import *                                                  # in main


def f(x):                                                           # in main
    e = exp(-0.2 * x)
    s = sin(7 * pi * x)
    return e / s


x = 0.25                                                            # in main
y = f(x)                                                            # in main
print('A result for the main program example is f(%g)=%g' % (x, y))  # in main


print('------')
# lambda functions, same as writing: f = lambda x: x ** 2 + 4
d2 = diff2(lambda t: t ** (-6), 1, h=1E-4)
print(d2)

d2_2 = diff2(lambda t, A=1, a=0.5: -a * 2 * t * A * exp(-a * t**2), 1.2)
print(d2_2)
