import random
import math
import pylab
import os, random
from sys import exit 
import cmath
import numpy as np

def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    if fname != '': pylab.savefig(fname)
    pylab.show()
    pylab.close()


def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

def initial_config(N,eta):
    filename = 'disk_configuration_N%i_eta%.2f.txt' % (N,eta)
    if os.path.isfile(filename):
        f = open(filename, 'r')
        L = []
        for line in f:
            a, b = line.split()
            L.append([float(a), float(b)])
        f.close()
        print 'starting from file', filename
    else:
        N_sqrt = int(math.sqrt(N))
        delxy = 1./(2*N_sqrt)
        two_delxy = 2*delxy
        L = [[delxy+i*two_delxy,delxy+j*two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]
        print 'starting from a new configuration (square lattice)'
    # save configuration
    f = open(filename, 'w')
    for a in L:
       f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
    f.close()

    return L

def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

def Psi_6(L, sigma):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist(L[i], L[j]) < 2.8 * sigma and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0:
            vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)



etaList = np.arange(0.4,0.8,0.02)[::-1]
eta = etaList[0]

N = 64
L = initial_config(N,etaList[0])
sigma_sq = eta/(len(L)*math.pi)
sigma = math.sqrt(sigma_sq)

n_steps = 1000

pa = np.zeros(etaList.shape[0])
for i,eta in enumerate(etaList):
    print i,eta
    sigma_sq = eta/(len(L)*math.pi)
    sigma = math.sqrt(sigma_sq)
    delta = 0.2*sigma
    for steps in range(n_steps):
	for smallstep in range(100):
            a = random.choice(L)
            b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
            min_dist = min( dist(b,c) for c in L if c!=a)
            if not (min_dist < 2.0 * sigma):
		b = [b[0]%1.,b[1]%1.]
                a[:] = b
        Psi = Psi_6(L,sigma)
	pa[i] +=  abs(Psi)/n_steps

    show_conf(L,sigma,str(eta),'')
np.savetxt('pa.txt',pa)

pylab.plot(etaList,pa)
pylab.xlabel(r"$\eta$")
pylab.ylabel(r"$|\Psi_6|$")
pylab.xlim([min(etaList),max(etaList)])
pylab.legend()
pylab.show()


