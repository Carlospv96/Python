import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# function that returns dy/dt
def model(y,t):
    k = 0.1
    dydt = t-y
    return dydt

# initial condition
y0 = 2

# time points
t = np.linspace(0,4)

# solve ODE
y = odeint(model,y0,t)

n=16
a=0
b=4
h=(b-a)/n
z=[2]
x=[a]

for i in range(0,n):
    m1=x[i]-z[i]
    m2=x[i]+h-(z[i]+h*m1)
    m=(m1+m2)/2
    x.append(a+(i+1)*h)
    z.append(z[i]+h*m)

print(z)
print(x)

# plot results
plt.plot(t,y)
for i in range(0,n+1):
    plt.plot(x[i],z[i],'o',color='orange',markersize=5)
    
plt.legend(['$y(t)=t+3e^{-t}-1$','aprox'])
plt.grid(True)
plt.xlabel('time')
plt.ylabel('v(t)')
plt.show()
