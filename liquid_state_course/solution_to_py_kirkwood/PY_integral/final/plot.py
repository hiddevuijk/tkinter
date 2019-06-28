import numpy as np
import matplotlib.pyplot as plt
import sys


# exact solution of the PY eq. 
# for g(1+)
def g1(rho):
	n = rho*np.pi/6.
	return (1+0.5*n)/((1-n)**2)

if len(sys.argv) > 1:
	rho = float(sys.argv[1])	
	plt.scatter(1,g1(rho)-1)

r = np.loadtxt("r.dat")
h = np.loadtxt("h.dat")
rd = np.loadtxt("rd.dat")
rc = np.loadtxt("rc.dat")
d = rd/r
c = rc/r


plt.axhline(0.,color="black")
plt.plot(r,d,label='d(r)')
plt.plot(r,c,label='c(r)')
plt.plot(r,h,label='h(r)')
plt.xlim([0,4])
plt.legend()
plt.show()




