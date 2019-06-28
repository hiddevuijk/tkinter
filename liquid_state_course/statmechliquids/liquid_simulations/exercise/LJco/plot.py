import numpy as np
import matplotlib.pyplot as plt


r = np.loadtxt("r1.dat")
g = np.loadtxt("rho1_T0_g.dat")
p = np.loadtxt("rho1_T0_p.dat")

plt.title(str(np.mean(p))+" ("+str(np.std(p))+")")
plt.plot(r,g)
plt.show()


