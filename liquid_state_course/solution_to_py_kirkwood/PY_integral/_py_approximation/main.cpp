

#include <iostream>
#include <vector>
#include <string>
#include <math.h>

#include "nr_headers/nr3.h"
#include "nr_headers/fourier.h"

#include "write_nrvec.h"
#include "py_approx.h"
#include "write_nrvec.h"

using namespace std;



int main()
{

	int N = 1024*4;
	double lambda = 0.99;
	int itmax = 100;
	double rho = 0.5;
	double eps = 1.;
	double sigma = 1.;
	double beta = 1.;

	double rmax =sigma*pow(2.,1./6);

	VecDoub r(N);
	for(int i=0;i<N;++i) {
		r[i] = (rmax/(N-1))*i;
	}

	VecDoub cn(N);
	cn = get_c0(r);
	VecDoub cnp1(N);
	cnp1 = cn;


	get_c(cn,cnp1,r,rho,lambda,itmax,eps,sigma,beta);
	cr2gr(cnp1,r);

	write_nrvec(cnp1,"g.dat");
	write_nrvec(r,"r.dat");



	return 0;
}



