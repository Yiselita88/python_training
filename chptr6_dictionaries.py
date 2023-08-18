# making dictionaries
temps = {'Oslo': 13, 'London': 15.4, 'Paris': 17.5}
temps['Madrid'] = 26.0

# Dict. operations
for city in temps:
    print('The temperature in %s is %g' % (city, temps[city]))

if 'Berlin' in temps:
    print('Berlin:', temps['Berlin'])
else:
    print('No temperature data for Berlin')

temps['Havana'] = 39.0
print(temps)

if 'London' in temps:
    print('London:', temps['London'])
else:
    print('No temperature data for Berlin')

# Extracting keys and values as lists:
cities = temps.keys()
temps_values = temps.values()
print(cities)
print(temps_values)

# NOTICE: if certain order is needed, it's recommended to sort the dictionaries
for city in sorted(temps):
    print(city, temps[city])

print(len(temps))
del temps['Oslo']
print(temps)

# if we want to keep the original dictionary and make some modifications, make a copy
temps_copy = temps.copy()
del temps_copy['Havana']
print(temps, temps_copy)
t1 = temps_copy
t1['Varadero'] = 29.5
print(temps_copy)

# Polynomials as dictionaries
# power-coefficient pairs, where the powers are the keys and the coefficients are the values
p = {0: -1, 2: 1, 7: 3}


def poly1(data, x):
    sum = 0.0
    for power in data:
        sum += data[power] * x**power
    return sum


data = p
polynomial1 = poly1(data, 2)
print(polynomial1)


# more compact way of defining this function:
def poly2(data, x):
    return sum([data[p] * x**p for p in data])


polynomial2 = poly2(data, 3)
print(polynomial2)

print('---------------------------------------------------------')
# file data in dictionaries


def read_densities(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]

        densities[substance] = density
    infile.close()
    return densities


densities = read_densities('densities.dat')
print(densities)

# # files in nested dictionaries
# example of nested dictionary
d = {'key1': {'key1': 2, 'key2': 3}, 'key2': 7}
print(d['key1'])          # this is a dictionary
print(d['key1']['key2'])  # this is a nested dictionary
