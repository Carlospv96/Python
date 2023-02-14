import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
x=[0.1]
y=[0.2]
for i in range(0,20):
    x.append(x[i]+0.3*x[i]*(1-0.2*y[i]-x[i]))
    y.append(y[i]+0.2*y[i]*(1+0.1*x[i]-y[i]))

plt.plot(x,y,'ro',marker='o',markersize=6,color="red",label='($x_{n}$,$y_{n}$)')
plt.legend()
plt.xlabel('$x_{n}$')
plt.ylabel('$y_{n}$')
plt.grid(True)
plt.show()

e=[-0.7]
n=[-0.9]
for i in range(0,8):
    e.append(0.7647*e[i]-0.04706*n[i])
    n.append(0.02157*e[i]+0.7843*n[i])

for i in range(0,9):
    e[i]=e[i]+0.7843
    n[i]=n[i]+1.0784

plt.plot(e,n,'bx',mew=2,markersize=6,label='($\u03BE_{n}$,$\u03B7_{n}$)')
plt.plot(x,y,'ro',marker='o',markersize=5,color="red",label='($x_{n}$,$y_{n}$)')
plt.legend()
plt.xlabel('$x_{n}$ y $\u03BE_{n}$')
plt.ylabel('$y_{n}$ y $\u03B7_{n}$')
plt.grid(True)
plt.show()
