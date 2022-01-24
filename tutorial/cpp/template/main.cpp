#include <vector>
#include <string>
#include <iostream>

// only get created when called 
// template<class T> is the same
template<typename T> // template parameter
void print(T value)
{
	std::cout << value << std::endl;
}

template<typename T,int size>
class array
{
public:
	array(T name) 
		: data(name) {}
	int get_size()
	{
		return size;
	}
private:
	T data;
};



int main()
{
	std::string name{"youzark"};
	// if c++ can deduce type ,we dont need to specify
	print(name);
	print<std::string>(name);

	auto names = array<std::string,3>("youzark");
}

