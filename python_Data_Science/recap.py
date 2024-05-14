import numpy as np
# # generating n-dimensional arrays and slicing them
a1 = np.random.seed(0)
print(a1)

a2 = np.random.randint(22, size=8)
print(a2[7])

a3 = np.random.randint(108, size=(8, 13))
print(a3[:8, ::2])

a4 = np.random.randint(11, size=(2, 3, 4))
print(a4[::2, ::-2, ::2])

a5 = np.random.randint(45, size=(2, 3, 4, 5))
print(a5[::2, ::2, ::2, ::2])

a6 = np.random.randint(83, size=(2, 3, 4, 5, 6))
print(a6[::2, ::2, ::2, ::2, ::2])

a7 = np.random.normal(5, 1, (3, 3, 3, 3))
print(a7[:, 0, 0, 0])
print(a7[0, :, 0, 0])

a8 = np.array([[12, 5, 2, 4],
               [7, 6, 8, 8],
               [1, 6, 7, 7]])

a8_sub = a8[:2, :2]
print(a8_sub)

a8_sub[0, 0] = 99  # if a subarray is modified, the original array is also modified
print(a8)

# reshaping arrays
a9 = np.array([1, 5, 8])
a9_new = a9[:, np.newaxis]
print(a9_new)

a10 = np.arange(1, 13).reshape((3, 4))
print(a10)

grid_1 = np.array([[1, 2, 3], [7, 8, 9]])
grid_2 = np.array([[10, 11, 12], [4, 5, 6]])

# arrays concatenation
grid_conc = np.concatenate([grid_1, grid_2], axis=1)
print(grid_conc)
grid_concat = np.concatenate([grid_1, grid_2], axis=0)
print(grid_concat)

v_conc = np.vstack([a9, grid_1])
print(v_conc)
h_conc = np.hstack([grid_2, a8_sub])
print(h_conc)

# array splitting
a11 = np.array([1, 3, 4, 99, 99, 4, 3, 1])
x1, x2, x3, x4 = np.split(a11, [2, 4, 6])
print(x1, x2, x3, x4)

grid_3 = np.arange(30).reshape((6, 5))
print(grid_3)
upper, lower = np.vsplit(grid_3, [2])
print(upper)
print(lower)
left, right = np.hsplit(grid_3, [3])
print(left)
print(right)
