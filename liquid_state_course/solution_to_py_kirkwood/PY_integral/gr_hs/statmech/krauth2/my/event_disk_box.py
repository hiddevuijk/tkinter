import numpy as np
import math

def wall_time(x,v,sigma):
	if v > 0.0:
		return (1.-sigma0-x)/v
	elif v < 0.:
		return (x-sigma)/abs(v)
	else:
		return float('inf')

def pair_time_vec(xa,va,xb,vb,sigma):
	dx = xb-xa
	dv = vb-va
	dxdv = np.inner(dx,dv)
	D = dxdv**2  - np.inner(dv,dv)*(np.inner(dx,dx) - 4*sigma*sigma)
	if D>0 and dxdv < 0:
		return -(dxdv + np.sqrt(D))/np.inner(dv,dv)
	else:
		return float('inf')
def pair_time(pos_a, vel_a, pos_b, vel_b, sigma):
    del_x = [pos_b[0] - pos_a[0], pos_b[1] - pos_a[1]]
    del_x_sq = del_x[0] ** 2 + del_x[1] ** 2
    del_v = [vel_b[0] - vel_a[0], vel_b[1] - vel_a[1]]
    del_v_sq = del_v[0] ** 2 + del_v[1] ** 2
    scal = del_v[0] * del_x[0] + del_v[1] * del_x[1]
    Upsilon = scal ** 2 - del_v_sq * ( del_x_sq - 4.0 * sigma **2)
    if Upsilon > 0.0 and scal < 0.0:
        del_t = - (scal + math.sqrt(Upsilon)) / del_v_sq
    else:
        del_t = float('inf')
    return del_t


