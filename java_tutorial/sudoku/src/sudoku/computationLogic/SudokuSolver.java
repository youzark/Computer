package sudoku.computationLogic;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

import sudoku.problemdomain.Coordinates;
import sudoku.problemdomain.SudokuGame;

public class SudokuSolver {

	private static final int ArrayList = 0;

	public static boolean puzzleIsSolvable(int[][] puzzle) {
		for(int i = 0;i < SudokuGame.GRID_BOUNDARY; i ++) {
			for (int j = 0;j < SudokuGame.GRID_BOUNDARY; j++) {
				if(puzzle[i][j] == 0) {
					for ( int value = 1;value <= SudokuGame.GRID_BOUNDARY;value ++) {
						puzzle[i][j] = value;
						if(GameLogic.givenTileIsInvalid(puzzle,new Coordinates(i,j))) {
							puzzle[i][j] = 0;
						} else {
							return puzzleIsSolvable(puzzle);
						}
					}
					return false;
				}
			}
		}
		return true;
	}

	public static boolean solvePuzzleRandomly(int[][] puzzle) {
		List<Integer> possibleNumbers = new ArrayList<>();
		for(int i = 1; i <= SudokuGame.GRID_BOUNDARY; i++) {
			possibleNumbers.add(i);
		}
		Collections.shuffle(possibleNumbers);
		for(int i = 0;i < SudokuGame.GRID_BOUNDARY; i ++) {
			for (int j = 0;j < SudokuGame.GRID_BOUNDARY; j++) {
				if(puzzle[i][j] == 0) {
					for ( int value : possibleNumbers) {
						puzzle[i][j] = value;
						if(GameLogic.givenTileIsInvalid(puzzle,new Coordinates(i,j))) {
							puzzle[i][j] = 0;
							SudokuUtilities.printBoard(puzzle);
						} else {
							SudokuUtilities.printBoard(puzzle);
							return solvePuzzleRandomly(puzzle);
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

