import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

#problema 5
#a)
y=[100]
for i in range (0,90):
	pt=y[i]+0.1*y[i]*(1-y[i]/500)
	y.append(pt)

y1=[50]
for i in range (0,90):
	pt=y1[i]+0.1*y1[i]*(1-y1[i]/500)
	y1.append(pt)

y2=[800]
for i in range (0,90):
	pt=y2[i]+0.1*y2[i]*(1-y2[i]/500)
	y2.append(pt)
	
x=[]

for i in range (0,91):
    x.append(i)

plt.plot(x,y,'ro',marker='o')
plt.plot(x,y1,'bo',marker='o')
plt.plot(x,y2,'go',marker='o')
plt.xlabel('t')
plt.ylabel('$P_{t}$')
plt.grid()
plt.show()

#b)

y=[100,100,100]
y1=[50,50,50]
y2=[1500,1500,1500]
x=[]

for i in range (0,88):
    pt=y[i+2]-0.2*y[i+2]+y[i]*(0.2+0.3*(1-y[i+2]/1000))
    y.append(pt)
    
for i in range (0,88):
    pt=y1[i+2]-0.2*y1[i+2]+y1[i]*(0.2+0.3*(1-y1[i+2]/1000))
    y1.append(pt)
    
for i in range (0,88):
    pt=y2[i+2]-0.2*y2[i+2]+y2[i]*(0.2+0.3*(1-y2[i+2]/1000))
    y2.append(pt)
    
for i in range (0,91):
    x.append(i)

plt.plot(x,y,'ro',marker='o')
plt.plot(x,y1,'bo',marker='o')
plt.plot(x,y2,'go',marker='o')
plt.xlabel('t')
plt.ylabel('$P_{t}$')
plt.grid()
plt.show()

#Grafica a)

x = np.arange(0.0, 1.0, 0.01)
y = 1.1*x-0.05
dy = x

## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy)
plt.plot(0.5, 0.5, 'or')

#Telarañas
x=0.4
for i in range (0,3):
        plt.plot(x,1.1*x-0.05,'og',markersize=2.5)
        if i>0:
                plt.plot(x,x,'og',markersize=2.5)
        x=1.1*x-0.05

plt.plot([0.4,0.4,0.4,0.4],[0.09,0.19,0.29,0.39],'g--',markersize=1)
plt.plot([0.4-0.25*0.01,0.4-0.5*0.01,0.4-0.75*0.01],[0.39,0.39,0.39],'g--',markersize=1)
plt.plot([0.39,0.39,0.39],[0.39-0.25*0.01,0.39-0.5*0.01,0.39-0.75*0.01],'g--',markersize=1)
plt.plot([0.39-0.25*0.01,0.39-0.5*0.01,0.39-0.75*0.01],[0.379,0.379,0.379],'g--',markersize=1)
plt.plot([0.379,0.379,0.379],[0.379-0.25*0.01,0.379-0.5*0.01,0.379-0.75*0.01],'g--',markersize=1)

## Config the graph
plt.xlabel('x')
plt.ylabel('F(x)')
plt.axis([0.3,0.51,0.3,0.51])
#plt.ylim([0, 1])
plt.grid(True)
plt.legend(['F(x) = 1.1x-0.05', 'y = x','(0.5,0.5)'], loc='upper left')

## Show the graph
plt.show()

#Grafica b)

x = np.arange(0.0, 1.0, 0.01)
y = -0.9*x**2+2*x-0.1
dy = x

## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy)
plt.plot(0.111, 0.111, 'or')
plt.plot(1,1,'or')

#Telaraña
x=0.5
for i in range (0,3):
        plt.plot(x,-0.9*x**2+2*x-0.1,'og',markersize=2.5)
        if i>0:
                plt.plot(x,x,'og',markersize=2.5)
        x=-0.9*x**2+2*x-0.1

