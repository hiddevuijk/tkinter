import numpy as np
import matplotlib.pyplot as plt



# you only need to give the value of rho
rho = 0.9

######

# read the data from the numerical calculations
h = np.loadtxt("h.dat")
rd = np.loadtxt("rd.dat")
rc = np.loadtxt("rc.dat")
r = np.loadtxt("r.dat")

d = rd/r
c = rc/r


plt.plot(r,h,label="h(r)")
plt.plot(r,c,label="c(r)")
plt.plot(r,d,label="d(r)")


plt.xlim([0.5,10])
plt.ylim([-1.5,10.])
plt.legend()
plt.show()


