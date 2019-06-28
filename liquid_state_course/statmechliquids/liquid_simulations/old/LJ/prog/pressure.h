#ifndef GUARD_pressure_h
#define GUARD_pressure_h

#include "vecmanip.h"

double pressure(const std::vector<std::vector<double> >& r,
	double (*force)(const double&),
	double rho, double T,double L)
{

	double P = 0;
	int N = r.size();
	double rij;
	for(int i=0;i<N;++i) {
		for(int j=i+1;j<N;++j) {
			rij = distance_3d(r[i],r[j],L);
			P += f(rij)*rij;
		}
	}
	return T*rho + P/(3*L*L*L);

}







#endif
