import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz, simps

# the pressure for lennard jones particles
# from g and the pressure eq.

# u'(r)*r^3
def upr3(r,r_co):
	if r < r_co:
		return -24*((2./r**10)-(1./r**4))
	else:
		return 0

def pressure(g,r,r0,r_co,rho,T):
	dr = r[1] - r[0]
	i = int(np.floor(r0/dr))
	r = r[i:]
	g = g[i:]
	I = np.zeros(r.shape[0])
	for i, ri in enumerate(r):
			I[i] = g[i]*4*np.pi*upr3(ri,r_co)
	p = rho*T-(rho*rho/6)*simps(I,r)
	return p

T = 1.
rho = 0.85
r_co = 2.**(1./6.)*1000
r = np.loadtxt("r.dat")
h = np.loadtxt("h.dat")
g = h+1
r0 = 0.5
print(pressure(g,r,r0,r_co,rho,T))


