import numpy as np
from sys import exit
def eu(r,r_co,T):
	a = (1./r)**6
	ac = (1./r_co)**6
	urco = 4*(ac*ac-ac)
	if r <r_co:
		return np.exp(urco/T-4*(a*a-a)/T)
	else:
		return 1

def get_f_LJ(T,r,r_co):
	N = r.shape[0]
	f = np.zeros(N)
	f[0] = -1
	for i in range(0,N):
			f[i] = eu(r[i],r_co,T)-1
	return f


def get_f_hs(r):
	f = np.zeros(r.shape[0])
	i = 0
	while r[i] < 1:
		f[i] = -1
		i += 1
	return f





