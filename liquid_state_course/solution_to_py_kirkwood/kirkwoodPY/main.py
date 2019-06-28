import numpy as np
import matplotlib.pyplot as plt
from sys import exit

def u_hs(r,sigma,epsilon):
	if r<sigma: return epsilon
	else: return 0
def u_ljc(r,sigma,epsilon):
	if r > 2**(1./6):
		return 0
	else:
		a = (sigma/r)**6
		return epsilon+4*epsilon*a*(a-1)

def u_lj(r,sigma,epsilon):
	a = (sigma/r)**6
	return 4*epsilon*a*(a-1)


def u_exp(r,sigma,epsilon):
	return epsilon*np.exp(-(r/sigma)**8)
def u(r,sigma,epsilon):
	return u_ljc(r,sigma,epsilon)


def g0(rList,kT,sigma,epsilon):
	xiList = np.linspace(0,1,len(rList))
	g0 = np.zeros((len(rList),len(rList)))
	for r_i,r in enumerate(rList):
		for xi_i,xi in enumerate(xiList):
			if r>=rmin:
				g0[xi_i][r_i] = np.exp(-xi*u(r,sigma,epsilon)/kT)
			elif xi_i==0:
				g0[xi_i][r_i] = 1
			else:
				g0[xi_i][r_i] = 0
	return g0

def next_g(g,rho,kT,sigma,epsilon,rmin,rmax,N):
	ng = np.zeros((N,N))

	RList = np.linspace(0,rmax,N)
	
	xiList = np.linspace(0,1,N)
	dxi = xiList[1]-xiList[0]

	rList = np.linspace(0,rmax,N)
	dr = rList[1]-rList[0]
	xipList = np.linspace(0,1,N)
	dxip = xipList[1]-xipList[0]
	for xip_i,xip in enumerate(xipList):
		if xip_i < 1: continue
	
		for R_i,R in enumerate(RList):
			if R_i == 0: continue


			Ir = 0.
			for r_i,r in enumerate(rList):
				s = abs(R-r)
				s_max = min(R+r,rmax)
				si_max = int(s_max/dr)
				s_i = int(s/dr)
			
				Is = 0
				while s_i<si_max:
					if abs(s) > rmin:
						Is += dr*s*u(s,sigma,epsilon)*g[xip_i][s_i]
						s_i += 1
						s += dr
					else:
						s_i += 1
						s += dr
				Ir += dr*r*(g[-1][r_i]-1)*Is

			ng[xip_i][R_i] = dxip*(2*np.pi*rho/R)*Ir
			if xip_i > 0:
				ng[xip_i][R_i] += ng[xip_i-1][R_i]	
	for R_i,R in enumerate(RList):
		for xi_i,xi in enumerate(xiList):
				if xi_i ==0:
					ng[xi_i][R_i] = 1.
				elif R<rmin:
					ng[xi_i][R_i] = 0.
				else:
					#print R,u(R,sigma,epsilon),ng[xi_i][R_i]
					ng[xi_i][R_i] = np.exp(-(xi*u(R,sigma,epsilon)+ng[xi_i][R_i])/kT)
	return np.asarray(ng)

N = 50
eta = 1.
rmin = 0.6
rmax = 2.
kT = 1.
sigma = 1.
epsilon = 1.
rho = .1
x = np.linspace(0,rmax,N)
y = g0(x,kT,sigma,epsilon)

xiList = np.linspace(0,1,N)
xiplt = [0,1,int(N/2)-1,N-1]
for i in xiplt:
	plt.plot(x,y[i],label=xiList[i])

plt.legend()
plt.show()
for i in range(1):
	print i
	y = (1-eta)*y+eta*next_g(y,rho,kT,sigma,epsilon,rmin,rmax,N)

for i in xiplt:
	plt.plot(x,y[i],label=xiList[i])

plt.legend()
plt.show()





