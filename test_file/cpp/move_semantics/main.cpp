#include <cstring>
#include <iostream>

// only after c++11 , move is possible
// since it relies on r-value reference which is first
// introduced in c++11
//


// why do you need move semantics
// move objects around
// just don't construt a throw away object as some parameter
//

class my_string
{
	public:
		my_string() = default;
		my_string(const char* string)
		{
			printf("Create!\n");
			m_size = strlen(string);
			m_data = new char[m_size];
			memcpy(m_data, string, m_size);

		}
		my_string(const my_string& other)
			:m_size(other.m_size)
		{
			std::cout << "copyed!\n";
			m_data = new char[m_size];
			memcpy(m_data,other.m_data, m_size);
		}

		my_string(my_string&& other)
		{
			std::cout << "Moved\n";
			m_size = other.m_size;
			m_data = other.m_data;

			other.m_data = nullptr;
			other.m_size = 0;
			// other become hollow cause we just steel data from it.
			// if we don't assign it to null
			// destructor will destroy our steeled data
		}

		void print()
		{
			for (int i = 0;i < m_size; i++)
			{
				printf("%c",m_data[i]);
			}
			std::cout << std::endl;
		}

		// here is a assignment operator that use move rather than copy
		// you can(should) implement a copy version too
		my_string& operator=(my_string&& other)
		{
			std::cout << "assign a r-value\n";
			if (this != &other)
			{
				delete[] m_data;  // we try to move new data in 
				// just first clear the old data
				// but be careful if this == other,the data will get deleted 
				m_data = other.m_data;
				m_size = other.m_size;

				other.m_size  = 0;
				other.m_data = nullptr;
			}
			return *this;
		}

		~my_string()
		{
			std::cout << "Destroy!\n";
			if(!m_data)
				delete m_data;
		}
	private:
		int m_size;
		char *m_data;
};

class entity
{
	public:
		entity(const my_string& name)
			: m_name(name) {}

		entity(my_string&& name)
			: m_name((my_string&&)name) {}

		void print_name()
		{
			m_name.print();
		}
	private:
		my_string m_name;
};

int main()
{
	/* entity entity(my_string("youzark")); // need copy constructor to pass parameter */
	// in this situation , we create a temp var my_string("youzark");  
	// to pass parameter we got to copy it first whatever situation
	// why not just move it
	//
	
	/* my_string string = "Hello"; */

	/* my_string second = string; // this is a copy rather than move */
	/* my_string third = (my_string &&)string; // this is a move */
	/* my_string dest(std::move(string));  // just a fancy way of doing the former move */

	/* my_string forth = std::move(string); */

	/* my_string fifth; */
	/* /1* fifth = std::move(string); *1/ */

	/* my_string apple = "apple"; */
	/* my_string apple_place ; */

	/* apple_place = std::move(apple); */

	my_string apple = "Apple";
	my_string dest = std::move(apple);

	my_string test;

	apple.print();
}

