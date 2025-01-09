# # U funcs: index preservation
import pandas as pd
import numpy as np
rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0,10,4))
# print(ser)
df = pd.DataFrame(rng.randint(0, 10, (3,4)), columns=['A', 'B', 'C', 'D'])
print(df)
print(np.exp(ser))
print(np.sin(df * np.pi /4))

# # Ufuncs: Index alignment
# index alignment in series
area = pd.Series({'La Habana': 85974, 'Mayabeque': 167543, 'Pinar del Rio': 184567}, name='area')
population = pd.Series({'La Habana': 1765890, 'Artemisa': 675980, 'Pinar del Rio': 876432}, name='population')
print(population/area)
print(area.index | population.index)

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
print(A, B, A + B)
print(A.add(B, fill_value=0))

# index alignment in DF
A = pd.DataFrame(rng.randint(0, 20, (2, 2)), columns=list('AB'))
B = pd.DataFrame(rng.randint(0, 10, (3, 3)), columns=list('ABC'))
fill = A.stack().mean()
print(A, B, A + B)
print(A.add(B, fill_value=fill))

# Ufuncs: operation between DF and Series
A = rng.randint(10, size=(3, 4))
# print(A)
df = pd.DataFrame(A, columns=list('QRST'))
print(df, df - df.iloc[0])
print(df.subtract(df['R'], axis=0))

halfrow = df.loc[0, ::2]
print(halfrow)
print(df - halfrow)