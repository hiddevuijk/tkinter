import numpy as np
import matplotlib.pyplot as plt


# rho must be in rhoList
# T must be in TList
# because those are the values for which there
# is simulation data

rho = .05
T = 1.4
r_co = 2.**(1./6.)*1000

# set to true if a cutoff is used
cutoff = False


####
rhoList = [0.05,0.316,0.85]
TList = [0.9,1.,1.1,1.2,1.3,1.325,1.35,1.4]
rhoi = rhoList.index(rho)
Ti = TList.index(T)



# read data from numerical calculations
h = np.loadtxt("h.dat")
g = h+1
r = np.loadtxt("r.dat")

plt.plot(r,g,label="g(r) PY")


# read data from simulations
fname = "../LJ"
if cutoff:
	fname += "co"
fname += "/rho"+str(rhoi)+"_T"+str(Ti)+"_g.dat"


g_dat = np.loadtxt(fname)
r_dat = np.loadtxt("../LJ/r"+str(rhoi)+".dat")
plt.plot(r_dat,g_dat,label="g(r) sim")
plt.xlim([0,7])
plt.legend()
plt.show()







