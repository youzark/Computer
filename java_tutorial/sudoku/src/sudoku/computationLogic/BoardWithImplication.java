package sudoku.computationLogic;
import java.util.ArrayList;
import java.util.PriorityQueue;

import sudoku.problemdomain.Coordinates;
import sudoku.problemdomain.SudokuGame;

public class BoardWithImplication {
	private GridWithImplication [][] impliedGrid;
	private int [][] grid;
	private PriorityQueue<GridWithImplication> gridsToTackle = new PriorityQueue<GridWithImplication>(81);

	public BoardWithImplication(int[][] grid) throws InvalidBoardException {
		this.grid = grid;
		this.impliedGrid = new GridWithImplication[SudokuGame.GRID_BOUNDARY][SudokuGame.GRID_BOUNDARY];
		try {
			initAllImplication();
		} catch (InvalidBoardException e) {
			throw e;
		}
		initGridPriorityQueue();
	}

	private void initAllImplication() throws InvalidBoardException {
		for (int i = 0;i < SudokuGame.GRID_BOUNDARY; i ++) {
			for (int j = 0; j < SudokuGame.GRID_BOUNDARY; j ++) {
				ArrayList<Integer> allAlternatives = new ArrayList<Integer>();
				for (int k = 1; k <= SudokuGame.GRID_BOUNDARY; k ++) {
					allAlternatives.add(k);
				}
				impliedGrid[i][j] = new	GridWithImplication(0
						,new Coordinates(i,j)
						,allAlternatives
						,9);
			}
		}
		ArrayList<Coordinates> filledGrids = getFilledGrids(grid);
		for(Coordinates gridPos : filledGrids) {
			try {
				maintainImplicationByOneGrid(gridPos,grid[gridPos.getX()][gridPos.getY()]);
			} catch (InvalidBoardException e) {
				throw e;
			}
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

	private void maintainImplicationByOneGrid(Coordinates gridPos, int value) throws InvalidBoardException {
		makeImplicationInLine(gridPos,value);
		makeImplicationInColumn(gridPos,value);
		makeImplicationInSector(gridPos,value);
	}

	private void initGridPriorityQueue() {
		ArrayList<Coordinates> emptyGrids = getEmptyGrids();
		for( Coordinates emptyGrid : emptyGrids ) {
			int xIndex = emptyGrid.getX();
			int yIndex = emptyGrid.getY();
			gridsToTackle.add(impliedGrid[xIndex][yIndex]);
		}
	}

    private ArrayList<Coordinates> getEmptyGrids() {
		ArrayList<Coordinates> emptyGrids = new ArrayList<Coordinates>();
		for (int x = 0;x < SudokuGame.GRID_BOUNDARY;x ++) {
			for (int y = 0; y < SudokuGame.GRID_BOUNDARY;y ++) {
				if (grid[x][y] == 0) {
					emptyGrids.add(new Coordinates(x, y));
				}
			}
		}
		return emptyGrids;
	}

	public boolean isFull() {
		return gridsToTackle.isEmpty();
    }

    public int[][] getPuzzle() {
        return grid;
    }

    public GridWithImplication getNextGridWithMostClearImplication() {
        return gridsToTackle.poll();
    }

    public void updateGrid(Coordinates gridPos, Integer value) throws InvalidBoardException {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		grid[xIndex][yIndex] = value;
		impliedGrid[xIndex][yIndex] = 
			new GridWithImplication(value,
					new Coordinates(xIndex, yIndex),
					new ArrayList<Integer>(),
					0);
		try {
			maintainImplicationByOneGrid(gridPos,value);
		} catch (InvalidBoardException e) {
			throw e;
		}

    }

	private void makeImplicationInLine(Coordinates coordinates, int value) throws InvalidBoardException{
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		for(int y = 0;y < SudokuGame.GRID_BOUNDARY && y != yIndex ; y ++) {
			if(!impliedGrid[xIndex][y].isFilled()) {
				try {
					impliedGrid[xIndex][y].removeGivenAlternative(value);
				} catch (IllegalArgumentException e) {
					throw e;
				}
			}
		}
	}

	private void makeImplicationInColumn(Coordinates coordinates, int value) throws InvalidBoardException{
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		for(int x = 0;x < SudokuGame.GRID_BOUNDARY && x != xIndex ; x ++) {
			if(!impliedGrid[x][yIndex].isFilled()) {
				try {
					impliedGrid[x][yIndex].removeGivenAlternative(value);
				} catch (IllegalArgumentException e) {
					throw e;
				}
			}
		}
	}

	private void makeImplicationInSector(Coordinates coordinates, int value) throws  InvalidBoardException{
		int sectorLocX = (coordinates.getX() / 3) * 3;
		int sectorLocY = (coordinates.getY() / 3) * 3;
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		for(int x = sectorLocX; x < sectorLocX + 3; x++) {
			for(int y = sectorLocY; y < sectorLocY + 3; y++) {
				if(!impliedGrid[x][y].isFilled() && x != xIndex && y != yIndex) {
					try {
						impliedGrid[x][y].removeGivenAlternative(value);
					} catch (IllegalArgumentException e) {
						throw e;
					}
				}
			}
		}
	}

    public void withdrawChangeOnGrid(Coordinates gridPos) {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		int value = grid[xIndex][yIndex];
		impliedGrid[xIndex][yIndex] = 
			new GridWithImplication(value,
					new Coordinates(xIndex, yIndex),
					new ArrayList<Integer>(),
					0);
		withdrawImplicationByOneGrid(gridPos,value);
    }

    private void withdrawImplicationByOneGrid(Coordinates gridPos, int value) {
		withDrawImplicationOnLine(gridPos,value);
		withDrawImplicationOnColumn(gridPos,value);
		withDrawImplicationOnSector(gridPos,value);
	}

	private void withDrawImplicationOnSector(Coordinates gridPos, int value) {
		int sectorLocX = (gridPos.getX() / 3) * 3;
		int sectorLocY = (gridPos.getY() / 3) * 3;
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		for(int x = sectorLocX; x < sectorLocX + 3; x++) {
			for(int y = sectorLocY; y < sectorLocY + 3; y++) {
				if(x != xIndex && y != yIndex) {
					impliedGrid[x][y].addGivenAlternative(value);
				}
			}
		}
	}

	private void withDrawImplicationOnColumn(Coordinates gridPos, int value) {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		for(int x = 0;x < SudokuGame.GRID_BOUNDARY && x != xIndex ; x ++) {
			impliedGrid[x][yIndex].addGivenAlternative(value);
		}
	}

	private void withDrawImplicationOnLine(Coordinates gridPos, int value) {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		for(int y = 0;y < SudokuGame.GRID_BOUNDARY && y != yIndex ; y ++) {
			impliedGrid[xIndex][y].addGivenAlternative(value);
		}
	}

	public void setWithdrawedGridasUntackled(Coordinates gridPos) {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		gridsToTackle.add(impliedGrid[xIndex][yIndex]);
    }
}
