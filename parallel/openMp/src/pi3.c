#include <stdio.h>
#include <omp.h>

#define P_Number 2

static long num_steps = 100000;
double step;

int main()
{
	int i;
	double sum[P_Number];
	double pi;

	step = 1.0/(double)num_steps;
	omp_set_num_threads(P_Number);
	#pragma omp parallel
	{
		double x;
		int id;
		id = omp_get_thread_num();
		sum[id] = 0;
			#pragma omp parallel for
			for(i = 0;i < num_steps;i ++)
			{
				x = (i + 0.5) * step;
				sum[id] += 4.0/(1.0 + x*x);
			}
	}
	for(i = 0;i < P_Number;i++) pi += sum[i] * step;
	printf("%lf\n",pi);
}
