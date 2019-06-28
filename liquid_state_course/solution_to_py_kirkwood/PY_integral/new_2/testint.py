import numpy as np
import matplotlib.pyplot as plt
from sys import exit
from scipy.integrate import cumtrapz

N = 1000
xm = 10.

x = np.linspace(0,xm,N)

integrant = np.asarray([3*(t**2) for t in x])

y_int = cumtrapz(integrant,x,initial=0)
plt.plot(x,y_int)
plt.show()


