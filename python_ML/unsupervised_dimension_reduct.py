import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sklearn 
from sklearn.datasets import load_digits
from sklearn.manifold import Isomap
digits = load_digits()
print(digits.images.shape)
X = digits.data
print(X.shape)
y = digits.target
print(y.shape)
iso = Isomap(n_components=2)
iso.fit(digits.data)
data_projected = iso.transform(digits.data)
print(data_projected.shape)

# the following 3 lines are from the old code
# plt.scatter(data_projected[:, 0], data_projected[:, 1], c=digits.target, edgecolor='none', alpha=0.5, cmap=plt.cm.get_cmap('tab10', 10))
# plt.colorbar(label='digit label', ticks=range(10))
# plt.clim(-0.5, 0.5)

# these are the updated version of the code
plt.scatter(data_projected[:, 0], data_projected[:, 1], c=digits.target, 
            edgecolor='none', alpha=0.5, cmap='tab10')
plt.colorbar(label='digit label')
plt.show()