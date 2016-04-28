from __future__ import division
import scipy as sy
import matplotlib.pyplot as plt

vector=sy.arange(-5,5,0.1)
matriz=[]
vec=[]


for i in vector:
    vec=[]
    for j in vector:
        covarianza=sy.exp((-1/2)*((i-j)**2))
        vec.append(covarianza)

    matriz.append(vec)
    
    
media=sy.zeros(100)

x = sy.random.multivariate_normal(media, matriz,200) #gracias a internet puedo usar esto =)

y=sy.random.multivariate_normal(media, matriz,200)

plt.figure("3")
plt.plot(x, y, 'x')
plt.axis('equal')

plt.xlabel("X")
plt.ylabel("Y")
plt.show()

