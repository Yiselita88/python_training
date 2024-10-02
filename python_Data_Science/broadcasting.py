import numpy as np
M = np.ones((2, 3))
print(M)

a = np.arange(3)
print(a)

print(M + a)

# example where broadcasting does not work
M = np.ones((3, 2))
print(M, M.shape)

a = np.arange(3)
print(a, a.shape)

# print(M + a) @ this will raise an error

# using broadcasting to center an array
pass
# add the code here

# comparison operator as ufunc
b = np.array([1, 2, 3, 4, 5])
print(b < 3)

print(2 * b == b**2)

print(np.less(b, 4))

# Boolean arrays and masks (examples)
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)
print(summer)
