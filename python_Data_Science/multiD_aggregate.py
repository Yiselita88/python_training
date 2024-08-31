import numpy as np

M = np.random.random((3, 4))
print(M)

# minimum value for each column:
min_col = M.min(axis=0)
print(min_col)

# maximum value of each row
max_col = M.max(axis=1)
print(max_col)

# sum of elements
suma = np.sum(M)
print(suma)

# compute product
producto = np.prod(M)
print(producto)

# compute mean
promedio = np.mean(M)
print(promedio)

# compute standard deviation
desviacion = np.std(M)
print(desviacion)

# compute variance
varianza = np.var(M)
print(varianza)

# compute index of minimum value
min_index = np.argmin(M)
print(min_index)
