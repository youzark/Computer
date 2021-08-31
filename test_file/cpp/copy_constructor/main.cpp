#include <iostream>
#include <cstring>

// copy function is used to deal with pointer in the class
// when we copy the object
// we don't want to simply copy the pointer(sallow)
// we want to copy the data the pointer points to(deep)
class string
{
	private:
		char* m_buffer;
		unsigned int m_size;

	public:
		string(const char* string)
		{
			m_size = strlen(string);
			m_buffer = new char[m_size + 1]; // to put 0 at end of the string
			memcpy(m_buffer,string,m_size);
			m_buffer[m_size] = 0;
		}

		// copy constructor
		// when you copy the object to a same type object
		// rather than copy by default(sallow)
		// copy constructor will be called
		
		/* string(const string& other) = delete; */
		// the above one will disable copy operation
		//
		// string string_new = string_old;
		// here: = will call constructor,since it pass string_old as parameter,
		// it just invoke copy constructor
		// string_new is this object
		// string_old is other object
		string(const string& other)
			: m_size(other.m_size)
		{
			// not only init and assign will invoke copy funciton
			// parameter passing will copy the object by default
			// to save the space and time 
			// just use const classname&  (const reference)
			std::cout << "copy string" << std::endl; //check how many copy
			m_buffer = new char[m_size + 1]; 
			memcpy(m_buffer,other.m_buffer,m_size);
		}

		char& operator[](unsigned int index)
		{
			return m_buffer[index];
		}


	~string()
	{
		delete[] m_buffer;
	}

	friend std::ostream& operator<<(std::ostream& stream, const string& string);
};

std::ostream& operator<<(std::ostream& stream, const string& string)
{
	stream << string.m_buffer;
	return stream;
}


void print_string(const string& string)
{
	std::cout << string << std::endl;
}

int main()
{
	string string1 = "youzark";
	string second = string1;  

	second[0] = 'v';
	// something wrong here? (if no copy function is defined)
	// we have a shadow copy 
	// so what we copy into second is exactly what's in string1
	// but since we have "a pointer to m_buffer"
	// we copy it into second too
	// so when the destructor is called by string1 and second
	// the "m_buffer " will be released twice which cause a problem(double free)

	/* std::cout << string1 << std::endl; */
	/* std::cout << second << std::endl; */

	print_string(string1);
	print_string(second);
}

/**
* @brief: test
*
* @param: 

:p: TODO
:a: TODO
:r: TODO
:a: TODO
:m: TODO
*
* @return: ReturnType
*/
void print_num(int a)
{
	std::cout << a << std::endl;
}
