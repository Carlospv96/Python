import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

x=[0,3,6,9,12,15]
y=[math.log(2),math.log(1),math.log(0.5),math.log(0.25),math.log(0.13),math.log(0.06)]
t=np.arange(0.0,15.0,0.01)
l=0.693-0.233*t
plt.plot(x,y,'ro')
plt.plot(t,l)
plt.legend(['$ln(P(t))$','$ln(P(t))=0.693-0.233t$'],loc='upper right')
plt.xlabel('$t$')
plt.ylabel('$\log(P(t))$')
plt.grid(True)
plt.show()

a=[2]
for i in range(0,5):
    a.append(1.999*math.exp(-0.233*x[i+1]))
y=[2,1,0.5,0.25,0.13,0.06]
print(a)
plt.plot(x,y,'ro')
plt.plot(x,a,'bx')
plt.grid(True)
plt.xlabel('$t$')
plt.ylabel('$P(t)$')
plt.legend(['$P(t)$','$P(t)=1.999e^{-0.233t}$'],loc='upper right')
plt.show()
