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
