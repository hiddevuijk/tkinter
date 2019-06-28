
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

	int N = 5;
	int L = 10;
	double d = 0.1;
	double bs = 0.1;
	int itmax = 100;
	int steps_per_it = 10000;


	int seed = 12345689;

	double rho = (1.*N)/(L*L*L);
	Ranq2 ranNR(seed);

	vector<double> r1(3,0.),r2(3,0.);
	r1[0] = 1;
	r2[0] = 10.;
	cout << distance_3d(r1,r2,L) << endl;




	return 0;

}







