# if not specify arguement=value, the order of arguments will matter
def yfunc(t, v0):
    g = 9.81  # local variable with fixed value
    return v0 * t - 0.5 * g * t ** 2


# calling the function
y1 = yfunc(0.1, 6)
y2 = yfunc(6, 0.1)
# y1 != y2, the sequence of arguments in call must match the order in the function
print(y1, y2)

# best way to avoid mistakes is to specify the value of the argument when calling the function
y3 = yfunc(t=0.1, v0=6)
y4 = yfunc(v0=6, t=0.1)
print(y3, y4)  # notice y3 == y4

# using makelist() instead of range(), as the former can generate real numbers


def makelist(start, stop, step):
    value = start
    result = []
    while value <= stop:
        result.append(value)
        value = value + step
    return result


mylist = makelist(0, 10, 0.2)
# print(mylist) # uncomment this


# # multiple return values
def yfunc(t, v0):
    g = 9.81
    y = v0 * t - 0.5 * g * t**2
    dydt = v0 - g * t
    return y, dydt


position, velocity = yfunc(0.6, 3)
print(position, velocity)

# table of velocities corresponding to different times
t_values = [0.05 * i for i in range(10)]
for t in t_values:
    pos, vel = yfunc(t, v0=0.5)
    print('t=%-10g position=%-10g velocity=%-10g' % (t, pos, vel))
