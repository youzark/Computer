#include <iostream>
#include <vector>
#include <unordered_map>

int main()
{
	std::vector<int> value = {1,2,3,4,5};

	// traditional way
	for (int i = 0; i < value.size(); ++i) 
	{
		std::cout << value[i] << std::endl;
	}

	std::cout << "\ntest2\n" ;

	for (int i : value) 
	{
		std::cout << i << std::endl;
	}
	// how does that work?

	// iterator
	// iterator just like a generalize index
	// for vector , it's a int(i)
	// for linked list, it's some way to traverse the list
	// for a tree , it's another way
	
	// extented way to write test2
	// when you need to erase or add an element to the vector
	// begin() and end() must be provided to ues :(range) operator
	std::cout << "\ntest3\n";
	for(std::vector<int>::iterator iter = value.begin();iter != value.end();iter++)
	{
		std::cout << *iter << std::endl;
	}

	using scoremap = std::unordered_map<std::string, int>;
	scoremap map;
	map["Chrome"] = 5;
	map["youzark"] = 9;

	std::cout << "\ntest4\n";
	for (scoremap::const_iterator iter = map.begin(); iter != map.end(); iter ++)
	{
		auto &key = iter->first;
		auto &val = iter->second;
		std::cout << "map[" << key << "] == " << val << std::endl;
	}

	std::cout << "\ntest5\n";
	for (auto kv:map)
	{
		auto &key = kv.first;
		auto &val = kv.second;
		std::cout << "map[" << key << "] = " << val << std::endl;
	}

	for (auto [key,val] : map)
	{
		std::cout << "map[" << key << "] = " << val << std::endl;
	}

}
