
#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

#include "fcc_lattice.h"
#include "distance_3d.h"
#include "pair_distribution.h"
#include "back_in_box.h"

#include "ConfigFile.h"
#include "nr3.h"
#include "ran.h"


#include "markov_chain.h"
#include "box_muller.h"
using namespace std;

int main()
{

	int N;
	double L;
	double d;
	double bs;
	int itmax;
	int steps_per_it;
	int init_steps;
	int seed;

	string input_name = "input.txt";

	ConfigFile config(input_name);
	N = config.read<int>("N");
	L = config.read<double>("L");
	d = config.read<double>("d");
	bs = config.read<double>("bs");
	itmax = config.read<int>("itmax");
	steps_per_it = config.read<int>("steps_per_it");
	init_steps = config.read<int>("init_steps");
	seed = config.read<int>("seed");



	double rho = (1.*N)/(L*L*L);
	cout << rho << endl;
	Ranq2 ranNR(seed);

	vector<double> pdist_temp(N*(N-1)/2);
	int Ngr = ceil(L/bs);
	vector<double> g_temp(Ngr,0.);
	vector<double> g(Ngr,0);
	// contains r values of g
	// shift -.5 bs in the end
	vector<double> gr(Ngr);
	//cout << "check this crap at line 43 or something" << endl;
	for(int i=0;i<Ngr;++i)
		gr[i] = (i+1)*bs;


	vector<vector<double> > r(N,vector<double>(3,0.));
	init_r_fcc(r,N,L);

	int s=0;
	double p=0;
	write_mat(r,r.size(),r[0].size(),"config0.dat");

	make_steps(r,ranNR,init_steps,d,L,N);
	for(int it = 0;it<itmax;++it) {
		if(it%10 == 0) cout << it << '\t'<<itmax<<endl;
		s = make_steps(r,ranNR,steps_per_it,d,L,N);	
		p += double(s)/double(steps_per_it);
		pdist_temp = pair_distances(r,L);
		g_temp = pd2g(pdist_temp,gr,N,rho);
		for(int i=0;i<Ngr;++i)
			g[i] += g_temp[i]/itmax;
	}
	for(int i=0;i<N;++i) {
		for(int j=0;j<i;++j) {
			if(distance_3d(r[i],r[j],L)<1)
				//cout << distance_3d(r[i],r[j],L) << endl;
				cout << "Fuck!! Some spheres overlap!" << endl;
		}
	}
	// shit gr to the centers of the bins
	for(int i=0;i<Ngr;++i)
		gr[i] -= .5*bs;
	back_in_box(r,L);
	write_vec(g,"g.dat");
	write_vec(gr,"r.dat");
	write_mat(r,r.size(),r[0].size(),"config.dat");
	cout <<"succes rate: " <<  p/itmax << endl;
	return 0;
}







