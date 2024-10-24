# # # basic array sorting (not the most efficient)
# # import numpy as np


# # def selection_sort(x):
# #     for i in range(len(x)):
# #         swap = i + np.argmin(x[i:])
# #         (x[i], x[swap]) = (x[swap], x[i])
# #     return x


# # x = np.array([2, 1, 4, 3, 5])
# # print(selection_sort(x))

# # # more efficient algorithm
# # print(np.sort(x))

# # # also could be:
# # print(x.sort())

# import numpy as np
# X = np.random.rand(10, 2)
# # print(X)
# #print(X[:, 0])
# print(X[:, np.newaxis, :], X[np.newaxis, :, :])

import pandas as pd
print(pd.__version__)
