# implementation of a class named Y
class Y:
    """vertical motion of a ball"""

    def __init__(self, v_0):
        self.v_0 = v_0
        self.g = 9.81

    def value(self, t):
        return self.v_0 * t - 0.5 - self.g * t**2


# construncts and instance bound to the variable y (we created an object from the data type Y)
y = Y(3)
print(y)

# with instance y we can compute the following value:
v = y.value(0.1)
print(v)
