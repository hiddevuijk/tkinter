#ifndef GUARD_markov_chain_h
#define GUARD_markov_chain_h

#include "distance_3d.h"
void make_steps(std::vector<std::vector<double> >& r,
	Ranq2& ranNR,int steps,double d,double L,
	int N)
{
	double mindist;
	int i,xyz;
	std::vector<double> tryvec(3);
	for(int it = 0;it<steps;++it) {
		i = ranNR.int64()%N;
		tryvec = r[i];
		//xyz = ranNR.int64()%(3);
		tryvec[0] += d*(-.5+ranNR.doub());
		tryvec[1] += d*(-.5+ranNR.doub());
		tryvec[2] += d*(-.5+ranNR.doub());

		mindist = min_dist(tryvec,i,r,L);
		if(mindist>1.0) {
			r[i] = tryvec;
		}
	}
}

#endif

