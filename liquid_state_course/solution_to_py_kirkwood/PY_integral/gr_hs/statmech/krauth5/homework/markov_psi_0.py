import random, math
import matplotlib.pyplot as plt
import numpy as np

def psi_0_sq(x):
	return (math.pi**(-1./2))*math.exp(-0.5*x**2)**2

def psi_n_sq(x,n):
	if n == -1:
		return 0.0
	else:
		psi = [math.exp(-x*x/2.)/(math.pi**0.25)]
		psi.append(math.sqrt(2.)*x*psi[0])
		for k in range(2,n+1):
			psi.append(math.sqrt(2./k)*x*psi[k-1] - math.sqrt((k-1.)/k)*psi[k-2])
	return psi[n]**2

def pi_quant(x):
	a = math.sqrt(math.tanh(0.5*beta)/math.pi)
	return a*math.exp(-x*x*math.tanh(0.5*beta))
def pi_class(x):
	a = math.exp(-beta*x*x/2.)
	return a*math.sqrt(beta/(2.*math.pi))	

beta = 500.
x = 0.0
delta = 0.5
n=0
xList = []
for k in range(1000000):
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) < psi_n_sq(x_new,n)/psi_n_sq(x,n): 
        x = x_new 
    xList.append(x)

    n_new = n + random.choice([-1,1])
    if random.uniform(0.0,1.0) < \
	psi_n_sq(x_new,n_new)/psi_n_sq(x,n)*math.exp(-beta*(n_new-n)) and n_new>=0:
	n = n_new
xList = np.asarray(xList)

plt.hist(xList,normed=True,bins=35,label="markov chain")


xm = 1.2*max(np.absolute(xList))
y = np.linspace(-xm,xm,1000)
py = np.zeros(1000)
for i,yi in enumerate(y):
	py[i] = pi_quant(yi)

plt.plot(y,py,label=r"$exact quantum$")

for i,yi in enumerate(y):
	py[i] = pi_class(yi)

plt.plot(y,py,label=r"$exact classical $")

plt.title(r"$\beta="+str(beta)+"$")
plt.xlabel(r'$x$')
plt.xlim([-xm,xm])
plt.legend()
plt.show()

