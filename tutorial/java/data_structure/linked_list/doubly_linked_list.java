public class doubly_linked_list <T> implements Iterable <T> 
{
	private int size = 0;
	private Node <T> head = null;
	private Node <T> tail = null;
	
	private class Node <T> 
	{
		T data;
		Node <T> prev,next;
		public Node(T data, Node <T> prev, Node <T> next) 
		{
			this.data = data;
			this.prev = prev;
			this.next = next;
		}
		@Override
		public String toString() {
			return "Node [data=" + data + "]";
		}
	}

	public void clear() 
	{
		Node <T> trav = head;
		while(trav != null)
		{
			Node <T> next = trav.next;
			trav.prev = trav.next = null;
			trav.data = null;
			trav = next;
		}
		trav = head = tail = null;
		size = 0;
	}

	public int size()
	{
		return size;
	}

	


}
