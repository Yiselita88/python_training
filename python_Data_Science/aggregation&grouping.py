import pandas as pd
import numpy as np

df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'], 'data': range(6)}, columns=['key', 'data'])
print(df.groupby('key').sum())

rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'], 'data1': range(6), 'data2': rng.randint(0, 10, 6)}, columns=['key', 'data1', 'data2'])
print(df)
print(df.groupby('key').aggregate(['min', np.median, max]))

# filtering
def filter_func(x):
    return x['data2'].std() > 4

print(df.groupby('key').std())
print(df.groupby('key').filter(filter_func))

# transformation
print(df.groupby('key').transform(lambda x: x - x.mean()))

# apply() method
def norm_by_data2(x):
    x['data1']/= x['data2'].sum()
    return x

print(df.groupby('key').apply(norm_by_data2))

L = [0, 1, 0, 1, 2, 0]
print(df); print(df.groupby(L).sum())
print(df.groupby(df['key']).sum())

# mapping index to group
df2 = df.set_index('key')
mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
print(df2); print(df2.groupby(mapping).sum())
print(df2.groupby(str.lower).mean())
print(df2.groupby([str.lower, mapping]).std())


# # Pandas str methods
monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin'])
print(monte.str.lower())
print(monte.str.len())
print(monte.str.split())
print(monte.str.split().str.get(-1))
print(monte.str.split().str.get(-2))
