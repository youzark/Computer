package sudoku.computationLogic;

import java.util.ArrayList;
import sudoku.problemdomain.Coordinates;
import sudoku.problemdomain.SudokuGame;

public class SudokuSolver {

	public static boolean puzzleIsSolvable(int[][] puzzle) {
		for(int i = 0;i < SudokuGame.GRID_BOUNDARY; i ++) {
			for (int j = 0;j < SudokuGame.GRID_BOUNDARY; j++) {
				if(puzzle[i][j] == 0) {
					for ( int value = 0;value < SudokuGame.GRID_BOUNDARY;value ++) {
						puzzle[i][j] = value;
						if(GameLogic.givenTileIsvalid(puzzle,new Coordinates(i,j))) {
							return puzzleIsSolvable(puzzle);
						} else {
							puzzle[i][j] = 0;
						}
					}
					return false;
				}
			}
		}
		return true;
	}

	private static ArrayList<Coordinates> getEmptyCells(int[][] puzzle) {
		ArrayList<Coordinates> emptyCells = new ArrayList<Coordinates>();
		for (int y = 0;y < SudokuGame.GRID_BOUNDARY;y ++) {
			for (int x = 0; x < SudokuGame.GRID_BOUNDARY;x ++) {
				if (puzzle[x][y] == 0) {
					emptyCells.add(new Coordinates(x, y));
				}
			}
		}
		return emptyCells;
	}
}

