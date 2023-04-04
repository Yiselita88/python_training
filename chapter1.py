print(5 * 0.6 - 0.5 * 9.81 * 0.6**2)

v_0 = 55
g = 9.815459387492829
t = 5987.2452
y = v_0 * t - 1 / 2 * g * t**2
print(y)

print('At t=%g s, with the Earth gravity g=%.4G the heigth of the ball is %14.6E m' % (t, g, y))
y = 3
y = y + 4
print(y)
y = y * y
print(y)

# page 19
C = 21
F = (9 / 5) * C + 32
F2 = int(9 / 5) * C + 32
print(F, F2)

a = C
z = 5 / (9 + 2) * a**(4 / 2)
z2 = 5 / (9 + 2) * a**4 / 2
print(z, z2)

import math
v_0 = 5
g = 9.81
y_c = 0.2
from math import sqrt, e, pi, log as ln, exp, sin, cos, log10 as log
print(ln(e), log(10))
t1 = (v_0 - sqrt(v_0**2 - 2 * g * y_c)) / g
t2 = (v_0 + sqrt(v_0**2 - 2 * g * y_c)) / g
print(t1, t2)
v = sin(pi)
print(v)

a = 3.7
b = int(2)
c = 'vanilla'
d = [3, 2, 1]
f = (5, 6, 7)
g = {'R': 'ARG', 'H': 'HIS'}
print(type(g), type(a), type(b), type(c), type(d), type(f))
h = int(a)
k = int(round(a))
print(h, k)

# complex numbers
u = 2.5 + 3j
v = 2
w = u + v
print(w)

a = -2
b = 0.5
s = a + b * 1j
s = complex(a, b)
print(s)
print(s * w)
print(s / w)
print(s.real)
print(w.imag)
print(s.conjugate())

from cmath import sin, sinh, cos, cosh, exp
r = sin(w)
print(r)
r1 = sin(8j)
r2 = 1j * sinh(8)
print(r1)
print(r2)

q = 8
print(exp(1j * q))
print(cos(q) + 1j * sin(q))

from numpy.lib.scimath import *
print(sqrt(4))
print(sqrt(-1))

theta = 60
x = 0.5
y_0 = 1
g = 9.81
v_0 = 15
v_0 = v_0 / 3.6
theta = theta * pi / 180
print("""\
    v_0 = %d km/h
    theta = %.1f radians\
    """ % (v_0, theta))
