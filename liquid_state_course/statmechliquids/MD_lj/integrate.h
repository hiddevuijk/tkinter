#ifndef GUARD_integrate_h
#define GUARD_integrate_h


#include <vector>

#include "deriv.h"


void integrate(std::vector<std::vector<double> >& r,
	Deriv& deriv, double ti, double tf, double dt)
{
	while( (ti+dt) < tf){
		deriv(r,dt);
		ti += dt;
	}
	if(ti < tf)
		deriv(r,tf-ti);
}





#endif
