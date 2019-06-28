import numpy as np

from py_solution import *
from potentials import *


# physical parameters
rho = .5
T = 1.
r_co = 2.**(1./6.)

#integration parameters
a = 0.5
R = 50.
N = -1+2**14
maxit = 50000
eps_conv = 1.e-6
use_prev = False

# vector with r values, start at dr
dr = R/(N-1)
r = np.linspace(dr,R+dr,N)
#vector with k values
k = np.linspace(np.pi/R,np.pi*N/R,N)

# the f function
# functions to initialize are located in
# potentials.py

#f = get_f_hs(r)
f = get_f_LJ(T,r,r_co)

# k times the FT of rd
kD = np.zeros(N)
# r times the direct correlation function
rc = np.zeros(N)
# k times the FT of rc
kC = np.zeros(N)
# m the m function
m = np.zeros(N)


# step 1
# initial guess is all 0s
rd = np.zeros(N)
# or use the saved rd from a previous calculation
if use_prev:
	rd = np.loadtxt("rd.dat")

for i in range(maxit):
	# all the function in this loop are located in 
	# py_solution.py

	# step 2
	# get rc from rd and the PY approximation
	rc = rd2rc(f,rd,r)

	# step 3
	# Fourier transform rc to get kC
	kC = rc2kC(rc,r,N)
	
	# step 4
	# use kC and the OZ eq. in k-space
	# to get kD
	kD = kC2kD(kC,k,rho)

	# step5
	# Fourier transform kD back to r-space
	m = kD2rd(kD,r,N)
	
	# print error estimate every 500 iterations
	#if i%50==0: print i,eps(rd,m)
	if i%50==0: print(i,eps(rd,m))

	# step 6
	# check for convergence
	if eps(rd,m) < eps_conv:
		break

	# step 7
	# mix m with rd
	rd = a*rd + (1-a)*m

	if i == maxit-1:
		#print "Did not converge."
		print( "Did not converge.")
# step 8
# get h from rc and rd
h = rc_rd2h(rc,rd,r)

np.savetxt("rd.dat",rd)
np.savetxt("rc.dat",rc)
np.savetxt("h.dat",h)

np.savetxt("r.dat",r)

