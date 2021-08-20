#include <cstddef>
#include <iostream>

// basic feature implementation
//

template<typename T>
class Vector
{
	public:
		Vector()  //start with the size of 2
		{
			realloc(2);
		}

		~Vector()
		{
			delete[] m_data;
		}

		void push_back(const T& value)
		{
			if ( m_size >= m_capacity )
			{
				realloc(m_size + m_size/2);
			}

			m_data[m_size++] = value;
		}

		void push_back(const T&& value)
		{
			if ( m_size >= m_capacity )
			{
				realloc(m_size + m_size/2);
			}

			m_data[m_size++] = std::move(value);
		}

		T& operator[](size_t index)
		{
			return m_data[index];
		}

		const T& operator[](size_t index) const
		{
			return m_data[index];
		}

		size_t size() const
		{
			return m_size;
		}

		template<typename... args>
		T& emplace_back(args&&... arglist)
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

		void pop_back()
		{
			if(m_size > 0)
			{
				m_data[--m_size].~T();
			}
		}


		void clear()
		{
			for (int i = 0; i < m_size; ++i) 
			{
				m_data[i].~T();
			}
			m_size = 0;
		}
	private:
		void realloc(size_t new_capacity)
		{
			// 1. allocate a new block of memory
			// 2. copy accross all the old var (move rather than cope is better)
			// 3. delete
			
			T *new_block = new T[new_capacity];

			// for downsize 
			if ( new_capacity < m_size )
			{
				m_size = new_capacity;
			}

			for ( size_t i = 0 ;i < m_size; i++ )
			{
				new_block[i] = std::move(m_data[i]);
			}

			delete [] m_data;
			m_data = new_block;
			m_capacity = new_capacity;
		}
	private:
		
		T* m_data = nullptr;
		size_t  m_size = 0;
		size_t m_capacity = 0;

};



struct Vector3
{
	float x = 0.0f,y = 0.0f,z = 0.0f;

	Vector3() {}
	Vector3(float scalar)
		: x(scalar),y(scalar),z(scalar) {}
	Vector3(float x,float y,float z)
		: x(x) ,y(y) ,z(z) {}

	Vector3(const Vector3& other)
		: x(other.x) ,y(other.y) ,z(other.z)
	{
		std::cout << "Copy\n";
	}

	Vector3(const Vector3&& other)
		: x(other.x) ,y(other.y) ,z(other.z)
	{
		std::cout << "Move\n";
	}

	~Vector3() {}

	Vector3& operator=(const Vector3& other)
	{
		std::cout << "Copy\n"; 
		x = other.x;
		y = other.y;
		z = other.z;
		return *this;
	}

	Vector3& operator=(const Vector3&& other)
	{
		std::cout << "Move\n"; 
		x = other.x;
		y = other.y;
		z = other.z;
		return *this;
	}
};


template<typename T>
void printVector(const Vector<T>& vector)
{
	std::cout << "+-------------------+" << std::endl;
	for (size_t i = 0;i < vector.size() ; i++)
	{
		std::cout << vector[i] << std::endl;
	}
	std::cout << "+-------------------+" << std::endl;
}


template<>
void printVector(const Vector<Vector3>& vector)
{
	std::cout << "+-------------------+" << std::endl;
	for (size_t i = 0;i < vector.size() ; i++)
	{
		std::cout << vector[i].x  << " ,"<< vector[i].y << " ," << vector[i].z << std::endl;
	}
	std::cout << "+-------------------+" << std::endl;
}


int main()
{
	Vector<Vector3> vector;
	vector.push_back(Vector3(1.0));
	vector.push_back(Vector3(1.0,2.0,3.0));
	vector.push_back(Vector3());
	vector.emplace_back(2.0f);
	vector.emplace_back(1,2,4);
	vector.emplace_back(1,2,4);
	printVector(vector);
}
