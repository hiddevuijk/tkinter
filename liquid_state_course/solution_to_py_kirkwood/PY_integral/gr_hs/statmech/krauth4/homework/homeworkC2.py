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

def V(dim,n_trials,delta):
	v0 = 2
	dimi = 1
	while dimi<dim:
		v0 *=  mc_Q(dimi+1,n_trials,delta)
		dimi += 1
	return v0



dim  = 20
delta = 0.1


n_trials = [1,10,100,1000,10000,100000]

n_runs = 10



for i,n_trial in  enumerate(n_trials):
	m = 0.
	v = 0.

	for n in range(n_runs):
		vol =  V(dim,n_trial,delta)
		m += vol/n_runs
		v += vol*vol/n_runs
	s = np.sqrt(v-m*m)/np.sqrt(n_runs)

	print n_trial, "\t|", m, "\t|",V_sph(dim),"\t|",s,"\t|",abs(m-V_sph(dim))


