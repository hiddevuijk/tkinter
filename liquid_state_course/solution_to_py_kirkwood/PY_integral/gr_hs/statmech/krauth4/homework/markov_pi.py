import random
import numpy as np
import matplotlib.pyplot as plt

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

d = 20
delta = 0.1 
x = np.zeros(d)
radius = 0
n_hits = 0
n_trials = 5000000
rList = []
for i in range(n_trials):
    dk = random.uniform(-delta, delta)
    k = random.randint(0,d-1)
    xk_old = x[k]
    xk_new = xk_old+dk
    new_radius = radius+xk_new**2 - xk_old**2

    if new_radius < 1.0:
	x[k] = xk_new
	radius = new_radius
    rList.append(np.sqrt(radius))
    alpha = random.uniform(-1.,1.)
    if   radius + alpha**2 < 1.0: n_hits += 1
Q =   2*n_hits / float(n_trials)

bins = np.linspace(0,1,100)
plt.hist(rList,bins=bins,normed=True)
x = np.linspace(0,1,100)
y = 20*x**19
plt.plot(x,y)

plt.show()






