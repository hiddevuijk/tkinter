#ifndef GUARD_write_nrvec_h
#define GUARD_write_nrvec_h


#include <fstream>
#include <iostream>
#include <string>

void write_nrvec(VecDoub& v,const char fileName[], int N = 0)
{
	if(N==0) N = v.size();
	std::ofstream out;
	out.open(fileName);
	for(int i=0;i<N;++i)
		out<<v[i] << '\n';
}




#endif
