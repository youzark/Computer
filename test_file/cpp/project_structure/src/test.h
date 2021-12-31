#pragma once
#include <iostream>

template<typename T>
class test_class
{
	public:
		inline test_class(T);
		inline void set_data(T);
		inline T get_data();
	private:
		T data;
};

template<typename T>
test_class<T>::test_class(T init_data)
	:data(init_data) {}

template<typename T>
T test_class<T>::get_data()
{
	return data;
}

template<typename T>
void test_class<T>::set_data(T input_data)
{
	return data;
}
