package sudoku.computationLogic;
import java.util.ArrayList;
import java.util.PriorityQueue;

import sudoku.problemdomain.Coordinates;
import sudoku.problemdomain.SudokuGame;

public class BoardWithImplication {
	public GridWithImplication [][] impliedGrid;
	private int [][] grid;
	private PriorityQueue<GridWithImplication> gridsToTackle = new PriorityQueue<GridWithImplication>(81);

	public BoardWithImplication(int[][] grid) {
		this.grid = grid;
		initAllImplication();
		makeImplication();
	}

	public void withDrawImplicationAndValueOnOneGrid(Coordinates coordinates) {
	}
	
	public void updateImplicationAndValueOnOneGrid(Coordinates coordinates,int value) {
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		impliedGrid[xIndex][yIndex] = 
			new GridWithImplication(value,
					new ArrayList<Integer>(),
					0);
		makeImplicationInLine(coordinates,value);
		makeImplicationInColumn(coordinates,value);
		makeImplicationInSector(coordinates,value);
	}

	private void makeImplicationInLine(Coordinates coordinates, int value) {
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		for(int y = 0;y < SudokuGame.GRID_BOUNDARY && y != yIndex ; y ++) {
			impliedGrid[xIndex][y].removeGivenAlternative(value);
		}
	}

	private void makeImplicationInColumn(Coordinates coordinates, int value) {
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		for(int x = 0;x < SudokuGame.GRID_BOUNDARY && x != xIndex ; x ++) {
			impliedGrid[x][yIndex].removeGivenAlternative(value);
		}
	}

	private void makeImplicationInSector(Coordinates coordinates, int value) {
		int sectorLocX = (coordinates.getX() / 3) * 3;
		int sectorLocY = (coordinates.getY() / 3) * 3;
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		for(int x = sectorLocX; x < sectorLocX + 3; x++) {
			for(int y = sectorLocY; y < sectorLocY + 3; y++) {
				if(x != xIndex && y != yIndex) {
					impliedGrid[x][y].removeGivenAlternative(value);
				}
			}
		}
	}

	private void initAllImplication() {
		ArrayList<Integer> allAlternatives = new ArrayList<Integer>();
		for (int i = 1; i <= SudokuGame.GRID_BOUNDARY; i ++) {
			allAlternatives.add(i);
		}
		for (int i = 0;i < SudokuGame.GRID_BOUNDARY; i ++) {
			for (int j = 0; j < SudokuGame.GRID_BOUNDARY; j ++) {
				impliedGrid[i][j] = new	GridWithImplication(0,allAlternatives,9);
			}
		}
	}

	private void makeImplication() {
		ArrayList<Coordinates> filledGrids = getFilledGrids(grid);
		for(Coordinates gridPos : filledGrids) {
			updateImplicationAndValueOnOneGrid(gridPos,grid[gridPos.getX()][gridPos.getY()]);
		}
	}

	private ArrayList<Coordinates> getFilledGrids(int[][] grid) {
		ArrayList<Coordinates> filledGrids = new ArrayList<Coordinates>();
		for (int x = 0;x < SudokuGame.GRID_BOUNDARY;x ++) {
			for (int y = 0; y < SudokuGame.GRID_BOUNDARY;y ++) {
				if (grid[x][y] != 0) {
					filledGrids.add(new Coordinates(x, y));
				}
			}
		}
		return filledGrids;
	}

    public boolean isFull() {
		return gridsToTackle.isEmpty();
    }

    public GridWithImplication getNextGrid() {
		return gridsToTackle.poll();
    }

    public int[][] getPuzzle() {
        return grid;
    }

}
