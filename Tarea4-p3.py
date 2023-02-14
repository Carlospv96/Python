import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math

x=np.array([0,1.65,1.75,1.86,2.07,2.30,2.52,3.02,3.7,4.45,5.3])
y=np.array([0,0.1,0.11,0.21,0.23,0.22,0.5,0.68,0.75,0.85,0.76])
dy=17/89*x
plt.plot(x,y,'or')
plt.plot(x,dy)
plt.axis([0,6,0,1])
plt.grid(True)
plt.xlabel('$P_{t}$')
plt.ylabel('$P_{t+1}-P_{t}$')
plt.show()


x=np.array([1.65,1.75,1.86,2.07,2.30,2.52,3.02,3.7,4.45,5.3,6.06])
t=np.array([0,1,2,3,4,5,6,7,8,9,10])
dy=1.65*(106/89)**t
plt.plot(t,x,'or')
plt.plot(t,dy,'xb')
plt.xlabel('t')
plt.ylabel('$P_{t}$')
plt.axis([-0.3,12,-0.3,12])
plt.grid(True)
plt.legend(['Datos obs','$P_{t}=1.65(106/89)^t$'],loc='upper left')
plt.show()

h=np.array([0.9,1.1,1.25,1.35,1.45,1.6,1.8,1.88,1.9,2.1,2.12])
f=np.array([0,1,2,3,4,5,6,7,8,9,10])
df=0.9+(2.1-0.9)/9*f
plt.plot(f,h,'or')
plt.plot(f,df,'xb')
plt.xlabel('t')
plt.ylabel('$F_{t}$')
plt.legend(['Datos obs','$F_{t}=0.9+0.1333t$'],loc='upper left')
plt.grid(True)
plt.show()
