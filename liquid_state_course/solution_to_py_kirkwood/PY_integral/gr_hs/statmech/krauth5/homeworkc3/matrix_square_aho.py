import math, numpy
import matplotlib.pyplot as plt

# Free off-diagonal density matrix
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

def rho_harmonic_trotter(grid, beta):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * 0.5 * (x ** 2 + xp ** 2)) \
                         for x in grid] for xp in grid])

def V(x,cubic,quartic):
	return 0.5*x*x + cubic*x*x*x+ quartic*x*x*x*x
def rho_a_trotter(grid, beta,c,q):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta *(V(x,c,q)+ V(xp,c,q))) \
                         for x in grid] for xp in grid])


def pi_quant(x,beta):
	a = math.sqrt(math.tanh(0.5*beta)/math.pi)
	return a*math.exp(-x*x*math.tanh(0.5*beta))


def Epert(n,c,q):
	return n+0.5-15./4.*c**2*(n**2+n+11./30) \
		+3./2. *q*(n**2+n+0.5)
def Zpert(c,q,beta,n_max):
	return sum(math.exp(-beta*Epert(n,c,q)) for n in range(n_max+1))

x_max = 5.
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
beta_tmp = 2.0 ** (-6)                   # initial value of beta (power of 2)
beta     = 2.0 ** 2                      # actual value of beta (power of 2)

for q in [0.001,0.01,0.1,0.2,0.3,0.4,0.5]:
	c=  -q
	rho = rho_a_trotter(x, beta_tmp,c,q)  # density matrix at initial beta
	while beta_tmp < beta:
	    rho = numpy.dot(rho, rho)
	    rho *= dx
	    beta_tmp *= 2.0


        Z_q = sum(rho[j,j] for j in range(nx+1))*dx
	Zpert_q = 0
	try:
		Zpert_q = Zpert(c,q,beta,50)
		print q,Z_q,Zpert_q,abs(Z_q-Zpert_q)
	except:
		print q,Z_q,'inf','inf'
