# functions in python
def F(C):
    return (9 / 5) * C + 32


# calling or invoking the function
a = 10
F1 = F(a)
print(F1)
print(F(a + 1))

temp = F(15.5)
print(temp)

sum_temp = F(10) + F(20)
print(sum_temp)

Cdegrees = [-20, -15, -5, 10, 35, 40]
Fdegrees = [F(C) for C in Cdegrees]
print(Fdegrees)

# retunrning formatting strings and creating variables inside a function


def F2(C):
    F_value = (9 / 5) * C + 32
    return '%.1f degrees Celsius corresponds to '\
           '%.1f degrees Fahrenheit' % (C, F_value)


s1 = F2(21)
print(s1)
c1 = 37.5
s2 = F2(c1)
print(s2)

print('---------------------------------')

# example of the previous function definition
from math import pi


def V(R):
    volume = (4 / 3) * pi * R ** 3
    return 'The volume of a sphere of radius %.1f cm '\
           'is equal to %.1f cm^3' % (R, volume)


V1 = V(21)
print(V1)

# python order of variables with the samer name: local, global, built-in python functions
print(sum)
sum = 500
print(sum)


def myfunc(n):
    sum = n + 1
    print(sum)
    return sum


sum = myfunc(2) + 1
print(sum)

print('--------------------------------')
# example using areas and radii
from math import pi


def A(R):
    area = 4 * pi * R ** 2  # local variable
    # print(A)
    print(area)
    return(area + 35)


Area1 = A(3)
print(Area1)
# this is to better undestand which area value corresponds to which global variable. Notices it'll print the original area without adding the 35 in the return
print('--------------------------------')
Area2 = A(3) + 40
print(Area2)


a = 20
b = - 2.5  # global variables


def f1(x):
    a = 21  # new local variable
    return a * x + b  # 21 * x -2.5


print(a)  # prints 20, original global variable


def f2(x):
    global a
    a = 35
    return a * x + b


f1(3)
print(a)
f2(3)
print(a)
