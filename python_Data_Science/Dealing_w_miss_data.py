# # Operate on null value
# detect null value
import pandas as pd
import numpy as np
data = pd.Series([1, np.nan, 'hello', None])
# print(data.isnull())
print(data[data.notnull()])

# drop null value
df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])

print(df.dropna())
print(df.dropna(axis='columns'))
df[3] = np.nan
print(df)

print(df.dropna(axis='columns', how='all'))

print(df.dropna(axis='rows', thresh=3))

# filling null values
data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
print(data)
print(data.fillna(88))
print(data.ffill())
print(data.bfill())

print(df.ffill(axis=1))
print(df.bfill(axis=0))