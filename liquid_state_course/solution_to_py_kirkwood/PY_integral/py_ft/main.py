import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from sys import exit


def u(r):
	a = (1./r)**(6)
	return 4*(a*a - a)


def get_e(r,rmin,T):
	e = np.zeros(r.shape[0])
	for ri,r in enumerate(r):
		if r<rmin: continue
		else:
			e[ri] = np.exp(-u(r)/T)
	return e

def get_f(r,rmin,T):
	return get_e(r,rmin,T)-np.ones(r.shape[0])
a= 0.99
n = 10
rmax = 20
rmin = 0.1
N = 1000
rho = 0.1
T = 1.
r = np.linspace(0,rmax,N)
e = get_e(r,rmin,T)
f = get_f(r,rmin,T)


y = np.ones(N)
yn = np.copy(y)
for i in range(n):
	y = np.copy(yn)
	fy = np.multiply(f,y)
	ey = np.multiply(e,y)

	fy_k = fft(fy)
	ey_k = fft(ey)

	eyfy_k = np.multiply(fy_k,ey_k)

	yn = a*y + (1-a)*np.real(1-rho*fy_k[0] + rho*ifft(eyfy_k))

y = yn
g = np.multiply(e,y)
plt.plot(r,g)
plt.show()





