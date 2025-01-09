# # Concat & Append
import pandas as pd
import numpy as np

# define a function to quickly create a dataframe
def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)

# example
# print(make_df('ABCD', range(4)))

df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])

print(pd.concat([df1, df2]))

df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
print(pd.concat([df3, df4], axis='columns'))

# adding multiindex keys
x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
print(pd.concat([x, y], keys=['x', 'y']))

# # Merge and Join
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'], 'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'], 'hire_date': [2004, 2008, 2012, 2014]})
df3 = pd.merge(df1, df2)
print(df3)
df4 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})
print(pd.merge(df1, df4, left_on="employee", right_on="name"))
print(pd.merge(df1, df4, left_on="employee", right_on="name").drop('name', axis=1))

df1a = df1.set_index('employee')
df2a = df2.set_index('employee')
print(pd.merge(df1a, df4, left_index=True, right_on="name"))

# set arithmetic for joins
df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'], 'food': ['fish', 'beans', 'bread']}, columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'], 'drink': ['wine', 'bear']}, columns=['name', 'drink'])
print(pd.merge(df6, df7, how='inner'))
print(pd.merge(df6, df7, how='outer'))
print(pd.merge(df6, df7, how='left'))