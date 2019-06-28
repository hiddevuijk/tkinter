import numpy as np

from py_solution import *
from potentials import *


# physical parameters
rho = .85
R = 50.
T = 1.128
r_co = 2.**(1./6.)
#integration parameters
a = 0.9
N = -1+2**14
maxit = 50000
eps_conv = 1.e-12
use_prev = True

# vector with r values
# functions are shifted f(r[i]) = f[i-1] !!
# also in k-space
r = np.linspace(0,R,N)

#vector with k values
k = np.linspace(0,np.pi*N/R,N)

# the f function
# functions to initialize are located in
# potentials.py

#f = get_f_hs(r)
f = get_f_LJ(T,r,r_co)


# m the m function
m = np.zeros(N)


# r times the indirect correlation function
# initial guess is all 0s
# step 1
rd = np.zeros(N)
# or use the saved rd from a previous calculation
if use_prev:
	rd = np.loadtxt("rd.dat")


# k times the FT of rd
kD = np.zeros(N)

# r times the direct correlation function
rc = np.zeros(N)

# k times the FT of rc
kC = np.zeros(N)

iterations = 0
for i in range(maxit):
	# all the function in this loop are located in 
	# py_solution.py

	# step 2
	# get rc from rd and the PY approximation
	rc = rd2rc(f,rd,r)

	# step 3
	# Fourier transform rc to get kC
	kC = rc2kC(rc,r,k,N)
	
	# step 4
	# use kC and the OZ eq. in k-space
	# to get kD
	kD = kC2kD(kC,k,rho)

	# step5
	# Fourier transform kD back to r-space
	m = kD2rd(kD,r,k,N)
	
	# step 6
	# mix m with rd
	rd = a*rd + (1-a)*m


	# print error estimate every 500 iterations
	if i%500==0: print i,eps(rd,m)
	# step 7
	# check for convergence
	if eps(rd,m) < eps_conv:
		break

	iterations += 1

# get h from rc and rd
h = rc_rd2h(rc,rd,r)

np.savetxt("rd.dat",rd)
np.savetxt("rc.dat",rc)
np.savetxt("h.dat",h)

# shift r to r+dr such that f(r) = f(r[i])
dr = R/(N-1)
np.savetxt("r.dat",r+dr*np.ones(N))

