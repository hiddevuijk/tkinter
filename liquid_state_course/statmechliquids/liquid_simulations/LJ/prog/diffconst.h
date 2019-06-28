#ifndef GUARD_diffconst_h
#define GUARD_diffconst_h

#include <vector>


#include "vecmanip.h"

/*
void get_delta_r(const std::vector<std::vector<double> >& r,
	const std::vector<std::vector<double> >& r0,
	std::vector<double>& delta_r)
{
	int N = r.size();
	for(int i=0;i<N;++i)
		delta_r[i] = dist_sq(r[i],r0[i]);
}

double get_dR(const std::vector<double> & delta_r)
{

	int N = delta_r.size();
	double dR = 0;
	for(int i=0;i<N;++i)
		dR += delta_r[i]*delta_r[i];
	dR /= N;
	return dR;
}
*/
double dist_sq(const std::vector<double>& a,
	const std::vector<double>& b)
{
	double d = 0;
	d += (a[0]-b[0])*(a[0]-b[0]);
	d += (a[1]-b[1])*(a[1]-b[1]);
	d += (a[2]-b[2])*(a[2]-b[2]);

	return d;
}

double get_dR(const std::vector<std::vector<double> >& r,
	const std::vector<std::vector<double> >& r0)
{
	int N = r.size();
	double dR = 0;
	double temp;
	for(int i=0;i<N;++i) 
		dR += dist_sq(r[i],r0[i]);
	return dR/N;
}






#endif

