import numpy as np
import matplotlib.pyplot as plt


def y(x):
	return 2*x*x


def z(x,y):
	return y(x)

print(z(2.,y))


