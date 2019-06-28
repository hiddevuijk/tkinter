import random
import numpy as np


x, y=  0.0, 0.0
delta = 0.1
n_trials = 10000000
n_hits = 0
for i in range(n_trials):
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    if (x + del_x)**2 + (y + del_y)**2 < 1.0:
        x, y = x + del_x, y + del_y
    z = random.uniform(-1.,1.)
    if x**2 + y**2 + z**2  < 1.0: n_hits += 1
Q3 =  2*n_hits / float(n_trials)

print "Q(3) = " , Q3
 
x, y, z= 0.0, 0.0, 0.0
delta = 0.1
n_trials = 10000000
n_hits = 0

for i in range(n_trials):
    del_x, del_y, del_z = random.uniform(-delta, delta), random.uniform(-delta, delta), random.uniform(-delta,delta)
    if (x + del_x)**2 + (y + del_y)**2 + (z+del_z)**2< 1.0:
        x, y,z = x + del_x, y + del_y, z+del_z
    alpha = random.uniform(-1.,1.)
    if x**2 + y**2 + z**2 + alpha**2 < 1.0: n_hits += 1
Q4 = 2*n_hits / float(n_trials)


print "Q(4) =", Q4

print '\n'

print "V_sph(4)           = "
print "pi^2/2             = ", 0.5*(np.pi**2)
print "V_sph(3)*Q(4)      = ", (4*np.pi/3)*Q4
print "V_sph(2)*Q(3)*Q(4) = ", np.pi*Q3*Q4




