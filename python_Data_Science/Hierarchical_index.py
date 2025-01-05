# multiply indexed series
import numpy as np
import pandas as pd
index = [('California', 2000), ('California', 2010), ('New York', 2000), ('New York', 2010), ('Texas', 2000), ('Texas', 2010)]
population = [33871648, 37253956, 18976457, 19378102, 20851820, 25145561]
pop = pd.Series(population, index=index)
index = pd.MultiIndex.from_tuples(index)
print(index)
# to see the hierarchical representation of the data
pop = pop.reindex(index)
print(pop)
print(pop[:, 2010])
print(pop[:, 2000])

# multiIndex as extra dimension
pop_df = pop.unstack()
print(pop_df)
print(pop_df.stack())

# add extra column with multiindex
pop_df = pd.DataFrame({'total': pop, 'under_18': [9267089, 9284094, 4687374, 4318033, 5906301, 6879014]})
print(pop_df)

f_u18 = pop_df['under_18'] / pop_df['total']
print(f_u18.unstack())

# # multiindex creation
ndx_array = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
print(ndx_array)
ndx_tupple = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
print(ndx_tupple)
ndx_product = pd.MultiIndex.from_product([['a', 'b'], [1, 2]])
print(ndx_product)

pop.index.names = ['state', 'year']
print(pop)

# multiindex for columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
# mock some data
data = np.round(np.random.randn(4, 6), 1)
print(data)
data[:, ::2] *= 10
data += 37
print(data)
# create DF
health_data = pd.DataFrame(data, index=index, columns=columns)
print(health_data)
# access a specific data
print(health_data['Sue'])

# # multiply indez df
print(health_data.iloc[:2, :2])
print(health_data.loc[:, ('Bob', 'HR')])

# data aggregation on multiindex
data_mean = health_data.mean(level='year')
print(data_mean)
print(data_mean.mean(axis=1, level='type'))

# # Indexing and slicing multiindex
print(pop)
print(pop['California'])
print(pop['California', 2000])
print(pop.loc['California':'New York'])
print(pop[:, 2000])
print(pop[pop > 22000000])
print(pop[['California', 'Texas']])

# sorted and unsorted index
index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
print(data)
data = data.sort_index()
print(data)
print(data['a':'b'])

# stacking and unstacking indices
print(pop.unstack(level=0))
print(pop.unstack(level=1))
print(pop.unstack().stack())

# Index setting and resetting
pop_flat = pop.reset_index(name='population')
print(pop_flat)
print(pop_flat.set_index('state', 'year'))