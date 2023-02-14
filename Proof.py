import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# function that returns dy/dt
def model(y,t):
    dydt = 0.2-0.04*y
    return dydt

# initial condition
y0 = 0

# time points
t = np.linspace(0,55)

# solve ODE
y = odeint(model,y0,t)


# plot results
plt.plot(t,y,color='red')
plt.legend(['$P(t)=5-5e^{-0.04t}$'])
plt.grid(True)
plt.xlabel('time')
plt.ylabel('P(t)')
plt.show()
