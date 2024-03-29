# implementation of a class named Y
class Y:
    """vertical motion of a ball"""

    def __init__(self, v_0):
        self.v_0 = v_0
        self.g = 9.81

    def value(self, t):
        return self.v_0 * t - 0.5 - self.g * t**2

    def formula(self):
        return 'v_0*t - 0.5*g*t**2; v_0=%g' % self.v_0


# construncts and instance bound to the variable y (we created an object from the data type Y)
y = Y(3)
print(y)

# with instance y we can compute the following value:
v = y.value(0.1)
print(v)

print(y.formula())


# Example 2
class VelocityProfile:
    """the class holds the physical parameters"""

    def __init__(self, beta, mu0, n, R):
        self.beta, self.mu0, self.n, self.R = beta, mu0, n, R

    def value(self, r):
        """the class also provides a value(r) method for computing the v function, r is the indepependent variable"""
        beta, mu0, n, R = self.beta, self.mu0, self.n, self.R
        n = float(n)
        v = (beta / (2.0 * mu0))**(1 / n) * (n / (n + 1)) * \
            (R**(1 + 1 / n) - r**(1 + 1 / n))
        return v


v1 = VelocityProfile(R=1, beta=0.06, mu0=0.02, n=0.1)
import numpy as np
r = np.linspace(0, 1, 9)
v = v1.value(r)
print(v)


# Example 3: how can you keep bank accounts in a an organized manner. The underscore _ before a name indicates protection, so no attribute can be touched and not method should be called

class Account:
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = initial_amount

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        """to only read the balance attribute"""
        return self._balance

    def dump(self):
        s = '%s, %s, balance:%s' % (self._name, self._no, self._balance)
        print(s)


a1 = Account('John Smith', '123456789', 500000)
print(a1)
a1.deposit(100000)
a1.withdraw(50000)
print(a1._balance)


# Example 4, set up initially attributes = None to add them later with the corresponding methods
class Phone_book:
    def __init__(self, name, mobile_phone=None, office_phone=None, private_phone=None, email=None):
        self.name = name
        self.mobile = mobile_phone
        self.office = office_phone
        self.private = private_phone
        self.email = email

    def add_mobile_phone(self, number):
        self.mobile = number

    def add_office_phone(self, number):
        self.office = number

    def add_private_phone(self, number):
        self.private = number

    def add_email(self, address):
        self.email = address

    def dump(self):
        s = self.name + '\n'
        if self.mobile is not None:
            s += self.mobile + '\n'
        if self.office is not None:
            s += self.office + '\n'
        if self.private is not None:
            s += self.private + '\n'
        if self.email is not None:
            s += self.email
        print(s)


PhB1 = Phone_book('Lady Gaga', office_phone='3054778230',
                  email='gagahulala@badromance.com')
PhB2 = Phone_book('David Copperfield', office_phone='infinity')
PhB2.add_email('loststatue@newliberty.com')
phone_notebook = [PhB1, PhB2]

for person in phone_notebook:
    print(person.dump())


# Example of the use of classes for geometric figures
from math import *


class Circle:
    def __init__(self, x0, y0, R):
        self.x0, self.y0, self.R = x0, y0, R

    def area(self):
        return pi * self.R**2

    def circumference(self):
        return 2 * pi * self.R


C1 = Circle(2, -1, 5)
print('A circle with radius %g at (%g, %g) has area %g' %
      (C1.R, C1.x0, C1.y0, C1.area()))

# # Special Methods
# Special method __call__


class Derivative:
    def __init__(self, f, h=1E-9):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x + h) - f(x)) / h


df = Derivative(sin)
x = pi
print(df(x))
print(cos(x))

# the following is the direct formula if we were not using classes
print((sin(pi + float(1E-9)) - sin(pi)) / float(1E-9))


def g(t):
    return t ** 3


dg = Derivative(g)
t = 1
print(dg(t))

# special method __string__. For this, we will reuse the Y class previously defined


class Y2:

    def __init__(self, v_0):
        self.v_0 = v_0
        self.g = 9.81

    def __call__(self, t):
        return self.v_0 * t - 0.5 - self.g * t**2

    def __str__(self):
        return 'v_0*t - 0.5*g*t**2; v_0=%g' % self.v_0


y = Y2(1.5)
print(y(0.2))
print(y)

# implementing what we learned


class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None, private=None, email=None):
        p = Phone_book(name, mobile, office, private, email)
        self.contacts[name] = p

    def __str__(self):
        s = ''
        for p in sorted(self.contacts):
            s += str(self.contacts[p])
        return s

    def __call__(self, name):
        return self.contacts[name]


b = PhoneBook()
b.add('Yisi Martina', office='1234667788', email='ymartinita @ yahoo.com')
b.add('Pochito Pio', office='789456147', mobile='9874546321')

print(b('Yisi Martina'))
print(b)
