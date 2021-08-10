#include <iostream>
#include <string>


class abstract_employee
{
	// abstract class
	// or name "contract"
	// whichever class signs this contract,must provide implementation for the methods in the contract
	// hide the complex of implementation of abstarct function
	
	//pure virtual function
	// cautious the define form
	// any class sign this abstract class must provide implementation of abstract function
	// virtual return_type function_name(para_list)=0;
	virtual void ask_for_promotion()=0;

};

class employee:abstract_employee
{
	private:
		std::string name;
		std::string company;
		int age;
	public:
		//constructor : when create constructor default one while eliminate
		//1: no return value
		//2: same name as class 
		//3: almost always public
		// can be put anywhere in class def
		employee(std::string i_name,std::string i_company,int i_age)
		{
			name = i_name;
			company = i_company;
			age = i_age;
		}


		// idea of encapsulation
		// getter & setter
		// you can add validator in getter and setter
		void set_name(std::string i_name)
		{
			name = i_name;
		}
		std::string get_name()
		{
			return name;
		}
		void set_company(std::string i_company)
		{
			company = i_company;
		}
		std::string get_company()
		{
			return company;
		}
		void set_age(int i_age)
		{
			if(i_age >= 18)
			{
				age = i_age;
			}
		}
		int get_age()
		{
			return age;
		}



		void introduce()
		{
			std::cout << "Name - " << name << std::endl;
			std::cout << "Company - " << company << std::endl;
			std::cout << "Age - " << age << std::endl;
		}
		void ask_for_promotion()
		{
			if(age > 30)
				std::cout << name << " got promoted!" << std::endl;
			else
				std::cout << "sorry no promotion for you" << std::endl;
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
	employee1.ask_for_promotion();

	employee employee2 = employee("Jhon","Amazon",43);
	employee2.set_name("Bob");
	/* employee2.name = "Jhon"; */
	/* employee2.company = "Amazon"; */
	/* employee2.age = 23; */
	employee2.introduce();
	employee2.ask_for_promotion();
	

	// Rule1 : encapsulation
	// bind operation and data
	// prevent object outside class interact with data directly
	// provide own way for doing that (by function)
	//
	// Rule2 : abstraction
	// hide complex operation series behind simple interface
	// By: interface class or abstract class

}
