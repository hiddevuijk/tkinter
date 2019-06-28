import math, random
import matplotlib.pyplot as plt

def rho_free(x, y, beta):    # free off-diagonal density matrix
    return math.exp(-(x - y) ** 2 / (2.0 * beta)) 

def V(x,c,q):
	return 0.5*x*x+c*x*x*x+q*x*x*x*x

def read_file(filename):
	lx = []
	ly = []
	with open(filename) as f:
		for line in f:
			x,y = line.split()
			lx.append(x)
			ly.append(y)
	return lx,ly

quartic = 1.
cubic = -quartic

c = cubic
q = quartic
beta = 4.0
N = 16                                             # number of slices
dtau = beta / N
delta = 1.0                                       # maximum displacement on one slice
n_steps = 1000000                                 # number of Monte Carlo steps
x = [0.0] * N                                     # initial path
k_sample = 0
hist_data = []
for step in range(n_steps):
    k = random.randint(0, N - 1)                  # random slice
    knext, kprev = (k + 1) % N, (k - 1) % N       # next/previous slices
    x_new = x[k] + random.uniform(-delta, delta)  # new position at slice k
    old_weight  = (rho_free(x[knext], x[k], dtau) *
                   rho_free(x[k], x[kprev], dtau) *
                   math.exp(-dtau * V(x[k],c,q)))
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-dtau*V(x_new,c,q)))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    if step%10 ==0:
	hist_data.append(x[k_sample])



plt.hist(hist_data,100,normed=True,label="path integral")
matrix_square_data = read_file('data_aharm_matrixsquare_beta4.0.dat')
plt.plot(matrix_square_data[0],matrix_square_data[1],'ro',label="mat. sq.")
plt.xlim([-2,2])
plt.xlabel('x')
plt.ylabel(r"$\rho$")
plt.legend()
plt.title("comparison between matrix squaring and path integration")
plt.show()






