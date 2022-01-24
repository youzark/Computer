#include <iostream>
#include <vector>

struct Vertex
{
	float x,y,z;
	Vertex(float x,float y,float z)
		: x(x),y(y),z(z) {}
	Vertex(const Vertex& vertex)
		: x(vertex.x),y(vertex.y),z(vertex.z)
	{
		std::cout << "Copied !!!" << std::endl;
	}
};

std::ostream& operator<<(std::ostream& COUT,const Vertex& vertex)
{
	COUT << vertex.x << ", " << vertex.y << ", " << vertex.z << std::endl;
	return COUT;
}

int main()
{
	std::vector<Vertex> vertices;
	vertices.reserve(3);  // this way , we don't realloc if we know the size
	vertices.emplace_back(1,2,3); // this way , we just construct in place rather than construct and copy
	vertices.emplace_back(4,5,6);
	vertices.push_back(Vertex(6,7,8));

	/* for (int i = 0; i < vertices.size(); ++i) */
	/* { */
	/* 	std::cout << vertices[i]; */
	/* } */

	/* for ( auto vertex : vertices ) */
	/* { */
	/* 	std::cout << vertex; */
	/* } */
}



