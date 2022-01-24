#include <string>
#include <iostream>
#include "test.h"

int main()
{
	test_class<int> cla(2);
	std::cout << cla.get_data() << std::endl;
	return 0;
}
