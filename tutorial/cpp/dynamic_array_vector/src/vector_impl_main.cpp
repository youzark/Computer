#include <iostream>
#include "vector.h"
#include "vector3.h"

template<typename T>
void print_vector(const Vector<T>& vector)
{
	for(size_t i = 0; i < vector.size();i++)
	{
		std::cout << vector[i] << std::endl;
	}
}

int main()
{
	Vector<std::string> names;
	names.push_back("hyx");
	names.push_back("youzark");
	names.push_back("whitebrow");

	print_vector(names);

	return 0;
}
