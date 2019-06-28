import numpy as np
import matplotlib.pyplot as plt
from sys import exit
from scipy.integrate import simps,cumtrapz,trapz


def u(r):
	a = (1/r)**6
	return 4*(a*a-a)

def eu(r,T):
	a = (1/r)**6
	ur = 4*(a*a-a)
	if r < 2**(1./6):
		return np.exp(-4*(a*a-a)/T)
	else:
		return 0

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


N = 2*200
T = 2.
rmax = 2*10
rho = 0.1
a = 0.01
e = get_e(T,N,rmax)
z = np.linspace(0,rmax,N)
zip1 = np.linspace(0,rmax,N)
r = np.linspace(0,rmax,N)









