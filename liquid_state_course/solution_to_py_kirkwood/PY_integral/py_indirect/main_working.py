import numpy as np
import matplotlib.pyplot as plt
from sys import exit
from scipy.fftpack import dst, idst
np.random.seed(123456)
N = -1+2*10
R = 10.
dr = R/(N-1)
r = np.linspace(0,10,N)
y = np.sin(r)+0.5*np.random.randn(N)



def ift(kF,dr,N):
	norm = 1./(4*np.pi*(N+1)*dr)
	return norm*dst(kF,type=1)
	#return idst(kF,type=2,norm="ortho")/(4*np.pi)
	#return idst(kF,type=3,norm="ortho")/(4*np.pi)
	
def ft(rf,dr,N):
	nor = 2*np.pi*dr
	return nor*dst(rf,type=1)
	#return 4*np.pi*dst(rf,type=2,norm="ortho")
	#return 4*np.pi*dst(rf,type=3,norm="ortho")



def eu(r,T):
	a = (1./r)**6
	r0 = 2.**(1./6)
	r0 += 1000.
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
			if r[i]<1:
				f[i] = -1
			else:
				f[i] = 0
			#f[i] = eu(r[i],T)-1
	return f

def rhi2rc(f,rhi,r):
	return f*(rhi+r)

def kC2kHi(kC,k,rho):
	kHi = np.zeros(kC.shape[0])
	kHi[1:] = np.divide(kC[1:],1-rho*np.divide(kC[1:],k[1:]))-kC[1:]
	return kHi

def rc2kC(rc,r,k,N):
	return ft(rc,r[1]-r[0],N)
def kHi2rhi(kHi,r,k,N):
	return ift(kHi,r[1]-r[0],N)

def rc_rhi2h(rc,rhi,r):
	h = np.zeros(rc.shape[0])
	h[1:] = np.divide(rc[1:]+rhi[1:],r[1:])
	return h

def eps(old,new):
	return np.sqrt(sum(d*d for d in (old-new)))


a = .9
rho = .6
R = 75.
N = -1+2**14
print N
n = 50000
T = 1.
dr = R/(N-1)
eps_conv = 1.e-5
r = np.linspace(0,R,N)
k = np.linspace(0,np.pi*N/R,N)

rhi = np.zeros(N)
rhin = np.zeros(N)
kHi = np.zeros(N)
rc = np.zeros(N)
kC = np.zeros(N)
f = get_f(T,N,R)
np.savetxt("h0.dat",f)
done = False
iterations = 0


read = True
if read == True:
	rh = np.loadtxt("h.dat")*r
	rc = np.loadtxt("rc.dat")
	rhi = rh-rc
for i in range(n):
	rc = rhi2rc(f,rhi,r)
	kC = rc2kC(rc,r,k,N)
	kHi = kC2kHi(kC,k,rho)
	rhin = kHi2rhi(kHi,r,k,N)
	if eps(rhi,rhin) < eps_conv:
		break

	if i%500==0: print i,eps(rhi,rhin)
	rhi = a*rhi + (1-a)*rhin
	iterations += 1
print iterations
h = rc_rhi2h(rc,rhi,r)

np.savetxt("rc.dat",rc)
np.savetxt("h.dat",h)
np.savetxt("r.dat",r)





