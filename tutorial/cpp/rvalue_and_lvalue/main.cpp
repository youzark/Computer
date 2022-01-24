#include <iostream>


int get_value()
{
	return 10;
}

int& get_ref()
{
	static int value = 10;
	return value;
}

void set_val(int value)
{
}

int main()
{
	int i = 10;  // i is the l-value and 10 is the r-value
	// not all the time ,l-value is located at left hand

	int a = i;  // assign a l-value to a l-value
	// notive i is still a l-value here
	
	int b = get_value(); //get_value() here is a r-value (not modifiable)

	// get_value() = 10 is not valid;
	
	get_ref() = 11; // here get_ref() is modifiable and is l-value

	// you cannot take a l-value reference from a r-value
	set_val(i);
	set_val(10);

	
	const int& c = 10;  // the compiler will create a temp storage and assign to c
	/* int& d = 10; */  

	void print_name(std::string& name);
	// print_name(full_name) is valid since full_name is a l-value
	// print_name(first_name + second_name) is invalid since para is r-value
	
	void print_name(const std::string& name);
	// this function works both fine with 
	// l-value and r-value as parameter since for r-value ,compiler will
	// create a temp storage
	
	void print_name(std::string&& name);
	// r-value reference
	

	std::string first_name = "Hua";
	std::string second_name = "YongXiang";
	std::string full_name = first_name + second_name;
	
	print_name(full_name);

	print_name(first_name + second_name);

}

void print_name(std::string& name)
{
	std::cout << "[lvalue]" << name << std::endl;
}


void print_name(std::string&& name)
{
	std::cout << "[rvalue]" << name << std::endl;
}

void print_name(const std::string& name)
{
	std::cout << "[constvalue]" << name << std::endl;
}
