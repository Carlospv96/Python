#
# Codigo para elaborar las gráficas y ejemplos para la exposición
# E01-AI
#

#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
#%%


#%%
#  Figura 1
# Gráfica de Densidad de bacterias contra tiempo.

t = [0,1,2,3,4,5]
Bt = [0.022, 0.036, 0.060, 0.101, 0.169, 0.266]

plt.plot(t,Bt,'ro')
plt.axis([-0.1, 5.5, -0.01, 0.32])
plt.grid()
plt.show()
#%%


#%%
# Figura 2
# Gráfica de cambio en densidad de bacterias contra tiempo.


t = [0,1,2,3,4]
iBt = [0.014, 0.024, 0.041, 0.068, 0.097]
plt.plot(t,iBt,'ro')
plt.axis([-0.3,4.3,0.007,0.105])
plt.xlabel(r'$t$')
plt.ylabel('B(t+1) - B(t)')
plt.grid(True)
plt.show()
#%%

#%%
#  Figura 3 
# Gráfica de cambio en densidad de bacterias contra densidad.

Bt = [0.022, 0.036, 0.060, 0.101, 0.169]
iBt = [0.014, 0.024, 0.041, 0.068, 0.097]

plt.plot(Bt, iBt, 'ro',  marker='o', markersize=8, color="red")
plt.xlim(0.01, 0.18)
plt.ylim(0.007, 0.105)
plt.xlabel('B(t)')
plt.ylabel('B(t+1) - B(t)')
plt.grid(True)
plt.show()

#%%


#%%
#  Figura 4 
# Gráfica de cambio en densidad de bacterias contra densidad.
# con linea recta aproximada

Bt = [0.022, 0.036, 0.060, 0.101, 0.169]
iBt = [0.014, 0.024, 0.041, 0.068, 0.097]

plt.plot(Bt, iBt, 'ro',  marker='o', markersize=8, color="red")
plt.plot([0,0.15],[0,0.1], color="blue", linewidth=1.5)
plt.xlim(0.01, 0.18)
plt.ylim(0.007, 0.105)
plt.xlabel('B(t)')
plt.ylabel('B(t+1) - B(t)')
plt.grid(True)
plt.show()

#%%


#%%
#  Figura 5 
# Gráfica de cambio en densidad de bacterias contra densidad.
# comparación de la estimación con lo observado

t = [0, 1, 2, 3, 4, 5]
Bt = [0.022, 0.036, 0.060, 0.101, 0.169, 0.266]
Btest = 0.022 * np.power((5./3),t)

plt.plot(t, Bt, 'ro',  marker='o', markersize=8, color="red", 
              label='Dens. Obs.')
plt.plot(t, Btest, 'ro', marker='x', mew=2, markersize=8, color="blue", 
         label='Dens. Est.')
plt.legend(loc='upper left')
plt.xlim(-0.3, 5.3)
plt.ylim(0.007, 0.3)
plt.xlabel(r'$t$')
plt.ylabel(r'$B_t$')
plt.grid(True)
plt.show()
#%%

#%%
#  Figura 6 
# Gráfica de cambio en densidad de bacterias contra densidad.
# con ajuste de parabola

t = np.array([0, 1, 2, 3, 4, 5])
Bt = np.array([0.022, 0.036, 0.060, 0.101, 0.169, 0.266])
Bt_parab = 0.0236 + 0.000186*t + 0.00893*t**2
plt.plot(t, Bt, 'ro',  marker='o', markersize=8, color="red", 
              label='Dens. Obs.')
plt.plot(t, Bt_parab, color="blue", 
         label='Parabola')
plt.legend(loc='upper left')
plt.xlim(-0.3, 5.3)
plt.ylim(0.007, 0.3)
plt.xlabel(r'$t$')
plt.ylabel(r'$B_t$')
plt.grid(True)
plt.show()
#%%


#%%
#  Figura 7 
# Gráficas de intensidad de luz en el agua.
# 

d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
Id = np.array([0.400, 0.330, 0.270, 0.216, 0.170, 0.140, 0.124, 0.098,
               0.082, 0.065])
