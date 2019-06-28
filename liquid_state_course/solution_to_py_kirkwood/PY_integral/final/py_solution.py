import numpy as np
from scipy.fftpack import dst, idst

# the two discrete Fourier transformation
# with the correct normalization

def ft(rf,dr,N):
	norm = 2*np.pi*dr
	return norm*dst(rf,type=1)

def ift(kF,dr,N):
	norm = 1./(4*np.pi*(N+1)*dr)
	return norm*dst(kF,type=1)

	
def rd2rc(f,rd,r):
	rc = np.zeros(f.shape[0])
	rc[:-1] = f[:-1]*(rd[:-1]+r[1:])
	return rc

def kC2kD(kC,k,rho):
	kHi = np.zeros(kC.shape[0])
	kHi[:-1] = np.divide(kC[:-1],1-rho*np.divide(kC[:-1],k[1:]))-kC[:-1]
	return kHi

def rc2kC(rc,r,k,N):
	return ft(rc,r[1]-r[0],N)
def kD2rd(kD,r,k,N):
	return ift(kD,r[1]-r[0],N)

def rc_rd2h(rc,rd,r):
	h = np.zeros(rc.shape[0])
	h[:-1] = np.divide(rc[:-1]+rd[:-1],r[1:])
	return h

def eps(old,new):
	return np.sqrt(sum(d*d for d in (old-new)))



