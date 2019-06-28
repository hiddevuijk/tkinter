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
	return f*(rd+r)

def kC2kD(kC,k,rho):
	return np.divide(kC,1-rho*np.divide(kC,k))-kC

def rc2kC(rc,r,N):
	return ft(rc,r[1]-r[0],N)
def kD2rd(kD,r,N):
	return ift(kD,r[1]-r[0],N)

def rc_rd2h(rc,rd,r):
	return np.divide(rc+rd,r)

def eps(old,new):
	return np.sqrt(sum(d*d for d in (old-new)))



