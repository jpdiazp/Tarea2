from __future__ import division
import scipy as sy
import matplotlib.pyplot as plt
from scipy.linalg import cholesky

vector=sy.arange(-5,5,0.1)
matriz=[]
vec=[]
epsilon=42 #lo multiplico para que la matriz sea positiva definida pero no funciona =(


for j in vector:
    vec=[]
    for i in vector:
        covarianza=epsilon*sy.exp((-1/2)*((i-j)**2))
        vec.append(covarianza)

    matriz.append(vec)
    

chol=cholesky(matriz,lower=1)    


normal=sy.random.normal(0,1,100)

diagonal=sy.diag(sy.diag(normal))
print diagonal

X=chol*diagonal



plt.figure("2")
n, bins, patches = plt.hist(X, 10, facecolor='green', alpha=0.5,normed=1)
plt.xlabel("X")
plt.ylabel("$\phi_{\mu,\sigma^2}(X)$")
plt.show()


