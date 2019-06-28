#ifndef GUARD_py_approx_h
#define GUARD_py_approx_h

#include <math.h>
#include <iostream>
namespace py_approx_params {
double pi2 = 6.2831853071795864769;
double r_cutoff = 0.7;
}



//pair potential
double u(double r, double eps =1., double sigma=1.,double beta = 1.)
{
	if(r<sigma*pow(2.,1./6)) {
		double sr6 = pow(sigma/r,6.);
		return eps*4*(sr6*sr6-sr6)/beta;
	} else {
		return 0.;
	}
}

// exp(beta u(r))
double ebu(double r, double eps = 1., double sigma = 1., double beta =1.)
{
	/*	
	if( r> sigma*py_approx_params::r_cutoff)
		return exp(beta*u(r,eps,sigma,beta));
	else
		return exp(beta*u(py_approx_params::r_cutoff,eps,sigma,beta));
	*/
	return exp(beta*u(r,eps,sigma,beta));
}


VecDoub get_c0(const VecDoub& r,double eps=1.,double sigma=1.,double beta = 1.)
{
	VecDoub c0(r.size());
	for(int i=r.size()-1;i>=0;--i){
		if(r[i]>sigma*pow(2.,1./)) {
			
		if(r[i]>py_approx_params::r_cutoff)
			c0[i] = 1-ebu(r[i],eps,sigma,beta);
		else
			c0[i] = c0[i+1];

	}

	return c0;
}

// ck2hk replaces the input vector c(k) with h(k)
void ck2hk(VecDoub& vec, const double& rho)
{
	int N = vec.size();
	for(int i=0;i<N;++i) {
		vec[i] = vec[i]/(1.-rho*vec[i]);
	}
}


// hr2cr replaces the input vector h(r) with c(r)
void hr2cr(VecDoub& vec, const VecDoub& r, double eps = 1., double sigma = 1., double beta = 1.)
{
	int N = vec.size();
	for( int i =N-1;i>=0;--i)
		if(r[i]>py_approx_params::r_cutoff)
			vec[i] = (vec[i]+1)*(1-ebu(r[i],eps,sigma,beta));
		else
			vec[i] = vec[i+1];
}


void gr2cr(VecDoub& vec, const VecDoub& r, double eps = 1.,double sigma = 1.,double beta = 1.)
{

	int N = vec.size();
	for(int i=N-1;i>=0;--i)
		if(r[i]>py_approx_params::r_cutoff)
			vec[i] *= (1-ebu(r[i],eps,sigma,beta));
		else
			vec[i] = vec[i+1];

}

void cr2gr(VecDoub& vec, const VecDoub& r, double eps = 1.,double sigma = 1.,double beta = 1.)
{

	int N = vec.size();
	for(int i=N-1;i>=0;--i)
		if(r[i]>py_approx_params::r_cutoff){
			double d = (1-ebu(r[i],eps,sigma,beta));
			if(d>0)
				vec[i] /= d;
			else
				vec[i] = 1.;
		}else
			vec[i] = 0.;
}




void cr2ck(VecDoub& vec, const VecDoub& r)
{
	int N = vec.size();
	for(int i=1;i<N;++i){
		vec[i] *= r[i]*py_approx_params::pi2/i;
	}
	sinft(vec);
	vec[0] = 0.;
}


void hk2hr(VecDoub& vec, const VecDoub& r)
{
	int N = vec.size();
	for(int i=0;i<N;++i) {
		vec[i] *= i/py_approx_params::pi2;
	}
	sinft(vec);
	for(int i=1;i<N;++i)
		vec[i] *= 2/(N*r[i]);
	
	vec[0] = -1.;
}



void get_cnp1(VecDoub& cn, const VecDoub& r,double rho,
	double eps = 1.,double sigma = 1., double beta = 1.)
{
	cr2ck(cn,r);
	ck2hk(cn,rho);
	hk2hr(cn,r);
	hr2cr(cn,r,eps,sigma,beta);
}


void get_c(VecDoub& cn, VecDoub& cnp1, const VecDoub& r, const double& rho, double lambda,
	int itmax, double eps=1., double sigma = 1., double beta = 1.)
{
	int N = cn.size();

	for(int it = 0; it< itmax;++it) {
		cn = cnp1;
		get_cnp1(cnp1,r,rho,eps,sigma,beta);
		for(int i=0;i<N;++i)
			cnp1[i] = lambda*cn[i] + (1-lambda)*cnp1[i];
	}

}





#endif
