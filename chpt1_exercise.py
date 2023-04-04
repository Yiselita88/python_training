# 1
print(1 + 1)

# 2
greeting = 'Hello World'
print(greeting)

# 3
m = 640
cm = m * 100
inch = cm / 2.54
foot = inch / 12
yard = foot / 3
mile = yard / 1760
print('640m = %g cm, %g inches, %g feet, %g yards, %g miles' %
      (cm, inch, foot, yard, mile))
# 4
rho = 21.4
volume = 1
mass = rho * volume * 1000
print('the mass of 1 L of platinum is %g grams' % (mass))

# 5
A = 1000  # euros, initial amount of money
p = 5     # bank interes rate
n = 13    # number of years
B = A * (1 + p / 100)**n  # final amount of money
C = B - A  # how much money did it grow
print('After 13 years, the initial %g euros have grown %g to a final amount of %g euros.' % (A, C, B))

# 6
x = 1
from math import sin
print('sin(%g)=%g' % (x, sin(x)))

# 7
from math import pi
h = 5.0
b = 2.0
r = 1.5
area_parallel = h * b
area_square = b ** 2
area_circle = pi * r**2
volume_cone = (1.0 / 3) * pi * r**2 * h
print("""the area of a parallelogram is %.3f
    the area of the square is %g
    the area of the circle is %8.3f
    the volume of the cone is %.3f""" % (area_parallel, area_square, area_circle, volume_cone))

# 8-a)
from math import sin, cos, pi
x = pi / 4
val_1 = (sin(x))**2 + (cos(x))**2
print(x, val_1)

# 8-b)
v_0 = 3
t = 1
a = 2
s = v_0 + (1 / 2) * a * t**2
print(s)

# 8-c)
a = 3.3
b = 5.3
a2 = a**2
b2 = b**2

sum1 = a2 + 2 * a * b + b2
sum2 = a2 - 2 * a * b + b2

pow1 = (a + b)**2
pow2 = (a - b)**2

print('first eq.: %g = %g' % (sum1, pow1))
print('second eq.: %.1f = %.1f' % (sum2, pow2))

# 9
from math import pi, exp, sqrt
m = 0
s = 2
x = 1
y = (1 / (sqrt(2 * pi) * s)) * exp(-(1 / 2) * ((x - m) / s)**2)
print(y)

# 13
from math import sin, pi
alpha = 0.25
tau = 2 * pi
t = alpha * tau
s = (4 / pi) * (sin(2 * pi * t / tau))
print(s)
s = s + (4 / (3 * pi)) * sin(6 * pi * t / tau)
print(s)
s = s + (4 / (5 * pi)) * sin(10 * pi * t / tau)
print(s)
