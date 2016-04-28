from __future__ import division
import scipy as sy
import matplotlib.pyplot as plt

def graficar (l):
    v=1
    c=1
    y=[]
    for i in range(0,47000):
        rand = sy.random.uniform(0,sy.pi)
        vel=(v*sy.sin(rand))/(1-(v/c)*sy.cos(rand))
        if vel<50: #no me interesan los demas valores
            y.append(vel)


    plt.figure(l)
    n, bins, patches = plt.hist(y,1500, normed=1, facecolor='green', alpha=0.5,cumulative=1)
    plt.xlabel("Velocidad")
    plt.ylabel("Probabilidad")

l="CDF"    
graficar(l)

plt.show()

