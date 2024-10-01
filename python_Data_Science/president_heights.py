import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)

print(heights.mean(), heights.std(), heights.min(), heights.max())

print(np.percentile(heights, 25))

print(heights.max() == np.max(heights))

plt.hist(heights)
plt.xlabel('height (cm)')
plt.ylabel('number')
# plt.show()
