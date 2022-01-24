package sudoku.computationLogic;

import java.util.Arrays;

import sudoku.problemdomain.SudokuGame;

public class SudokuUtilities {
	public static void copySudokuArrayValue(int[][] oldArray,int[][] newArray) {
		for(int xIndex = 0;xIndex < SudokuGame.GRID_BOUNDARY;xIndex ++) {
			for(int yIndex = 0;yIndex < SudokuGame.GRID_BOUNDARY;yIndex ++) {
				newArray[xIndex][yIndex] = oldArray[xIndex][yIndex];
			}
		}
	}

	public static int[][] copyToNewArray(int[][] oldArray) {
		int[][] newArray = new int[SudokuGame.GRID_BOUNDARY][SudokuGame.GRID_BOUNDARY];
		for(int xIndex = 0;xIndex < SudokuGame.GRID_BOUNDARY;xIndex ++) {
			for(int yIndex = 0;yIndex < SudokuGame.GRID_BOUNDARY;yIndex ++) {
				newArray[xIndex][yIndex] = oldArray[xIndex][yIndex];
			}
		}
		return newArray;
	}

	public static void printBoard(int[][] grid) {
		System.out.println("########################################### ");
		System.out.println("Board: ");
		for(int i = 0; i < SudokuGame.GRID_BOUNDARY;i ++) {
			System.out.println(Arrays.toString(grid[i]));
		}
		System.out.println("########################################### ");
	}
}
