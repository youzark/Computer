import java.util.ArrayList;

public class Main 
{
	public static void main(String args[]) 
	{
		Integer[] int_array =  {1,2,3,4,5};
		Double[] double_array = {1.1,2.2,3.4,5.5,6.6};
		Character[] character_array = {'a','b','c','d','e'};
		String[] string_array = {"asd","test","why","so"};
		display_array(int_array );
		display_array(double_array);
		display_array(character_array);
		display_array(string_array);

		my_generical_class<Integer> my_int = new my_generical_class<>(1);
		my_generical_class<Double> my_float = new my_generical_class<>(1.1);
		my_generical_class<Character> my_char = new my_generical_class<>('a');
		my_generical_class<String> my_string = new my_generical_class<>("test");

		ArrayList<String> my_array_list = new ArrayList<>();

		System.out.println(my_int.getI());
		System.out.println(my_char.getI());
		System.out.println(my_float.getI());
		System.out.println(my_string.getI());
	}
	
	public static <T> void display_array(T[] array) 
	{
		for (T i : array) 
		{
			System.out.println(i+" ");
		}
		System.out.println();
	}
}
