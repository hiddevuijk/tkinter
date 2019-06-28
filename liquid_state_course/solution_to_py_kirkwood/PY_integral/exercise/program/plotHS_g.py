import numpy as np
import matplotlib.pyplot as plt

# you only need to give the value for rho
rho = 0.6


#####

#read data from numerical calculations
h = np.loadtxt("h.dat")
rd = np.loadtxt("rd.dat")
rc = np.loadtxt("rc.dat")
r = np.loadtxt("r.dat")

g = h+1
d = rd/r
c = rc/r

# read data from simulations
g_dat = np.loadtxt("../HS/rho0"+str(int(10*rho))+"_g.dat")
r_dat = np.loadtxt("../HS/r.dat")


plt.plot(r,g,label="g(r) PY")
plt.plot(r_dat,g_dat,label="g(r) sim")


# the analytical solution to th PY eq. for r=1.
def g1(rho):
	n = rho*np.pi/6.
	return (1+0.5*n)/((1-n)**2)

plt.scatter(1,g1(rho),label="g(1) analytical solution to PY")

plt.xlim([0,7])
plt.legend()
plt.show()


