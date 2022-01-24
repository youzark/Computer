import java.util.Iterator;

public class Array <T> implements Iterable <T> 
{
	private T [] arr;
	private int len = 0;
	private int capacity = 0;

	public Array(int capacity) {
		if(capacity < 0)
		{
			throw new IllegalArgumentException("illegal Capacity" + capacity);
		}
		this.capacity = capacity;
		arr = (T[]) new Object[capacity];
	}

	public Array() 
	{
		this(16);
	}

	public int size() 
	{
		return len;
	}
	public boolean is_empty() 
	{
		return len == 0;
	}
	@Override
	public Iterator<T> iterator() {
		// TODO Auto-generated method stub
		return null;
	}

	
}
