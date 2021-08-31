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
