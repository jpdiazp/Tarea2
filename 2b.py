from __future__ import division
import scipy as sy
import matplotlib.pyplot as plt
from scipy.stats import norm


y=[]

for i in range(0,5000):
    x = sy.random.uniform(0,1)
    normal=norm.ppf(x)
    y.append(normal)


plt.figure("1")
n, bins, patches = plt.hist(y, 50, facecolor='green', alpha=0.5,normed=1)
plt.xlabel("X")
plt.ylabel("$\phi_{\mu,\sigma^2}(X)$")
plt.show()