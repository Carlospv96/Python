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

#Metodo de Runge-Kutta
for i in range(0,n):
    s1=x[i]-z[i]
    s2=(x[i]+0.5*h)-(z[i]+0.5*h*s1)
    s3=(x[i]+0.5*h)-(z[i]+0.5*h*s2)
    s4=(x[i]+h)-(z[i]+h*s3)
    z.append(z[i]+(h/6)*(s1+2*s2+2*s3+s4))
    x.append(a+(i+1)*h)

# Graficamos los resultados
plt.plot(t,y)
for i in range(0,n+1):
    plt.plot(x[i],z[i],'o',color='orange',markersize=5)
    
plt.legend(['$y(t)=t+3e^{-t}-1$','aprox'])
plt.grid(True)
plt.xlabel('time')
plt.ylabel('v(t)')
plt.show()
