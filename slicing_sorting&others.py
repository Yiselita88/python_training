my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[5])
print(my_list[-1])
print(my_list[-10])

# extracting a range from a list using list[start:end:step]

print(my_list[3:8])

print(my_list[3:-2])

print(my_list[1:])

print(my_list[:-1])  # it goes from 0 to 8

print(my_list[0:7:2])  # end is not included

print(my_list[2:-1:2])

print(my_list[2:-1:-1])  # it prints out an empty list

print(my_list[-1:2:-1])  # print in reverse

print(my_list[-2:1:-2])

print(my_list[::-2])


# Slicing strings

sample_url = 'http://yiselmn.com'

print(sample_url[::-1])

print(sample_url[-4:])

print(sample_url[7:])

print(sample_url[7:-4])

print('-------------')
# sorting in python

messy_list = [9, 7, 4, 1, 5, 3, 8, 2, 6]

s_li = sorted(messy_list)  # using sorted method

print('Sorted Variables:\t', s_li)

messy_list.sort()  # using sorted method

print('Original Variable:\t', messy_list)

s_li = sorted(messy_list, reverse=True)

messy_list.sort(reverse=True)

print('Sorted Variables:\t', s_li)

print('Original Variable:\t', messy_list)

# as tuples do NOT have sort methods, sorted functions are recommended in this case
tup = (9, 7, 4, 1, 5, 3, 8, 2, 6)

s_tup = sorted(tup)
print('Tuple\t', s_tup)

di = {'name': 'Yisel', 'job': 'ballerina', 'age': None, 'os': 'Windows'}
s_di = sorted(di)
print('Dictionary\t', s_di)  # only prints keys in an ordered way

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li)
print(s_li)

s_li = sorted(li, key=abs)  # prints ordered absolute values
print(s_li)

print('---------------')

# recap mutables and immutables

a = 'yisel'
print(a)
print('Address of a is: {}'.format(id(a)))
# a[0] = 'Y' # not possible cuz strings are ummutable
# print(a)

a = 'sophie'
print(a)
print('Address of a is: {}'.format(id(a)))

a = [1, 2, 3, 4, 5]
print(a)
print('Address of a is: {}'.format(id(a)))

a[0] = 6
print(a)
# it changes the values but the address is the same
print('Address of a is: {}'.format(id(a)))


print('---------------')
# working with classes: This is a topic we have not introduce yet, but it's useful for visualizing how to sort within dictionaries


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

# employees = [e1, e2, e3]

# s_employees = sorted(employees) # this does NOT work without defining a customized function

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort)
print(s_employees)


def e_sort(emp):
    return emp.age


s_employees = sorted(employees, key=e_sort)
print(s_employees)


def e_sort(emp):
    return emp.salary


s_employees = sorted(employees, key=e_sort, reverse=True)
print(s_employees)
