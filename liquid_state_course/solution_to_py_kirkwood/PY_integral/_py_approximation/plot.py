import numpy as np
import matplotlib.pyplot as plt


c = np.loadtxt("g.dat")
r = np.loadtxt("r.dat")
#plt.ylim([-10,10])
plt.plot(r,c)
plt.show()


