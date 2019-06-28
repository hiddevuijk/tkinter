import math, numpy
import matplotlib.pyplot as plt

# Free off-diagonal density matrix
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

# Harmonic density matrix in the Trotter approximation (returns the full matrix)
def rho_harmonic_trotter(grid, beta):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * 0.5 * (x ** 2 + xp ** 2)) \
                         for x in grid] for xp in grid])



def pi_quant(x,beta):
	a = math.sqrt(math.tanh(0.5*beta)/math.pi)
	return a*math.exp(-x*x*math.tanh(0.5*beta))

x_max = 2.5
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
beta_tmp = 2.0 ** (-1)                   # initial value of beta (power of 2)
beta     = 2.0 ** 2                      # actual value of beta (power of 2)
rho = rho_harmonic_trotter(x, beta_tmp)  # density matrix at initial beta
while beta_tmp < beta:
    rho = numpy.dot(rho, rho)
    rho *= dx
    beta_tmp *= 2.0


Z = sum(rho[j,j] for j in range(nx+1))*dx
pi_of_x = [ rho[j,j]/ Z for j in range(nx+1)]
f = open('data_harm_matrixsquare_beta'+str(beta)+'.dat','w')
for j in range(nx+1):
	f.write(str(x[j])+' '+str(rho[j,j]/Z)+'\n')
f.close()


plt.scatter(x,pi_of_x,label="mat. sq.")
plt.plot(x,[pi_quant(xi,beta) for xi in x],'-',label="analytical")

plt.legend()
plt.show()

