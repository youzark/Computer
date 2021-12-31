#pragma once

#include <cstddef>
#include <iostream>
#include <new>
template<typename T>
class Vector
{
	public:
		inline Vector();  //start with the size of 2
		inline ~Vector();
		inline void push_back(const T& value);
		inline void push_back(const T&& value);
		inline size_t size() const;
		inline void pop_back();
		inline void clear();

		template<typename... args>
		inline T& emplace_back(args&&... arglist);

		T& operator[](size_t index);
		inline const T& operator[](size_t index) const;
		
	private:
		inline void realloc(size_t new_capacity);
		T* m_data = nullptr;
		size_t m_size = 0;
		size_t m_capacity = 0;
};

// basic feature implementation
//

template<typename T>
Vector<T>::Vector()  //start with the size of 2
{
	realloc(2);
}

template<typename T>
Vector<T>::~Vector()
{
	clear();
}

template<typename T>
void Vector<T>::push_back(const T& value)
{
	if ( m_size >= m_capacity )
	{
		realloc(m_size + m_size/2);
	}

	m_data[m_size] = value;
	m_size++;
}

template<typename T>
void Vector<T>::push_back(const T&& value)
{
	if ( m_size >= m_capacity )
	{
		realloc(m_size + m_size/2);
	}

	m_data[m_size++] = std::move(value);
}

template<typename T>
T& Vector<T>::operator[](size_t index)
{
	return m_data[index];
}

template<typename T>
const T& Vector<T>::operator[](size_t index) const
{
	return m_data[index];
}

template<typename T>
size_t Vector<T>::size() const
{
	return m_size;
}

template<typename T>
template<typename... args>
T& Vector<T>::emplace_back(args&&... arglist)
{
	if (m_size >= m_capacity)
	{
		realloc(m_capacity + m_capacity/2);
	}
	new(&m_data[m_size])  T(std::forward<args>(arglist)...);
	// if we knew the postion where we want to pull new object in .
	// we can just use new(pos_pointer) Type; to create new object
	// this will not create in heap
	// and can avoid one move or copy
	/* m_data[m_size] = T(std::forward<args>(arglist)...); */
	return m_data[m_size++];
}

template<typename T>
void Vector<T>::pop_back()
{
	if(m_size > 0)
	{
		m_data[--m_size].~T();
	}
}


template<typename T>
void Vector<T>::clear()
{
	for (int i = 0; i < m_size; ++i) 
	{
		m_data[i].~T();
	}
	m_size = 0;
}

template<typename T>
void Vector<T>::realloc(size_t new_capacity)
{
	// 1. allocate a new block of memory
	// 2. copy accross all the old var (move rather than cope is better)
	// 3. delete
	
	//cause not constructor is actually needed ,we just need to alloc a piece of memory
	/* T *new_block = new T[new_capacity]; */
	T *new_block = (T*)::operator new(new_capacity * sizeof(T)) ;
	// ::operator new return a nullptr
	

	// for downsize 
	if ( new_capacity < m_size )
	{
		m_size = new_capacity;
	}

	for ( size_t i = 0 ;i < m_size; i++ )
	{
		new_block[i] = std::move(m_data[i]);
	}

	for (int i = 0; i < m_size; ++i) 
	{
		m_data[i].~T();
	}

	::operator delete(m_data,(std::size_t)(m_capacity * sizeof(T) ))  ;
	m_data = new_block;
	m_capacity = new_capacity;
}