plt.plot(d, Id, 'ro',  marker='o', markersize=8, color="red")
plt.xlim(-0.5, 9.5)
plt.ylim(0.0, 0.45)
plt.xlabel(r'$d$')
plt.ylabel(r'$I_d$')
plt.grid(True)
plt.show()
#%%


#%%
#  Figura 8 
# Gráficas de cambio de intensidad de luz en el agua.
# 

Id = np.array([0.400, 0.330, 0.270, 0.216, 0.170, 0.140, 0.124, 0.098,
               0.082])
Idi = np.array([-0.070, -0.060, -0.054, -0.046, -0.030, -0.016, -0.026,
                -0.016, -0.017])
plt.plot(Id, Idi, 'ro',  marker='o', markersize=8, color="red")
plt.xlim(0.05, 0.45)
plt.ylim(-0.08, -0.01)
plt.xlabel('I(d)')
plt.ylabel('I(d+1)-I(d)')
plt.grid(True)
plt.show()
#%%


#%%
#  Figura 9 
# Gráficas de cambio de intensidad de luz en el agua.
# Con linea recta
# 

Id = np.array([0.400, 0.330, 0.270, 0.216, 0.170, 0.140, 0.124, 0.098,
               0.082])
Idi = np.array([-0.070, -0.060, -0.054, -0.046, -0.030, -0.016, -0.026,
                -0.016, -0.017])
plt.plot(Id, Idi, 'ro',  marker='o', markersize=8, color="red")
plt.plot([0,0.4],[0,-0.072], color="blue", linewidth=1.5)
plt.xlim(0.05, 0.45)
plt.ylim(-0.08, -0.01)
plt.xlabel('I(d)')
plt.ylabel('I(d+1)-I(d)')
plt.grid(True)
plt.show()
#%%

#%%
#  Figura 10 
# Gráficas de comparación de intensidad de luz observada
# y estimada
# 

d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
Id = np.array([0.400, 0.330, 0.270, 0.216, 0.170, 0.140, 0.124, 0.098,
               0.082, 0.065])
Id_est = 0.4 * 0.82 ** d
plt.plot(d, Id, 'ro',  marker='o', markersize=8, color="red", label='Id Obs.')
plt.plot(d, Id_est, 'ro', marker='x', mew=2, markersize=8, color="blue", 
         label='Id Est.')
plt.legend()
plt.xlim(-0.5, 9.5)
plt.ylim(0.03, 0.43)
plt.xlabel(r'$d$')
plt.ylabel(r'$I_d$')
plt.grid(True)
plt.show()
#%%

#%%
#  Figura 11 
# Gráfica de densidad de bacterias con tiempos de duplicado y de reducción
# a la mitad.

tt = np.array([0, 16, 35, 48, 64, 80])
Bt = np.array([0.022, 0.036, 0.060, 0.101, 0.169, 0.266])
vt = np.arange(0, 80, 1.)
Bvt = 0.022 * 1.032 ** vt
plt.plot(tt, Bt, 'ro',  marker='o', markersize=8, color="red")
plt.plot(vt, Bvt, color="blue")
plt.plot([26,48,70], [0.05,0.1,0.2], 'ro', marker='x', mew=2, markersize=14, 
         color="black", label='Dens. Est.')
plt.xlim(-5, 85)
plt.ylim(0, 0.3)
plt.xlabel(r'$t$')
plt.ylabel(r'$B_t$')
plt.grid(True)
plt.show()
#%%


#%%
#  Figura 12 
# Gráficas de intensidadad de luz con tiempos de reducción a la mitad
# 
# 

d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
Id = np.array([0.400, 0.330, 0.270, 0.216, 0.170, 0.140, 0.124, 0.098,
               0.082, 0.065])
vd = np.arange(0,9,0.1)
Id_vt = 0.4 * 0.82**vd
plt.plot(d, Id, 'ro',  marker='o', markersize=8, color="red", label='Id Obs.')
plt.plot(vd, Id_vt, color="blue")
plt.plot([0,3.5,7],[0.4,0.2,0.1], 'ro', marker='x', mew=2, markersize=14, 
         color="black")
plt.xlim(-0.5, 9.5)
#plt.ylim(0.03, 0.43)
plt.xlabel(r'$d$')
plt.ylabel(r'$I_d$')
plt.grid(True)
plt.show()
#%%




