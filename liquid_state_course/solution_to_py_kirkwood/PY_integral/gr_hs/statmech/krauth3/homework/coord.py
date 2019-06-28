from cmath import *

def psi6(L):
	psi = 0+0j
	for n in L:
		psi += exp(6j*n*2*pi/360.)
	return psi/len(L)

La0 = 0.
Lb0 = 30.
Lc0 = 15.

La = []
Lb = []
Lc = []
for n in range(6):
	La.append(La0+60*n)
	Lb.append(Lb0+60*n)
	Lc.append(Lc0+60*n)

print(psi6(La))
print(psi6(Lb))
print(psi6(Lc))
print(psi6(La)+psi6(Lb))

