import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

#Aqui definimos la ecuacion diferencial
def model(y,t):
    dydt = t-y 
    return dydt

#Aqui va el valor inicial de la ecuacion diferencial
y0 = 2

#Aqui definimos el intervalo
t = np.linspace(0,4)

# Esto resuelve la ecuacion diferencial
y = odeint(model,y0,t)

n=16 #Numero de intervalos que se desea
a=0
b=4
h=(b-a)/n
z=[2] #Aqui Valor inicial de la ecuacion diferencial
x=[a]

#Metodo del Trapecio
for i in range(0,n):
    m1=x[i]-z[i]
    m2=x[i]+h-(z[i]+h*m1)
    m=(m1+m2)/2
    x.append(a+(i+1)*h)
    z.append(z[i]+h*m)

# Graficamos los resultados
plt.plot(t,y)
for i in range(0,n+1):
    plt.plot(x[i],z[i],'o',color='orange',markersize=5)
    
plt.legend(['$y(t)=t+3e^{-t}-1$','aprox'])
plt.grid(True)
plt.xlabel('time')
plt.ylabel('v(t)')
plt.show()
