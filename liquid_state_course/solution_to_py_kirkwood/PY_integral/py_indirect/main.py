import numpy as np
import matplotlib.pyplot as plt
from sys import exit
from scipy.fftpack import dst, idst

def ift(kF,r,k,N):
	return idst(kF)/(4*np.pi*2*N)
def ft(rf,r,k,N):
	return 4*np.pi*dst(rf)

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

def get_f(T,N,rmax):
	r = np.linspace(0,rmax,N)
	f = np.zeros(N)
	for i in range(1,N):
			f[i] = eu(r[i],T)-1
	return f

def hi2c(f,hi):
	return f*(hi+1)

def C2Hi(C,rho):
	return np.divide(C,1-rho*C)-C

def c2C(c,r,k,N):
	return ft(c,r,k,N)
def Hi2hi(Hi,r,k,N):
	return ift(Hi,r,k,N)
def c_hi2h(c,hi):
	return c+hi

a = 0.1
rho = 0.1
R = 30.
N = 300
n = 5
T=1.
dr = R/N
dk = np.pi/R

r = np.linspace(dr,R,N)
k = np.linspace(dk,np.pi*N/R,N)
hi = np.zeros(N)
hin = np.zeros(N)
Hi = np.zeros(N)
c = np.zeros(N)
C = np.zeros(N)
f = get_f(T,N,R)

for i in range(n):
	c = f*(hi+1)
	C = c2C(c,r,k,N)
	Hi = C2Hi(C,rho)
	hin = Hi2hi(Hi,r,k,N)
	hi = a*hi + (1-a)*hin


h = c_hi2h(c,hi)
plt.plot(r,h)
plt.show()





