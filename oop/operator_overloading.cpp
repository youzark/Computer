#include <iostream>
#include <string>
#include <list>

enum knowledge_type
{
	global_operator,
	normal_operator,
	common_error1
};

struct youtube_channel
{
	std::string name;
	int subscriber_count;
	youtube_channel(std::string i_name,int i_subscriber_count)
	{
		name = i_name;
		subscriber_count = i_subscriber_count;
	}

	// cause we use & here ,we never change operand in and == operation
	// we have to make parameter a const
	bool operator==(const youtube_channel& yt)
	{
		return this->name == yt.name;
	}
};

struct my_collection
{
	std::list<youtube_channel>my_channels;

	// 1: created as member function
	// 2: only right values are needed
	// 3: right value can be referd to as this
	void operator+=(youtube_channel yt)
	{
		this->my_channels.push_back(yt);
	}

	// common_error1
	void operator-=(youtube_channel yt)
	{
		// remove need == to be overloaded (== or youtube_channel)
		this->my_channels.remove(yt);
	}
};

// passing by reference
std::ostream& operator<<(std::ostream& COUT,youtube_channel& ytc)
{
	COUT << "name: " << ytc.name << std::endl;
	COUT << "subscriber_count: " << ytc.subscriber_count << std::endl;
	return COUT;
}

std::ostream& operator<<(std::ostream& COUT,my_collection& mycol)
{
	for(youtube_channel yt:mycol.my_channels)
	{
		COUT << yt << std::endl;
	}
	return COUT;

}

void tester(int type)
{
	switch (type) 
	{
		case global_operator:
			{
				youtube_channel yt1 = youtube_channel("CodeBeauty",75000);
				youtube_channel yt2 = youtube_channel("CodeCamp",175000);

				// we need to overload << operator
				std::cout << yt1 << yt2;
				
				// can be used as normal function
				/* operator<<(std::cout,yt1); */
				break;
			}
		case normal_operator:
			{
				youtube_channel yt1 = youtube_channel("CodeBeauty",75000);
				youtube_channel yt2 = youtube_channel("CodeCamp",175000);
				my_collection mycol;
				mycol += yt1;
				mycol += yt2;
				std::cout << mycol;
				break;
			}
		case common_error1:
			{
				youtube_channel yt1 = youtube_channel("CodeBeauty",75000);
				youtube_channel yt2 = youtube_channel("CodeCamp",175000);
				my_collection mycol;
				mycol += yt1;
				mycol += yt2;
				// where error happens
				mycol -= yt2;
				std::cout << mycol;
				// reason: 
				// remove function need == operator
				// we need overload that operator also
				break;
			}
		default:
			{
				std::cout << "please choose a knowledge_type " << std::endl;
			}


	}
}

int main()
{
	tester(common_error1);
	std::cin.get();
}
