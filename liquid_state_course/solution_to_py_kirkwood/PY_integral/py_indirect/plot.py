import numpy as np
import matplotlib.pyplot as plt
from sys import exit

rho = .3
r = np.loadtxt("r.dat")
h = np.loadtxt("h.dat")
h0 = np.loadtxt("h0.dat")


def g1(rho):
	n = rho*np.pi/6.
	return (1+0.5*n)/((1-n)**2)

plt.scatter(1,g1(rho))



plt.plot(r,h+1,label="g")
plt.plot(r,h0+1,label="g0")
plt.legend()
plt.xlim([0,4])
plt.ylim([0,3.5])
plt.show()




