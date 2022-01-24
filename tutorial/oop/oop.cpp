#include <iostream>
#include <string>


enum Knowledge_parts
{
// Rule1 : encapsulation
// bind operation and data
// prevent object outside class interact with data directly
// provide own way for doing that (by function)
encapsulation,

// Rule2 : abstraction
// hide complex operation series behind simple interface
// By: interface class or abstract class
abstraction,

// Rule3 : inheritance
// explained by developer class and teacher class 
inheritance,

// Rule4 : polymorphism
// muliple implementation of the same function for different sub classes
// most commen usage is 
polymorphism,

// By codeBeauty
Virtual_function_pure_virual_function_abstract_class

};

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
		// not a pure virtual ,
		// if it's child class dont implement such a funciton
		// this implementation will be executed
		virtual void work()
		{
			std::cout << name << " is checking email ,task backlog, performing tasks... " << std::endl;
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

		void work()
		{
			std::cout << get_name() << " is writing " << favorite_programming_language << " code " << std::endl;
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
		void work()
		{
			std::cout << get_name() << " is teaching " << subject <<  std::endl;
		}
};


// virtual_function...
class instrument
{
	public:
		// actually every specific instrument should inplement makesound
		// no default is needed
		// and subclassed should be forced to implement 
		// so let use pure virtual function
		virtual void makesound() = 0;
		/* { */
		/* 	std::cout << "Instrument playing..." << std::endl; */
		/* } */
};

class accordion:public instrument
{
	public:
		void makesound()
		{
			std::cout << "accordion playing" << std::endl;
		}
};

class piano:public instrument
{
	public:
		void makesound()
		{
			std::cout << "piano playing" << std::endl;
		}
};

void tester(int part)
{
	switch(part) 
	{
		case encapsulation:
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
				break;
			}
		case abstraction: //same as inheritance
			{
				developer dev1 = developer("Saldina","CodeBeaty",25,"C++");
				dev1.ask_for_promotion();
				teacher tea1 = teacher("Jhon","Amazon",43,"Math");
				tea1.ask_for_promotion();
			}
		case inheritance:
			{
				developer dev1 = developer("Saldina","CodeBeaty",25,"C++");
				dev1.fix_bug();
				dev1.ask_for_promotion();

				teacher tea1 = teacher("Jhon","Amazon",43,"Math");
				tea1.prepare_lession();
				tea1.ask_for_promotion();
				break;
			}
		case polymorphism:
			{
				developer dev1 = developer("Saldina","CodeBeaty",25,"C++");
				dev1.work();

				teacher tea1 = teacher("Jhon","Amazon",43,"Math");
				tea1.work();

				// most common usage of polymorphism is below
				employee *emp1 = &dev1;
				employee *emp2 = &tea1;

				emp1->work();
				emp2->work();
				// if work() is not defined as virtual in employee class ,emp1->work() will use work() defined at employee class 
				// else it will use subclasses defination
				break;
			}
		case Virtual_function_pure_virual_function_abstract_class:
			{
				// abstract class don't have constructor
				/* instrument *inst1 = new instrument(); */
				/* inst1->makesound(); */
				// instrument playing...

				// virtual function enable different implementation of different subclasses and have a default implement
				instrument *inst2 = new accordion();
				inst2->makesound();
				// if in instrument:
				//   virtual void makesound() 
				//   output: accordion playing...
				// else
				// 	 output: instrument playing...

				instrument *inst3 = new piano();
				inst3->makesound();


				instrument *instruments[2] = {inst2,inst3};
				for(int i =0;i < 2;i++)
				{
					instruments[i]->makesound();
				}
			}
	}
}

int main()
{
	tester(Virtual_function_pure_virual_function_abstract_class);
}
