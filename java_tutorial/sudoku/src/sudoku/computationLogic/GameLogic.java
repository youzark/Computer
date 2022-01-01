package sudoku.computationLogic;

import sudoku.constants.GameState;
import sudoku.problemdomain.Coordinates;
import sudoku.problemdomain.SudokuGame;

public class GameLogic {

	public static SudokuGame getNewGame() {
		return new SudokuGame( 
				GameState.NEW, 
				GameGenerator.getNewGameGrid());
	}
	
	public static boolean gameIsCompleted(int[][] grid) {
		for(int xIndex = 0; xIndex < SudokuGame.GRID_BOUNDARY; xIndex++) {
			for(int yIndex = 0; yIndex < SudokuGame.GRID_BOUNDARY;yIndex ++) {
				if(grid[xIndex][yIndex] == 0) {
					return false;
				}
			}
		}
		return true;
	}

    public static boolean givenTileIsInvalid(int[][] grid, Coordinates coordinates) {
		if(rowIsInvalid(grid, coordinates)) return true;
		if(columnIsInvalid(grid, coordinates)) return true;
		if(sectionIsInvalid(grid, coordinates)) return true;
        return false;
    }

	private static boolean sectionIsInvalid(int[][] grid, Coordinates coordinates) {
		int sectorLocX = (coordinates.getX() / 3) * 3;
		int sectorLocY = (coordinates.getY() / 3) * 3;
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		for(int x = sectorLocX; x < sectorLocX + 3; x++) {
			for(int y = sectorLocY; y < sectorLocY + 3; y++) {
				if(x != xIndex && y != yIndex && grid[x][y] == grid[xIndex][yIndex]) {
					return true;
				}
			}
		}
		return false;
	}

	private static boolean rowIsInvalid(int[][] grid, Coordinates coordinates) {
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		int y = yIndex;
		for(int x = 0; x < SudokuGame.GRID_BOUNDARY;x ++) {
			if(x != xIndex && grid[x][y] == grid[xIndex][yIndex]) {
				return true;
			}
		}
		return false;
	}

	private static boolean columnIsInvalid(int[][] grid, Coordinates coordinates) {
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		int x = xIndex;
		for(int y = 0; y < SudokuGame.GRID_BOUNDARY;y ++) {
			if(y != yIndex && grid[x][y] == grid[xIndex][yIndex]) {
				return true;
			}
		}
		return false;
	}

    public static boolean SudokuIsInvalid(int[][] grid) {
		for(int xIndex = 0; xIndex < SudokuGame.GRID_BOUNDARY; xIndex++) {
			for(int yIndex = 0; yIndex < SudokuGame.GRID_BOUNDARY;yIndex ++) {
				if(givenTileIsInvalid(grid,new Coordinates(xIndex,yIndex))) ;
				else {
					return false;
				}
			}
		}
        return true;
    }

    public static GameState checkForCompletion(int[][] grid) {
		if(gameIsCompleted(grid)) {
			return GameState.COMPLETE;
		}
		return GameState.ACTIVE;
    }

}

