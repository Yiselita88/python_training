# if tests
from math import pi, sin


def f(x):
    if 0 <= x <= pi:
        value = sin(x)
    else:
        value = 0
    return value


sin_1 = f(2)
sin_2 = f(4)
print(sin_1, sin_2)


def N(x):
    if x < 0:
        return 0.0
    elif 0 <= x < 1:
        return x
    elif 1 <= x < 2:
        return 2 - x
    elif x >= 2:
        return 0.0


N_1 = N(-2)
N_2 = N(0)
N_3 = N(0.89)
N_4 = N(1)
N_5 = N(1.5)
N_6 = N(3)
print(N_1, N_2, N_3, N_4, N_5, N_6)

# one-line syntax


def f1(x):
    return (sin(x) if 0 <= x <= 2 * pi else 0)


f1_1 = f1(0)
f1_2 = f1(2)
fi_3 = f1(3)
print(f1_1, f1_2, fi_3)

# # SUMMARY of Chapter 2
t = 0
dt = 0.5
T = 2
while t <= T:
    print(t)
    t += dt
print('Final t:', t, '; t <= T is', t <= T)

for elem in [10, 15, pi, 78, 1 / 2, 35.8]:
    print(elem)

for element in range(1, 5, 2):
    print(element)


def funct(x):
    if x < 0:
        value = -1
    elif x >= 0 and x <= 1:
        value = x
    else:
        value = 1
    return value


funct_1 = funct(-2)
funct_2 = funct(0.5)
funct_3 = funct(2)
print(funct_1, funct_2, funct_3)

print('--------------------')
# functions


def quadratic_polyn(x, a, b, c):
    value = a * x * x + b * x + c
    derivative = 2 * a * x + b
    return value, derivative


x = 1
p, dp = quadratic_polyn(x, 2, 0.5, 1)
print(p, dp)
p1, dp1 = quadratic_polyn(x=x, a=-4, b=0.5, c=0)
print(p1, dp1)


# f(x) w/ no arguments and no return values
def print_date():
    """Print the current date in the format 'June 14, 2023'."""
    import time
    print(time.strftime("%b %d, %Y"))


print_date()
from math import exp, sin, pi


def synus(x, A=1, a=1, w=pi):
    return A * exp(-a * x) * sin(w * x)


synus1 = synus(0)
x2 = 0.1
synus2 = synus(x2, w=2 * pi)
print(synus1, synus2)

print('----Example of a full program----')
# example of a full program
g = 9.8
v_0 = 5
dt = 0.25


def yfunc(t):
    return v_0 * t - 0.5 * g * t**2


def table():
    data = []
    t = 0
    while yfunc(t) >= 0:
        data.append([t, yfunc(t)])
        t += dt
    return data


data_table = table()
print(data_table)


for t, y in data_table:
    print('%5.1f %5.1f' % (t, y))

# extract y values from data_table and create a list with them
y_list = [y for t, y in data_table]
print(y_list)

ymax = 0
for yi in y_list:
    if yi > ymax:
        ymax = yi
print('max y(t) =', ymax)

data_table = table()
