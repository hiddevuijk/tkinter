import numpy as np
import matplotlib.pyplot as plt
from sys import exit


def u_lj(r,sigma,epsilon):
	a = (sigma/r)**6
	return 4*epsilon*a*(a-1)

def u_exp(r,sigma,epsilon):
	return epsilon*np.exp(-(r/sigma)**8)
def u(r,sigma,epsilon):
	return u_exp(r,sigma,epsilon)


def g0(r,kT,sigma,epsilon,Nxi):
	xiList = np.linspace(0,1,Nxi)
	return np.asarray([ np.exp(-xi*u(r,sigma,epsilon)/kT) for xi in xiList])


def next_g(g,rho,kT,sigma,epsilon,rmax,N):
	ng = np.zeros((N,N))

	RList = np.linspace(0.,10,N)
	
	xiList = np.linspace(0,1,N)
	dxi = xiList[1]-xiList[0]

	rList = np.linspace(0,rmax,N)
	dr = rList[1]-rList[0]

	for xi_i,xi in enumerate(xiList):
		for R_i,R in enumerate(RList):
			if R_i == 0: continue

			xipList = np.linspace(0,xi,N)
			dxip = xipList[1]-xipList[0]
			for xip_i,xip in enumerate(xipList):
	
				Ir = 0.
				for r_i,r in enumerate(rList):

					Is = 0
					sList = np.linspace(abs(R-r),R+r,N)
					ds = sList[1]-sList[0]
					for s_i,s in enumerate(sList):
						Is += ds*s*u(s,sigma,epsilon)*g[xip_i][s_i]
					
					Ir += dr*r*(g[-1][r_i]-1)*Is

				ng[xip_i,R_i] = dxip*(2*np.pi*rho/R)*Ir
				if xip_i > 0:
					ng[xip_i,R_i] += ng[xip_i-1,R_i]	
		
		for R_i,R in enumerate(RList):
			for xi_i,xi in enumerate(xiList):
				ng[xi_i][R_i] = np.exp(-(xi*u(R,sigma,epsilon)+ng[xi_i][R_i])/kT)
	return np.asarray(ng)

N = 10
eta = 0.2
rmax = 2
kT = 1.
sigma = 1.
epsilon = 50.
rho = 0.0
x = np.linspace(0,rmax,N)
y = g0(x,1.,1.,1.,N)

xiList = np.linspace(0,1,N)
xiplt = [0,1,9]
for i in xiplt:
	plt.plot(x,y[i],label=xiList[i])
plt.legend()
plt.show()

for i in range(3):
		y = (1-eta)*y+eta*next_g(y,rho,kT,sigma,epsilon,rmax,N)
for i in xiplt:
	plt.plot(x,y[i],label=xiList[i])
plt.legend()
plt.show()




