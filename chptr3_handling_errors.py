print('----uncomment every block one at a time-----')
# # the following commented script will yield and error. Uncomment it to see what happen
# import sys
# C = float(sys.argv[1])
# F = (9 / 5) * C + 32
# print(F)

# # This is how to handle the previous error
# # by using sys.exit function
# import sys
# if len(sys.argv) < 2:
#     print('You failed to provide Celsius degrees as input '
#           'on the command line!')
#     sys.exit(1)  # abort because of error
# C = float(sys.argv[1])
# F = (9 / 5) * C + 32
# print(F)


print('-----Exception Handling-----')
# import sys
# try:
#     C = float(sys.argv[1])
# except:
#     print('You failed to provide Celsius degrees as input on the command line!')
#     sys.exit(1)  # abort
# F = (9 / 5) * C + 32
# print(C, F)

# Testing for specific exception
# import sys
# try:
#     C = float(sys.argv[1])
# except IndexError:
#     print('Celsius degrees must be applied on the command line')
#     sys.exit(1)  # abort execution
# except ValueError:
#     print('Celsius degrees must be a pure number, not "%s"' % sys.argv[1])
#     sys.exit(1)

# F = (9 / 5) * C + 32
# print(C, F)

import sys


# def read_C():
#     try:
#         C = float(sys.argv[1])
#     except IndexError:
#         raise IndexError('Celsius must applied on cmmd line')
#     except ValueError:
#         raise ValueError('Celsius must be pure')
#     if C < -273.15:
#         raise ValueError('C=%g is non-physical' % (C))
#     return C


# C1 = read_C()


def read_C():
    try:
        C = read_C()
    except (ValueError, IndexError) as e:
        print(e)
    sys.exit(1)
