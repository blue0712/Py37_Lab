import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

mu = 80
sigma = 8

x = mu + sigma * np.random.randn(10000)
print(type(x), x.shape)
print(x[:10])
print(len(x))
num_bins = 50
n, bins, patches = plt.hist(x, num_bins, density=1,
                            facecolor='blue')
y = stats.norm.pdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel("sample data")
plt.ylabel('frequency')
plt.title('random number chart')
plt.show()