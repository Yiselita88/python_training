# continue with multiple values returns
def f(x):
    return x, x ** 2, x ** 4


s = f(2)
print(s, type(s))  # it indicates that s is a tuple
x, x2, x4 = f(2)
print(x2)


# # Functions by Corey (chek the link in the README info)
def hello_func():
    pass


print(hello_func)
print(hello_func())


def hello_func():
    print('Hello Function!')


hello_func()

# DRY: don't repeat yourself


def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(hello_func('Hi', name='Yisel'))


def student_info(*args, **kwards):
    print(args)
    print(kwards)


student_info('Math', 'Art', 'CompSci', 'ChemBio', name='Yiselita',
             age=22, year='freshmen', major='Chemistry')

print('------------------------------')
# another way of writing the same function


def student_info(*args, **kwards):
    print(args)
    print(kwards)


courses = ['Math', 'Art', 'CompSci', 'ChemBio']
info = {'name': 'Yiselita', 'age': 22,
        'year': 'freshmen', 'major': 'Chemistry'}

student_info(*courses, **info)  # same as before


print('---------------------------')


def L(x, n):
    s = 0
    for i in range(1, n + 1):
        s += (1 / i) * (x / (1 + x))**i
    value_of_sum = s
    first_neglected_term = (1 / (n + 1)) * (x / (1 + x))**(n + 1)
    from math import log
    exact_error = log(1 + x) - value_of_sum
    return value_of_sum, first_neglected_term, exact_error


# typical call:
value, approximate_error, exact_error = L(x, 100)

# Functions with no return values

from math import log


def table(x):
    print('\nx=%g, ln(1+x)=%g' % (x, log(1 + x)))
    for n in [1, 2, 10, 100, 500]:
        value, next, error = L(x, n)
        print('n = %-4d % -10g(next term: % 8.2e '
              'error: % 8.2e)' % (n, value, next, error))


table(10)
table(1000)
