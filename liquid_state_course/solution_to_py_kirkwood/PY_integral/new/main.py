import numpy as np
import matplotlib.pyplot as plt
from sys import exit
from scipy.integrate import simps,cumtrapz,trapz,romb

def eu(r,T):
	a = (1./r)**6
	r0 = 2.**(1./6)
	r0 += 1.0
	a0 = (1./r0)**6
	r0u = 4*(a0*a0-a0)
	if r <r0:
		return np.exp(r0u/T-4*(a*a-a)/T)
	else:
		return 1

def get_e(T,N,rmax):
	r = np.linspace(0,rmax,N)
	e = np.zeros(N)
	for i in range(1,N):
			e[i] = eu(r[i],T)
	return e

def z2g(z,r,e):
	g = np.zeros(N)
	g[1:] = z[1:]*e[1:]/r[1:]
	return g
nit = 10
N = 2*250
T = 1.
rmax = 2*10
rho = .5
a = 0.01
e = get_e(T,N,rmax)

z = np.linspace(0,rmax,N)
zip1 = np.linspace(0,rmax,N)
r = np.linspace(0,rmax,N)
ds = r[1]-r[0]


def get_zpi(rho,e,z,r,N,ti):
	iterable = ((1-e[si])*z[si]*(e[si+ti]*z[si+ti]\
		+np.sign(si-ti)*e[abs(si-ti)]\
		*z[abs(si-ti)]-2*si*ds) for si in range(0,N/2))
	I = np.fromiter(iterable,float)
	return 1 - 2*np.pi*rho*trapz(I,r[:N/2])

def get_z(rho,e,z,r,N):
	iterable = (get_zpi(rho,e,z,r,N,ti)\
			for ti in range(0,N/2))
	I = np.fromiter(iterable,float)
	return cumtrapz(I,r[:N/2],initial=1)



for i in range(nit):
		if nit%10 == 0: print i,nit
		zip1[:N/2] = get_z(rho,e,z,r,N)
		z = (1-a)*z + a*zip1

g = z2g(z,r,e)
np.savetxt("r.dat",r)
np.savetxt("g.dat",g)
exit()
plt.plot(r,g,label="g"+str(nit))
plt.legend()
plt.xlim([0,rmax/2])
plt.show()




