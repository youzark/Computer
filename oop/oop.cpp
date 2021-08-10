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

// object in abstract_employee is private by default
// you can specify it to public
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


// chile class / sub class
// super class / parent class
//
// object in abstract_employee is private by default
// you can specify it to public
class developer:public employee
{
	private:
		std::string favorite_programming_language;
	public:
		// constructor of subclasses
		// inherit constructor from super class, so no default constructor exists.
		// better create one

		developer(std::string i_name,std::string i_company,int i_age,std::string i_favorite_programming_language)
			:employee(i_name,i_company,i_age)  // construct base type this way
		{
			favorite_programming_language = i_favorite_programming_language;
		}

		void fix_bug()
		{
			// notice we have to use get_name()
			// cant access super private property directly
			std::cout << get_name() << " fixed bug using " << favorite_programming_language << std::endl;
			// if name define in employee as:
			// protected:
			// std::string name
			// you can use it directly
		}
};

class teacher:public employee
{ 
	private:
		std::string subject;
	public:
		teacher(std::string i_name,std::string i_company,int i_age,std::string i_subject)
			:employee(i_name,i_company,i_age)
		{
			subject = i_subject;
		}
		void prepare_lession()
		{
			std::cout << get_name() << " is preparing " << subject << "lesson" << std::endl;
		}
	
};


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

	developer dev1 = developer("Saldina","CodeBeaty",25,"C++");
	dev1.fix_bug();
	dev1.ask_for_promotion();

	teacher tea1 = teacher("Jhon","Amazon",43,"Math");
	tea1.prepare_lession();
	tea1.ask_for_promotion();
	

	
	

	// Rule1 : encapsulation
	// bind operation and data
	// prevent object outside class interact with data directly
	// provide own way for doing that (by function)
	//
	// Rule2 : abstraction
	// hide complex operation series behind simple interface
	// By: interface class or abstract class
	//
	// Rule3 : inheritance
	// base class 
	//

}
