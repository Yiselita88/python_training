t = (2, 4, 6, 'temp.pdf')
for element in ('myfile.txt', 'yourfile.txt', 'herfile.txt'):
    print(element)

t = t + (-1.0, -2.0)
print(t)
print(t[1])
print(t[2:])
print(6 in t)
print(10 in t)

# t[1] = -1
# t.append(0)
# del t[1]

print("---- Now we'll see a summary of lists and tuples ---------")

# # SUMMARY OF LISTS & TUPLES (video reference: https://www.youtube.com/watch?v=W8KRzm-HUcc)

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses[0])
print(courses[-1])
print(courses[0:])
print(courses[0:2])
print(courses[2:])

courses.append('Art')

courses.insert(0, 'ChemBio')

courses_2 = ['Philosophy', 'StatThermo']
courses.insert(0, courses_2)
print(courses[0])

del courses[0]
print(courses[0])
courses.extend(courses_2)

courses.remove('Philosophy')

popped = courses.pop()
print(popped)

courses.reverse()

courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

# if you don NOT want to alter your original list it is better to use a sorted() function instead
courses = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses = sorted(courses)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('CompSci'))
# print(courses.index('Art'))
print('Art' in courses)
print('Math' in courses)

for item in courses:
    print(item)

for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(index, course)


courses = ['History', 'Math', 'Physics', 'CompSci']
courses_str = ', '.join(courses)
print(courses_str)

courses_str = ' - '.join(courses)
print(courses_str)

new_list = courses_str.split(' - ')
print(new_list)

# mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# tuple_1[1] = 'Art'

# # Sets: through away duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)
print('Math' in cs_courses)
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
