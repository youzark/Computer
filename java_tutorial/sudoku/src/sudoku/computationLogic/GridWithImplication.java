package sudoku.computationLogic;

import java.util.ArrayList;

import sudoku.problemdomain.Coordinates;

public class GridWithImplication implements Comparable<GridWithImplication>{
	public int value;
	public ArrayList<Integer> alternatives;
	public int choices;
	private Coordinates coordinate;
	public GridWithImplication( int value,Coordinates coord ) {
		this.value = value;
		this.coordinate = coord;
	}
	public GridWithImplication(int value, ArrayList<Integer> alternatives, int choices) {
		this.value = value;
		this.alternatives = alternatives;
		this.choices = choices;
	}
    public void removeGivenAlternative(int value) throws InvalidBoardException{
		if(alternatives.contains(value)) {
			alternatives.remove(Integer.valueOf(value));
			choices --;
			if(choices <= 0) {
				throw new InvalidBoardException("no Choice left!");
			}
		}
    }

	@Override
	public int compareTo(GridWithImplication other) {
		if(choices > other.choices) {
			return 1;
		} else if (choices < other.choices) {
			return -1;
		} else {
			return 0;
		}
	}
    public ArrayList<Integer> getAlternatives() {
		return alternatives;
    }
    public Coordinates getCoordinates() {
		return coordinate;
    }
    public boolean noChoiceLeft() {
		return choices == 0;
    }
    public void addGivenAlternative(int value) {
		alternatives.add(value);
    }
    public boolean isFilled() {
        return false;
    }
}
