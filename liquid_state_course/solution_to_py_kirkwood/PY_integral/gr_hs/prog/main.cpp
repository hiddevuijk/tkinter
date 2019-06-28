
#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

#include "fcc_lattice.h"
#include "distance_3d.h"
#include "pair_distribution.h"
#include "back_in_box.h"

#include "nr3.h"
#include "ran.h"



#include "markov_chain.h"
#include "box_muller.h"
using namespace std;

int main()
{

	int N = 900;
	int L = 10;
	double d = 0.001;
	double bs = 0.0001;
	int itmax = 200;
	int steps_per_it = 1000000;

	int init_steps = 200000;
	int seed = 12345689;

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
	for(int i=0;i<Ngr;++i)
		gr[i] = (i+.5)*bs;


	vector<vector<double> > r(N,vector<double>(3,0.));
	init_r_fcc(r,N,L);


	write_mat(r,r.size(),r[0].size(),"config0.dat");

	make_steps(r,ranNR,init_steps,d,L,N);
	for(int it = 0;it<itmax;++it) {
		if(it%50 == 0) cout << it << '\t'<<itmax<<endl;
		make_steps(r,ranNR,steps_per_it,d,L,N);	
		pdist_temp = pair_distances(r,L);
		g_temp = pd2g(pdist_temp,gr,N,rho);
		for(int i=0;i<Ngr;++i)
			g[i] += g_temp[i]/itmax;
	}
	for(int i=0;i<N;++i) {
		for(int j=0;j<i;++j) {
			if(distance_3d(r[i],r[j],L)<1)
				cout << distance_3d(r[i],r[j],L) << endl;
		}
	}
	// shit gr to the centers of the bins
	for(int i=0;i<Ngr;++i)
		gr[i] -= .5*bs;
	back_in_box(r,L);
	write_vec(g,"g.dat");
	write_vec(gr,"r.dat");
	write_mat(r,r.size(),r[0].size(),"config.dat");

	return 0;
}







