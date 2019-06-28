import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

rcf = 0.01
rmax = 100.
nr = 1024+1
maxit = 10



r = np.linspace(0,rmax,nr)
dr = r[1]-r[0]

def u(r,eps=1.,sigma=1.):
	if r < 2.**(1./6):
		sr6 = (sigma/r)**6
		return 4*eps*(sr6*sr6-sr6)
	else:
		return 0.;

def f(r,eps=1.,sigma=1.,beta=1.):
	if r<0.01:
		return -1.
	else:
		return np.exp(-1.*beta*u(r,eps,sigma)) -1.

zr = np.linspace(0,rmax,nr)
fr = np.zeros(nr)
for i in range(nr):
	fr[i] = f(r[i])


zr = np.linspace(0,rmax,nr)
zrnew = np.zeros(nr)

Ai = np.zeros(nr)

for it in range(maxit):

	fzr = np.multiply(zr,fr)
	A = fzr+zr-r

	for ri in range(nr):
		for ui in range(nr):
			lower = abs(r[ri]-u[ui])
			upper = r[ri] + u[ui]
			loweri = min(range(nr),key=lambda i: abs(r[i]-lower))
			upperi = min(range(nr),key=lambda i: abs(r[i]-upper))
			IA[ui] = integrate.romb(A[loweri:upperi],dx=dr)
		B = 	
					



