import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math

#Grafica a)

x = np.arange(0.0, 1.0, 0.01)
y = x*(1-x)
dy = x

## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy,'--y')
plt.plot(0,0,'og')

## Config the graph
plt.xlabel('x')
plt.ylabel('F(x)')
plt.axis([-0.05,1,-0.05,1])
#plt.ylim([0, 1])
plt.grid(True)
plt.legend(['F(x) = x(1-x)', 'y = x','(0,0)'], loc='upper left')

plt.arrow(0.5,0,0,0.22,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.5,0.25,-0.22,0,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.25,0.25,0,-0.0325,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.25,0.1875,-0.0325,0,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.1875,0.1875,0,0.1875*(1-0.1875)-0.1875+0.03,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.1875,0.1875*(1-0.1875),0.1875*(1-0.1875)-0.1875+0.03,0,head_width=0.01,head_length=0.03,color='pink')

## Show the graph
plt.show()

#Grafica b)

x = np.arange(0.0, 1.0, 0.01)
y = 2*x*(1-x)
dy = x

## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy,'--y')
plt.plot(0.5,0.5,'og')
plt.plot(0,0,'og')

## Config the graph
plt.xlabel('x')
plt.ylabel('F(x)')
plt.axis([-0.05,1,-0.05,1])
#plt.ylim([0, 1])
plt.grid(True)
plt.legend(['F(x) = 2x(1-x)', 'y = x','(0,0)','(0.5,0.5)'], loc='upper left')

plt.arrow(0.25,0,0,0.345,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.25,0.375,0.095,0,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.375,0.375,0,(15/32)-0.375-0.03,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.375,15/32,15/32 - 0.375-0.03,0,head_width=0.01,head_length=0.03,color='pink')

## Show the graph
plt.show()

#Grafica c)

x = np.arange(0.0, 1.0, 0.01)
y = 3.5*x*(1-x)
dy = x

## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy,'--y')
plt.plot(5/7,5/7,'og')
plt.plot(0,0,'og')

## Config the graph
plt.xlabel('x')
plt.ylabel('F(x)')
plt.axis([-0.05,1,-0.05,1])
#plt.ylim([0, 1])
plt.grid(True)
plt.legend(['F(x) = 3.5x(1-x)', 'y = x','(0,0)','(5/7,5/7)'], loc='upper left')

plt.arrow(0.5,0,0,0.845,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.5,0.875,0.345,0,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.875,0.875,0,49/128-0.875+0.03,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(0.875,49/128,49/128-0.875+0.03,0,head_width=0.01,head_length=0.03,color='pink')
plt.arrow(49/128,49/128,0,3.5*(49/128)*(1-49/128)-49/128-0.03,head_width=0.01,head_length=0.03,color='pink')


## Show the graph
plt.show()
