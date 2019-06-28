#ifndef GUARD_distance_3d_h
#define GUARD_distance_3d_h

#include <vector>
#include <cmath>

double distance_3d(const std::vector<double>& a,
	const std::vector<double>& b, double L)
{
	double d = 0;
	double di = 0;

	for(int i;i<3;++i) {
		di = a[i] - b[i];
		di -= L*round(di/L);
		d += di*di;
	}
	return sqrt(d);
}

double min_dist(const std::vector<double>& a,
	int i, const std::vector<std::vector<double> >& r,
	double L)
{
	// set mindist to large value
	double mindist = L;

	double dist;
	for(int j=0;j<r.size();j++) {
		if( i == j) continue;
		dist = distance_3d(a,r[j],L);
		if( dist < mindist)
			mindist = dist;
	}
	return mindist;
}



#endif

