#include <vector>
#include <iostream>
#include <ostream>
#include <string>
#include <map>

// major difference : 
// on heap or on stack


class entity
{
private:
	std::string name;
public:
	entity() : name("unknown") {}
	entity(const std::string& iname) : name(iname) 
	{
		std::cout << "created!" << std::endl;
	}
	std::string get_name()
	{
		return name;
	}
	~entity()
	{
		std::cout << name << " got Destroyed!" << std::endl;
	}
};

std::ostream &operator<<(std::ostream& COUT,const std::vector<std::string>& arr)
{
	for(auto str : arr)
	{
		COUT << str << std::endl;
	}
	return COUT;
}

void test_mult_map()
{
	std::multimap<std::string, std::string> sec 
	{
		{"youzark","cool"},
		{"hyx","official"},
		{"whitebrow","don't know why"}
	};
	std::cout << "test 5:" << std::endl;
	for(const auto& pair : sec)
	{
		std::cout << pair.first << " couple with :" << pair.second << std::endl;
	}
}

int main()
{
	// fast and should alway be used : with constructor:
	entity me = entity("youzark");
	std::cout << "Test 1:" << std::endl;
	std::cout << me.get_name() << std::endl;


	// why some time not on stack:
	// 1: scope , life span
	// 2: size

	entity *temp;
	{
		entity *metoo = new entity("hyx");
		temp = metoo;
		std::cout << "Test 2:" << std::endl;
		std::cout << metoo->get_name() << std::endl;
		// destructor will not be called at end of the scope
	}

	std::cout << temp->get_name() << " can be all visited out of scope" << std::endl;
	// even not at the end of the main()
	entity inittest3{"whitebrow"};
	std::cout << "Test 3:" << std::endl;
	std::cout << inittest3.get_name() << " init with {}" << std::endl;

	std::vector<std::string> arr{"youzark","whitebrow","hyx"};
	std::cout << "Test 4:" << std::endl;
	std::cout << arr;

	test_mult_map();

	return 0;
}









