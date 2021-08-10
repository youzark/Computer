#include <iostream>
#include <string>

class employee
{
	public:
		std::string name;
		std::string company;
		int age;

		void introduce()
		{
			std::cout << "Name - " << name << std::endl;
			std::cout << "Company - " << company << std::endl;
			std::cout << "Age - " << age << std::endl;
		}

		//constructor : when create constructor default one while eliminate
		//1: no return value
		//2: same name as class 
		//3: almost always public
		employee(std::string i_name,std::string i_company,int i_age)
		{
			name = i_name;
			company = i_company;
			age = i_age;
		}
};  // need ; at end of class defination

int main()
{
	// class_name inst_name = constructor();
	employee employee1 = employee("Saldina","CodeBeauty",25);
	// if no constructor specified , default constructor is call ,assign random string
	/* employee1.name = "Saldina"; */
	/* employee1.company = "CodeBeauty"; */
	/* employee1.age = 25; */
	employee1.introduce();

	employee employee2 = employee("Jhon","Amazon",23);
	/* employee2.name = "Jhon"; */
	/* employee2.company = "Amazon"; */
	/* employee2.age = 23; */
	employee2.introduce();

}
