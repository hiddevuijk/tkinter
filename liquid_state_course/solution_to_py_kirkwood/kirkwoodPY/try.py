import numpy as np
import matplotlib.pyplot as plt
from sys import exit



def u(r,sigma,epsilon):
	a = (sigma/r)**6
	return 4*epsilon*a*(a-1)

r = 0.3
sigma = 1.
epsilon = 1.

print u(r,sigma,epsilon)*np.exp(-u(r,sigma,epsilon))


