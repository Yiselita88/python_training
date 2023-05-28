# as a recap, keyword or named arguments are palce always after ordinal or postional arguments
from math import pi, exp, sin


def f(t, A=1, a=1, omega=2 * pi):
    return A * exp(-a * t) * sin(omega * t)
    """Calling f with just the t argument specified:"""


v1 = f(0.2)
"""We can also call the following"""
v2 = f(0.2, omega=1)
v3 = f(1, A=5, omega=pi, a=pi**2)
v4 = f(A=5, a=2, t=0.01, omega=0.1)
v5 = f(0.2, 0.5, 1, 1)

print(v1, v2, v3, v4, v5)

# Computing sum with default tolearnce


def L2(x, epsilon=1.0E-6):
    x = float(x)
    i = 1
    term = (1 / i) * (x / (1 + x))**i
    s = term
    while abs(term) > epsilon:  # bs(x) is |x|
        i += 1
        term = (1 / i) * (x / (1 + x))**i
        s += term
    return s, i


from math import log
x = 10
for k in range(4, 14, 2):
    epsilon = 10**(-k)
    approx, n = L2(x, epsilon=epsilon)
    exact = log(1 + x)
    exact_error = exact - approx
    print('epsilon: %5.0e, exact_error: %8.2e, n = %d' %
          (epsilon, exact_error, n))

# Doc Strings


def C2F(C):
    """Convert Celsius degrees (C) to Fahrenheit"""
    return (9 / 5) * C + 32


print(C2F.__doc__)  # how to access a documentation string in a function

# functions as arguments to functions


def diff2(f, x, h=1E-6):
    r = (f(x - h) - 2 * f(x) + f(x + h)) / float(h * h)
    return r


def g(t):
    return t**(-6)


t = 1.2
d2g = diff2(g, t)
print("g''(%f)=%f" % (t, d2g))


for k in range(1, 15):
    h = 10**(-k)
    d2g = diff2(g, 1, h)
    print('h=%.0e: %.5f' % (h, d2g))
