import numpy as np
import matplotlib.pyplot as plt
from sys import exit
from scipy.integrate import trapz, simps

rho = 0.85
T = 1.128

r = np.loadtxt("r.dat")
dr = r[1]-r[0]
h = np.loadtxt("h.dat")
g = h+1
def up(r):
	return -(24/r)*((2./r**12)-(1./r**6))

def upr3(r):
	if r < 2.**(1./6)*1000:
			return -24*((2./r**10)-(1./r**4))
	else:
		return 0

i = int(np.floor(.3/dr))
print i,r[i]
r = r[i:]
g = g[i:]
I = np.zeros(r.shape[0])
for i,ri in enumerate(r):
		I[i] = g[i]*4*np.pi*upr3(ri)
p = rho*T-(rho*rho/6)*simps(I,r)
print p/(rho*T)


