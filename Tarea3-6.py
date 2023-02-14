import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
#Problema 6
x=[]

for i in range (0,150):
        x.append(2.5+i*0.01)
        w=[0.2]
        y=[]
        z=[]
        for j in range (0,999):
                pt=x[i]*w[j]*(1-w[j])
                w.append(pt)
                if j>948:
                        y.append(w[j])
                        z.append(x[i])
        plt.plot(z,y,'mo',marker='o',markeredgecolor='cyan')

plt.xlabel('R')
plt.ylabel('$W_{t}$')
plt.grid()
plt.show()
