import numpy as np
import matplotlib.pyplot as plt

r = np.loadtxt("r.dat")
g3 = np.loadtxt("rho03_g.dat")
g6 = np.loadtxt("rho06_g.dat")
g9 = np.loadtxt("rho09_g.dat")


plt.plot(r,g3)
plt.plot(r,g6)
plt.plot(r,g9)

plt.show()


