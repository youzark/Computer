#pragma once
#include <iostream>
#include "vector.h"
struct Vector3
{
	float x = 0.0f,y = 0.0f,z = 0.0f;
	int* mem_block;

	Vector3();
	Vector3(float scalar);
	Vector3(float x,float y,float z);
	Vector3(const Vector3& other);
	Vector3(Vector3&& other);
	~Vector3();
	Vector3& operator=(const Vector3& other);
	Vector3& operator=(Vector3&& other);
};
template<typename T>
void inline printVector(const Vector<T>& vector);

void inline printVector(const Vector<Vector3>& vector);


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

void printVector(const Vector<Vector3>& vector)
{
	std::cout << "+-------------------+" << std::endl;
	for (size_t i = 0;i < vector.size() ; i++)
	{
		std::cout << vector[i].x  << " ,"<< vector[i].y << " ," << vector[i].z << std::endl;
	}
	std::cout << "+-------------------+" << std::endl;
}
