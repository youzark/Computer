#include <iostream>
#include <vector>

struct Vertex
{
	float x,y,z;
};

std::ostream& operator<<(std::ostream& COUT,const Vertex& vertex)
{
	COUT << vertex.x << ", " << vertex.y << ", " << vertex.z << std::endl;
	return COUT;
}

int main()
{
	std::vector<Vertex> vertices;
	vertices.push_back({1,3,4});
	vertices.push_back({2,4,5});

	for (int i = 0; i < vertices.size(); ++i)
	{
		std::cout << vertices[i];
	}

	vertices.erase(vertices.begin() + 1);

	for ( auto vertex : vertices )
	{
		std::cout << vertex;
	}
}
