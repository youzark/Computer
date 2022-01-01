package sudoku.computationLogic;

import java.util.ArrayList;

public class GridWithImplication {
	public int value;
	public ArrayList<Integer> alternatives;
	public int choices;
	public GridWithImplication(int value, ArrayList<Integer> alternatives, int choices) {
		this.value = value;
		this.alternatives = alternatives;
		this.choices = choices;
	}
    public void removeGivenAlternative(int value) {
		if(alternatives.contains(value)) {
			alternatives.remove(Integer.valueOf(value));
		}
    }
}
