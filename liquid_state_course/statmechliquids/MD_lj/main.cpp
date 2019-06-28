
#include <iostream>
#include <vector>
#include <string>
#include <random>

#include "deriv.h"
#include "integrate.h"
#include "pair_distribution.h"
#include "fcc_lattice.h"
#include "pressure.h"
#include "ConfigFile.h"

using namespace std;


int main(int argc, char *argv[])
{

	int navg;
	int N, seed;
	double T,L,dt,tf,teq;
	double rho;
	int nbin;
	double bs;
	double P;
	// name of the output file
	string name;

	// name of the input file
	// default is input.txt, otherwise commandline input
	string input_name = "input.txt";

	ConfigFile config(input_name);
	N = config.read<int>("N");
	navg = config.read<int>("navg");
	seed = config.read<int>("seed");
	T = config.read<double>("T");
	dt = config.read<double>("dt");
	tf = config.read<double>("tf");
	teq = config.read<double>("teq");
	rho = config.read<double>("rho");
	nbin = config.read<int>("nbin");


	L = pow(N/rho,1./3);
	bs = L/nbin;

	
	// to get centers of bins.
	vector<double> gr(nbin);
	for(int i=0;i<nbin;++i)
		gr[i] = (i+1)*bs;
	vector<double> g(nbin,0.);

	vector<vector<double> > r(N,vector<double>(3));

	// initalize r vector: put particles on a fcc lattice
	init_r_fcc(r,N,1.,L);

	// init deriv objec to perform integration
	Deriv deriv(N,L,T,seed);
	cout << pressure(r,f,rho,T,L)/(rho*T) << endl;

	// equilibrate: integrate until teq
	integrate(r,deriv,0,teq,dt);

	cout << pressure(r,f,rho,T,L)/(rho*T) << endl;

	for( int n =0;n<navg;n++) {
		cout << n << '\t' << navg << endl;
		integrate(r,deriv,0,tf,dt);
		update_g(g,r,N,L,bs,navg);
		cout << pressure(r,f,rho,T,L)/(rho*T) << endl;
		P += pressure(r,f,rho,T,L)/navg;
	}

	// shift gr with -bs to get centers of bins
	for(int i=0;i<nbin;++i)
		gr[i] -= 0.5*bs;
	normalize_g(g,gr,rho);

	cout << P/(T*rho) << endl;
	write_vec(g,"g.dat");
	write_vec(gr,"gr.dat");

	return 0;
}
