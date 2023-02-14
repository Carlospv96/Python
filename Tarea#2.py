import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

d=np.array([0,1,2,3,4,5,6,7,8])
Id=np.array([0.842,0.639,0.459,0.348,0.263,0.202,0.154,0.114,0.085])
Id_est=0.842 * 0.73 ** d
plt.plot(d,Id,'ro', marker='o', markersize=8, color="red", label='Id Obs.')
plt.plot(d, Id_est, 'ro', marker='x', mew=2, markersize=8, color="blue", 
         label='Id Est.')
plt.legend()
plt.xlabel(r'$d$')
plt.ylabel(r'$I_{d}$')
plt.grid(True)
plt.show()
