#ifndef GUARD_back_in_box_h
#define GUARD_back_in_box_h

#include <vector>
#include <cmath>
void back_in_box(std::vector<std::vector<double> >& r, double L)
{
	int N = r.size();
	for(int i=0;i<N;++i) {
		r[i][0] -= L*floor(r[i][0]/L);
		r[i][1] -= L*floor(r[i][1]/L);
		r[i][2] -= L*floor(r[i][2]/L);

	}
}



#endif