plt.plot([0.5,0.5,0.5,0.5],[0,0.25,0.5,0.675],'g--',markersize=1)
plt.plot([0.5,0.5+0.25*0.175,0.5+0.5*0.175,0.5+0.75*0.175,0.5+0.175],[0.675,0.675,0.675,0.675,0.675],'g--',markersize=1)
plt.plot([0.675,0.675,0.675,0.675,0.675],[0.675,0.675+0.25*0.164,0.675+0.5*0.164,0.675+0.75*0.164,0.675+0.164],'g--', markersize=1)
plt.plot([0.675,0.675+0.25*0.164,0.675+0.5*0.164,0.675+0.75*0.164,0.675+0.164],[0.839,0.839,0.839,0.839,0.839],'g--',markersize=1)
plt.plot([0.839,0.839,0.839,0.839,0.839],[0.839,0.839+0.25*0.105,0.839+0.5*0.105,0.839+0.75*0.105,0.839+0.105],'g--',markersize=1)

## Config the graph
plt.xlabel('x')
plt.ylabel('F(x)')
#plt.ylim([0, 1])
plt.grid(True)
plt.legend(['F(x) = -0.9x+2x-0.1', 'y = x','(0.111,0.111)','(1,1)'], loc='upper left')

## Show the graph
plt.show()

#Grafica c)

x = np.arange(0.0, 1.0, 0.01)
y = 8*x**3-12*x**2+6*x-0.5
dy = x

## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy)
plt.plot(0.146,0.146 , 'or')
plt.plot(0.5,0.5, 'or')
plt.plot(0.854,0.854, 'or')

#Telaraña
x=0.2
for i in range (0,3):
        plt.plot(x,8*x**3-12*x**2+6*x-0.5,'og',markersize=2.5)
        if i>0:
                plt.plot(x,x,'og',markersize=2.5)
        x=8*x**3-12*x**2+6*x-0.5

x=0.7
for i in range (0,2):
        plt.plot(x,8*x**3-12*x**2+6*x-0.5,'og',markersize=2.5)
        if i>0:
                plt.plot(x,x,'og',markersize=2.5)
        x=8*x**3-12*x**2+6*x-0.5
plt.plot([0.7,0.7,0.7,0.7,0.7,0.7],[0,0.11,0.22,0.33,0.44,0.564],'g--',markersize=1)
plt.plot([0.7,0.7-0.25*0.136,0.7-0.5*0.136,0.7-0.75*0.136,0.564],[0.564,0.564,0.564,0.564,0.564],'g--',markersize=1)
plt.plot([0.564,0.564,0.564,0.564,0.564],[0.564,0.564-0.25*0.062,0.564-0.5*0.062,0.564-0.75*0.062,0.502],'g--',markersize=1)

plt.plot([0.2,0.2,0.2,0.2],[0,0.09,0.18,0.284],'g--',markersize=1)
plt.plot([0.2,0.2+0.25*0.084,0.2+0.5*0.084,0.2+0.75*0.084,0.284],[0.284,0.284,0.284,0.284,0.284],'g--',markersize=1)
plt.plot([0.284,0.284,0.284,0.284,0.284],[0.284,0.284+0.25*0.135,0.284+0.5*0.135,0.284+0.75*0.135,0.284+0.135],'g--',markersize=1)
plt.plot([0.284,0.284+0.25*0.135,0.284+0.5*0.135,0.284+0.75*0.135,0.284+0.135],[0.419,0.419,0.419,0.419,0.419],'g--',markersize=1)
plt.plot([0.419,0.419,0.419,0.419,0.419],[0.419,0.419+0.25*0.076,0.419+0.5*0.076,0.419+0.75*0.076,0.419+0.076],'g--',markersize=1)
## Config the graph
plt.xlabel('x')
plt.ylabel('F(x)')
#plt.ylim([0, 1])
plt.grid(True)
plt.legend(['F(x) = $8x^3-12x^2+6x-1/2$', 'y = x','(0.146,0.146)','(0.5,0.5)','(0.854,0.854)'], loc='upper left')

## Show the graph
plt.show()
