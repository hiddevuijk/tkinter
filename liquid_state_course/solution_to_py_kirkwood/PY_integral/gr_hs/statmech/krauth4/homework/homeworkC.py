import random
import numpy as np
import matplotlib.pyplot as plt
import math
from sys import exit

def mc_Q(d,n_trials,delta):
	x = np.zeros(d-1)
	radius = 0
	n_hits = 0
	for i in range(n_trials):
	    dk = random.uniform(-delta, delta)
	    k = random.randint(0,d-2)
	    xk_old = x[k]
	    xk_new = xk_old+dk
	    new_radius = radius+xk_new**2 - xk_old**2

	    if new_radius < 1.0:
		x[k] = xk_new
		radius = new_radius
	    alpha = random.uniform(-1.,1.)
	    if   radius + alpha**2 < 1.0: n_hits += 1
	return  2*n_hits / float(n_trials)

def V_sph(dim):
	return math.pi**(dim/2.)/math.gamma(dim/2. + 1)

d_max = 200
dimList = np.arange(1,d_max+1,1)

n_trials = 500000
d = 0.1

QList = []
VList = [2.]
VListTrue = [2.]
for i,dim in enumerate(dimList[1:]):
	Qd = mc_Q(dim,n_trials,d)
	QList.append(Qd)
	VList.append(VList[i]*Qd)
	VListTrue.append(V_sph(dim))
	if dim == 4:
		print "dim = ",dimList[i+1]
		print "V_sph("+str(dim)+") = ",VList[i+1]
		print "V true = " ,VListTrue[i+1]

	if dim == 200:
		print "dim = ",dimList[i+1]
		print "V_sph("+str(dim)+") = ",VList[i+1]
		print "V true = " ,VListTrue[i+1]


plt.plot(dimList,VList,color="blue",label="monte carlo")
plt.plot(dimList,VListTrue,color="red",label="true value")

plt.xlabel("dimension")
plt.ylabel(r"$V_{sphere}$")

plt.legend()
plt.yscale('log')
plt.show()



