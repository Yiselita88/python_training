# # 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sklearn 
iris = sns.load_dataset('iris')
print(iris.head())
sns.set()
# sns.pairplot(iris, hue='species', size=1.5)
# plt.show()
X_iris = iris.drop('species', axis=1) # discard the column called species
print(X_iris.shape, X_iris.head())
y_iris = iris['species']
print(y_iris.shape, y_iris.head())  # y_iris will be the dropped column: species

# supervised learning example: simple linear regression
rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)

from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True)

X = x[:, np.newaxis]
print(X, X.shape)
print(model.fit(X, y))
xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)
# plt.scatter(x,y)
# plt.plot(xfit, yfit)
# plt.show()

from sklearn.decomposition import PCA
model = PCA(n_components=2)
model.fit(X_iris)
X_2D = model.transform(X_iris)
iris['PCA1'] = X_2D[:, 0]
iris['PCA2'] = X_2D[:, 1]
sns.lmplot(x="PCA1", y="PCA2", hue='species', data=iris, fit_reg=False)
plt.show()