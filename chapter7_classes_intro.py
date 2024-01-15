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

# Example 3: how can you keep bank accounts in a an organized manner
