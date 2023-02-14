import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math

#a)
x = np.arange(-2.5, 3, 0.01)
y = 3*np.log(x)
dy = x

## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy,'--')
plt.plot(1.857183865, 1.857183865, 'ok')



## Config the graph
plt.xlabel('x')
plt.ylabel('F(x)')
plt.axis([-2.5,3,-2.5,3])
#plt.ylim([0, 1])
plt.grid(True)
plt.legend(['F(x) = 1.1x-0.05', 'y = x','(1.8571,1.8571)'], loc='upper left')

#telarañas
plt.arrow(1.25,0,0,3*np.log(1.25)-0.03,head_width=0.09,head_length=0.03,color='red')
plt.arrow(1.25,3*np.log(1.25),3*np.log(1.25)-1.25+0.03,0,head_width=0.09,head_length=0.03,color='red')
plt.arrow(3*np.log(1.25),3*np.log(1.25),0,3*np.log(3*np.log(1.25))-3*np.log(1.25)+0.03,head_width=0.09,head_length=0.03,color='red')
plt.arrow(3*np.log(1.25),3*np.log(3*np.log(1.25)),3*np.log(3*np.log(1.25))-3*np.log(1.25)+0.03,0,head_width=0.09,head_length=0.03,color='red')


## Show the graph
plt.show()

#b)
x = np.arange(-2.5, 3, 0.01)
y = 2*x*np.exp(-x)
dy = x

## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy,'--')
plt.plot(0, 0, 'ok')
plt.plot(0.6931,0.6931,'ok')



## Config the graph
plt.xlabel('x')
plt.ylabel('F(x)')
plt.axis([-0.1,1.5,-0.1,1.5])
#plt.ylim([0, 1])
plt.grid(True)
plt.legend(['F(x) = 1.1x-0.05', 'y = x','(0,0)','(0.6931,0.6931)'], loc='upper left')

#telarañas
plt.arrow(-0.4,0,0,2*-0.4*np.exp(0.4)+0.03,head_width=0.01,head_length=0.03,color='red')
plt.arrow(-0.4,2*-0.4*np.exp(0.4),2*-0.4*np.exp(0.4)+0.4+0.03,0,head_width=0.01,head_length=0.03,color='red')
plt.arrow(2*-0.4*np.exp(0.4),2*-0.4*np.exp(0.4),0,2*(2*-0.4*np.exp(0.4))*np.exp(-2*-0.4*np.exp(0.4))-2*-0.4*np.exp(0.4)+0.03,head_width=0.01,head_length=0.03,color='red')
plt.arrow(2*-0.4*np.exp(0.4),2*(2*-0.4*np.exp(0.4))*np.exp(-2*-0.4*np.exp(0.4)),2*(2*-0.4*np.exp(0.4))*np.exp(-2*-0.4*np.exp(0.4))-2*-0.4*np.exp(0.4)+0.03,0,head_width=0.01,head_length=0.03,color='red')

## Show the graph
plt.show()
