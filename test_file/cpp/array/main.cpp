#include <iostream>

template<typename T,size_t S>
class Array 
{
	public:
		constexpr int Size() const {return S;}

		/* T operator[](int index) {return m_data[index];} */
		// two reason why not use former implementation.
		// not a reference cause: 
		// 1: waste of time space
		// 2: cannot modify the value with []
		// so we chooise to return the reference

		T& operator[](int index) 
		{
			return m_data[index];
		}
		const T& operator[](int index) const {return m_data[index];}
		// fisrt const indicate return value is immutable.
		// the second const indicate the function cannot change class member value.


		T* Data() { return m_data; }
		const T* Data() const { return m_data; }

	private:
		T m_data[S];
};
	
int main()
{
	Array<int , 5> data;

	std::cout << data.Size();
	
	static_assert(data.Size() < 10, "Size is too large");


	const auto& dataReference = data;
	// what we expect is following:
	// 1 : we can access the data
	// 2 : we cannot modify the data

	for (int i = 0; i < data.Size(); ++i) 
	{
		dataReference[i ];
		std::cout << data[i] << std::endl;
	}
	

	/* int a = 0; */
	/* const int * const p = &a; */
	/* a = 1; */
	/* std::cout << *p << std::endl; */
}
