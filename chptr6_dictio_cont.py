# loading a tabular data into a nested dictionary
infile = open('table.dat', 'r')
lines = infile.readlines()
infile.close()
data = {}
first_line = lines[0]
properties = first_line.split()
for p in properties:
    data[p] = {}

for line in lines[1:]:
    words = line.split()
    i = int(words[0])
    values = words[1:]
    for p, v in zip(properties, values):
        if v != 'no':
            data[p][i] = float(v)

# to compute the mean values:
for p in data:
    values = data[p].values()
    data[p]['mean'] = sum(values) / len(values)

for p in sorted(data):
    print('Mean values of property %s = %g' % (p, data[p]['mean']))


# working with strings
s = 'Berlin: 18.4 C at 4 pm'
print(s.find('at'))

# checking if some string is within another string
if 'Y' in s:
    print('Y is found')
else:
    print('no Y')

print(s.startswith('Berlin'))
print(s.endswith('am'))

print(s.replace('Berlin', 'Paris'))

# diverse manners of string splitting
# split by whitespace
each_string = s.split()
print(each_string)
# it can be also splitted with respect of one element of the string
two_strings = s.split('C')    # C is not gonna be in the splitted string
print(two_strings)


s_prime = 'Berlin:\n18 C\nat \n4 pm'
print(s_prime)
print(s.splitlines())
print(s_prime.splitlines())


infile = open('table.dat', 'r')
lines = infile.readlines()
infile.close()
data = {}
line_1st = lines[0]
print(line_1st)
print(line_1st.splitlines())
# example to show the difference between s.split() and s.splitlines()
print(line_1st.split())

print(s.upper())
print(s.lower())
print(s.find('4 pm'))
# s[18] = 5 # this cannot me assigned because strings are constants
print(s[:18] + '5' + s[19:])

print('214'.isdigit())

print(' 214 '.isdigit())

# checking for spaces contained in a string
print(''.isspace())
print(' '.isspace())
print('\n'.isspace())
print('\t'.isspace())
print('--------------------')

line_test = ' \n'
print(line_test.strip() == '')

s = '  text with leading/trailing space  \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Join strings: opposite of the split method
strings = ['newton', 'secant', 'bisection']
t = ', '.join(strings)
print(t)

line = 'this is a line separated by space'
words = line.split()
line2 = ' '.join(words[2:])
print(words)
print(line2)
