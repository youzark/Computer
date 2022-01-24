#include <cstdlib>
#include <iostream>
#include <string>


class entity
{
	private:
		std::string data;
	public:
		entity()
			: data("youzark") {}
		entity(const std::string& name) 
			: data(name) {}
		const std::string& get_name() const { return data;}
};
int main()
{
	int a = 2; // on stake
	int *b = new int; // on heap

	entity *e_list = new entity[20];
	// with classes call new
	// 1: compute size of memory and allocate on the heap
	// 2: call the constructor
	
	entity *e_new_list = (entity*)std::malloc(sizeof(entity) * 20);
	// this will allocate the memory 
	// this will not call constructor

	delete b;
	delete[] e_list;
	// heap memory must get deleted explicitly
	// new with [] delete with []
}
