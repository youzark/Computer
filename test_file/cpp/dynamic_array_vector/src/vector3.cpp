#include <iostream>
#include "vector3.h"

Vector3::Vector3() {}
Vector3::Vector3(float scalar)
	: x(scalar),y(scalar),z(scalar) 
{
	mem_block = new int[5];
}
Vector3::Vector3(float x,float y,float z)
	: x(x) ,y(y) ,z(z) 
{
	mem_block = new int[5];
}

Vector3::Vector3(const Vector3& other)
	: x(other.x) ,y(other.y) ,z(other.z)
{
	std::cout << "Copy\n";
	mem_block = other.mem_block;
}

Vector3::Vector3(Vector3&& other)
	: x(other.x) ,y(other.y) ,z(other.z)
{
	mem_block = other.mem_block;
	other.mem_block = nullptr;
	std::cout << "Move\n";
}

Vector3::~Vector3() 
{
	std::cout << "destroyed" << std::endl;
	delete[] mem_block;
}

Vector3& Vector3::operator=(const Vector3& other)
{
	std::cout << "Copy\n"; 
	x = other.x;
	y = other.y;
	z = other.z;
	return *this;
}

Vector3& Vector3::operator=(Vector3&& other)
{
	mem_block = other.mem_block;
	other.mem_block = nullptr;
	std::cout << "Move\n"; 
	x = other.x;
	y = other.y;
	z = other.z;
	return *this;
}

