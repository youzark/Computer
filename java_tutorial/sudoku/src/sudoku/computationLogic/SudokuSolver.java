package sudoku.computationLogic;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

import sudoku.problemdomain.Coordinates;
import sudoku.problemdomain.SudokuGame;

public class SudokuSolver {

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
		Stack<Coordinates> emptyCells = getEmptyCells(puzzle);
		return recursiveRandomSolver(puzzle,emptyCells);
	}

	private static boolean recursiveRandomSolver(int[][] puzzle, Stack<Coordinates> emptyCells) {
		List<Integer> possibleNumbers = new ArrayList<>();
		for(int i = 1; i <= SudokuGame.GRID_BOUNDARY; i++) {
			possibleNumbers.add(i);
		}
		Collections.shuffle(possibleNumbers);
		System.out.println(possibleNumbers);
		while(!emptyCells.empty()) {
			Coordinates emptyCell = emptyCells.pop();
			for (int value : possibleNumbers) {
				puzzle[emptyCell.getX()][emptyCell.getY()] = value;
				if(GameLogic.givenTileIsInvalid(puzzle,emptyCell)) {
					puzzle[emptyCell.getX()][emptyCell.getY()] = 0;
					SudokuUtilities.printBoard(puzzle);
				} else {
					SudokuUtilities.printBoard(puzzle);
					if(recursiveRandomSolver(puzzle,emptyCells)) {
						return true;
					} else {
						emptyCells.add(emptyCell);
					}
				}
			}
			return false;
		}
		return true;
	}

	public static boolean solvePuzzleEfficiently(int[][] puzzle) {



		return true;
	}

	private static Stack<Coordinates> getEmptyCells(int[][] puzzle) {
		Stack<Coordinates> emptyCells = new Stack<Coordinates>();
		for (int x = 0;x < SudokuGame.GRID_BOUNDARY;x ++) {
			for (int y = 0; y < SudokuGame.GRID_BOUNDARY;y ++) {
				if (puzzle[x][y] == 0) {
					emptyCells.add(new Coordinates(x, y));
				}
			}
		}
		return emptyCells;
	}

	
}

