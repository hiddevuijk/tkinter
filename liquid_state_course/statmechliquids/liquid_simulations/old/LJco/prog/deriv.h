#ifndef GUARD_deriv_h
#define GUARD_deriv_h



#include <cmath>
#include <vector>
#include <random>
#include <assert.h>
#include "vecmanip.h"
#include <iostream>

// force between two particles
double f(const double&);



struct Deriv {
	public:

	Deriv(int NN, double LL, double TT, int seedd):
			N(NN),L(LL), T(TT),seed(seedd),
			generator(seed),ndist(0.,1.),
			F(N,std::vector<double>(3,0.))
			{}


	// calculate derivatives and new positions
	void operator() (
			std::vector<std::vector<double> >& r,
			double dt);

	const std::vector<std::vector<double> >& get_F() {return F;}


	private:
	int N;			// number of particles
	double L;		// size of the box
	double dt;
	double T;
	int seed;		// seed for the random generator

	// the force matrix: F[part. index][xyz]
	std::vector<std::vector<double> > F;
	// calculate the force matrix
	void update_F(const std::vector<std::vector<double> >& r);
	// random number generator
	std::default_random_engine generator;
	std::normal_distribution<double> ndist;
};

double f(const double& r)
{
	double sr6 = 1./(r*r*r*r*r*r);
	return 24.*(2*sr6*sr6-sr6)/r;
}

void Deriv::update_F(
	const std::vector<std::vector<double> >& r)
{

	double abs_r,abs_f,dx,dy,dz;

	// set force on particle i to zero
	for(int i=0;i<N;++i)
		std::fill(F[i].begin(),F[i].end(),0.);

	for(int i=0;i<N;++i) {

		// add force on i due to j
		for(int j=i+1;j<N;++j) {
			dx = r[j][0] - r[i][0];
			dy = r[j][1] - r[i][1];
			dz = r[j][2] - r[i][2];
			dx -= L*round(dx/L);
			dy -= L*round(dy/L);
			dz -= L*round(dz/L);
			abs_r = sqrt(dx*dx+dy*dy+dz*dz);
			if(abs_r < pow(2.,1./6) ) {
			
				abs_f = f(abs_r)/abs_r;
				F[i][0] -= abs_f*dx;
				F[i][1] -= abs_f*dy;
				F[i][2] -= abs_f*dz;
				F[j][0] += abs_f*dx;
				F[j][1] += abs_f*dy;
				F[j][2] += abs_f*dz;
			}
		}

	}
}

// The () operator calculates the increment in r and p (dr and dp) at r,p
// for a time increment dt and adds it to r and p
void Deriv::operator() (
		std::vector<std::vector<double> >& r,
		double dt)
{

	double sqrt_2Tdt = std::sqrt(2*dt*T);
	update_F(r);
	for(int i=0;i<N;++i) {

		//check if forces do not exceed critical value			
		assert(abs(F[i][0])*dt<1.);
		assert(abs(F[i][1])*dt<1.);
		assert(abs(F[i][2])*dt<1.);

		// calculate r increment
		r[i][0] += ndist(generator)*sqrt_2Tdt + F[i][0]*dt;
		r[i][1] += ndist(generator)*sqrt_2Tdt + F[i][1]*dt;
		r[i][2] += ndist(generator)*sqrt_2Tdt + F[i][2]*dt;


	}
}

#endif
