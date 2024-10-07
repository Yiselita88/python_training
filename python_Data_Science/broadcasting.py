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

# fancy indexing: when passing an array of indices to access multiple array elements at once
import numpy as np
matrx = np.arange(12).reshape(3, 4)
print(matrx)
rw = np.array([0, 1, 2])
clmn = np.array([2, 1, 3])
desire_vl = matrx[rw, clmn]
print(desire_vl)

# combine indexing
print(matrx[2, [3, 0, 2]])
# slicing & combine indexing
print(matrx[1:, [3, 2, 1]])

# example of fancy indexing application
mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
data_1 = np.random.multivariate_normal(mean, cov, 100)
print(data_1.shape)

indices = np.random.choice(data_1.shape[0], 20, replace=False)
print(indices)
selection = data_1[indices]
print(selection.shape)

import matplotlib
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

# plt.scatter(data_1[:, 0], data_1[:, 1])

#plt.scatter(data_1[:, 0], data_1[:, 1], alpha=0.3)
#plt.scatter(selection[:, 0], selection[:, 1], color='red', s=200)
# plt.show()

# example for bining data
np.random.seed(42)
x = np.random.randn(100)

bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

i = np.searchsorted(bins, x)
np.add.at(counts, i, 1)
#plt.plot(bins, counts, linestyle='solid')

plt.hist(x, bins, histtype='step')
plt.show()
