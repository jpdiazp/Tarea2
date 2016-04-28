from __future__ import division
import scipy as sy
import matplotlib.pyplot as plt

def graficar (l):   #defino la funcion que grafica los datos
    v=1
    c=1
    y=[]
    x=sy.arange(0,sy.pi*2,0.01)
    for i in x:
        vel=(v*sy.sin(i))/(1-(v/c)*sy.cos(i))
        y.append(vel)

    plt.figure(l)
    plt.plot(x,y,label=(l))            
    plt.xlabel("$\\theta$")
    plt.ylabel("v($\\theta$)")
    plt.legend()

l="velocidad"    
graficar(l)

plt.show()
