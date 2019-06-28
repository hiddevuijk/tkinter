from __future__ import print_function
import math, numpy
import matplotlib.pyplot as plt

def_x_max = 5.0
def_nx = 100

def pi_quant(x, beta):
    return (math.sqrt(math.tanh(beta / 2) / math.pi) * 
            math.exp(-(x ** 2) * math.tanh(beta / 2)))

# Free off-diagonal density matrix
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

# Harmonic density matrix in the Trotter approximation (returns the full matrix)
def rho_harmonic_trotter(grid, beta):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * 0.5 * (x ** 2 + xp ** 2)) \
                         for x in grid] for xp in grid])

x_max = 5.
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
beta_tmp = 2.**(-5)
beta = 2.** 8 
rho = rho_harmonic_trotter(x, beta_tmp)  # density matrix at initial beta

# Print initial density matrix to see that it is approximately diagonal
print('density matrix at beta = ', beta_tmp)
for i in range(nx + 1):
    for j in range(nx + 1):
        aeee=1#print("{0:.3f}".format(rho[i, j]), end=' ')
    #print(end='\n')

while beta_tmp < beta:
    rho = numpy.dot(rho, rho)
    rho *= dx
    beta_tmp *= 2.0
    #print('beta: %s -> %s' % (beta_tmp / 2.0, beta_tmp))

Z = sum(rho[j, j] for j in range(nx + 1)) * dx
pi_of_x = [rho[j, j] / Z for j in range(nx + 1)]
f = open('data_harm_matrixsquaring_beta' + str(beta) + '.dat', 'w')
for j in range(nx + 1):
    f.write(str(x[j]) + ' ' + str(rho[j, j] / Z) + '\n')
f.close()

plt.plot(x, pi_of_x, 'x',
         x, [pi_quant(xi, beta) for xi in x], '-')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.legend(['Matrix squaring', 'Analytical, Quantum'])
plt.title(r'Matrix squaring: 1D harmonic oscillator, $\beta = ' + str(beta)
           + r'$')
plt.grid()
plt.show()
