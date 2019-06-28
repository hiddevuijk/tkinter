import numpy as np
from scipy.fftpack import fft, ifft
from sys import exit



import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from sys import exit


def u(r):
	a = r**(1./6)
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

a= 0.0
n = 1
rmax = 20
rmin = 0.1
N = 1000
rho = 0.1
T = 1.
r = np.linspace(0,rmax,N)
e = get_e(r,rmin,T)
f = get_f(r,rmin,T)

h = get_f(r,rmin,T)
hn = np.copy(h)

for i in range(n):
	h = np.copy(hn)
	c = np.multiply(f,h+1)
	#c = np.multiply(c,1/e)
	ck = fft(c)
	hk = np.multiply(ck,1./(1-rho*ck))

	hn = (1-a)*h + a*ifft(hk)

plt.plot(r,hn)
plt.show()














