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
				if(grid[i][j] == 0) {
					impliedGrid[i][j] = new	GridWithImplication(grid[i][j]
							,new Coordinates(i,j)
							,allAlternatives
							,9);

				} else {
					impliedGrid[i][j] = new	GridWithImplication(grid[i][j]
							,new Coordinates(i,j)
							,new ArrayList<Integer>()
							,0);
				}
			}
		}
		ArrayList<Coordinates> filledGrids = getFilledGrids(grid);
		for(Coordinates gridPos : filledGrids) {
			// System.out.println("####################");
			// System.out.println(gridPos);
			// System.out.println(grid[gridPos.getX()][gridPos.getY()]);
			// System.out.println("####################");
			// printQueue();
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

	private void makeImplicationInLine(Coordinates coordinates, int value) throws InvalidBoardException{
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		for(int y = 0;y < SudokuGame.GRID_BOUNDARY ; y ++) {
			if(!impliedGrid[xIndex][y].isFilled() && y != yIndex) {
				try {
					impliedGrid[xIndex][y].removeGivenAlternative(value);
					gridsToTackle.remove(impliedGrid[xIndex][y]);
					gridsToTackle.add(impliedGrid[xIndex][y]);
				} catch (IllegalArgumentException e) {
					throw e;
				}
			}
		}
	}

	private void makeImplicationInColumn(Coordinates coordinates, int value) throws InvalidBoardException{
		int xIndex = coordinates.getX();
		int yIndex = coordinates.getY();
		for(int x = 0;x < SudokuGame.GRID_BOUNDARY ; x ++) {
			if(!impliedGrid[x][yIndex].isFilled() && x != xIndex) {
				try {
					impliedGrid[x][yIndex].removeGivenAlternative(value);
					gridsToTackle.remove(impliedGrid[x][yIndex]);
					gridsToTackle.add(impliedGrid[x][yIndex]);
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
						gridsToTackle.remove(impliedGrid[x][y]);
						gridsToTackle.add(impliedGrid[x][y]);
					} catch (IllegalArgumentException e) {
						throw e;
					}
				}
			}
		}
	}

	private void initGridPriorityQueue() {
		PriorityQueue<GridWithImplication> gridsToTackle = new PriorityQueue<GridWithImplication>(81);
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
		try {
			impliedGrid[xIndex][yIndex] = 
				new GridWithImplication(value,
						new Coordinates(xIndex, yIndex),
						new ArrayList<Integer>(),
						0);
			maintainImplicationByOneGrid(gridPos,value);
		} catch (InvalidBoardException e) {
			throw e;
		}

    }


    public void withdrawChangeOnGrid(Coordinates gridPos) {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		int value = grid[xIndex][yIndex];
		grid[xIndex][yIndex] = 0;
		ArrayList<Integer> allAlternatives = getAlternativesOnOneGrid(gridPos);
		impliedGrid[xIndex][yIndex] = 
			new GridWithImplication(0,
					new Coordinates(xIndex, yIndex),
					allAlternatives,
					allAlternatives.size());
		withdrawImplicationByOneGrid(gridPos,value);
    }

    private ArrayList<Integer> getAlternativesOnOneGrid(Coordinates gridPos) {
		ArrayList<Integer> allAlternatives = new ArrayList<>();
		for (int k = 1; k <= SudokuGame.GRID_BOUNDARY; k ++) {
			allAlternatives.add(k);
		}
		reduceAlternativesOnLine(gridPos,allAlternatives);
		reduceAlternativesOnColumn(gridPos,allAlternatives);
		reduceAlternativesOnSector(gridPos,allAlternatives);
		return allAlternatives;
	}

	private void reduceAlternativesOnSector(Coordinates gridPos, ArrayList<Integer> allAlternatives) {
		int sectorLocX = (gridPos.getX() / 3) * 3;
		int sectorLocY = (gridPos.getY() / 3) * 3;
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		for(int x = sectorLocX; x < sectorLocX + 3; x++) {
			for(int y = sectorLocY; y < sectorLocY + 3; y++) {
				if(x != xIndex && y != yIndex && grid[x][y] != 0) {
					allAlternatives.remove(Integer.valueOf(grid[x][y]));
				}
			}
		}
	}

	private void reduceAlternativesOnColumn(Coordinates gridPos, ArrayList<Integer> allAlternatives) {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		for(int x = 0;x < SudokuGame.GRID_BOUNDARY && x != xIndex ; x ++) {
			if(grid[x][yIndex] !=0 && x != xIndex) {
				allAlternatives.remove(Integer.valueOf(grid[x][yIndex]));
			}
		}
	}

	private void reduceAlternativesOnLine(Coordinates gridPos, ArrayList<Integer> allAlternatives) {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		for(int y = 0;y < SudokuGame.GRID_BOUNDARY && y != yIndex ; y ++) {
			if(grid[xIndex][y] !=0 && y != yIndex) {
				allAlternatives.remove(Integer.valueOf(grid[xIndex][y]));
			}
		}
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
					gridsToTackle.remove(impliedGrid[x][y]);
					gridsToTackle.add(impliedGrid[x][y]);
				}
			}
		}
	}

	private void withDrawImplicationOnColumn(Coordinates gridPos, int value) {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		for(int x = 0;x < SudokuGame.GRID_BOUNDARY ; x ++) {
			if(!impliedGrid[x][yIndex].isFilled() && x != xIndex) {
				impliedGrid[x][yIndex].addGivenAlternative(value);
				gridsToTackle.remove(impliedGrid[x][yIndex]);
				gridsToTackle.add(impliedGrid[x][yIndex]);
			}
		}
	}

	private void withDrawImplicationOnLine(Coordinates gridPos, int value) {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		for(int y = 0;y < SudokuGame.GRID_BOUNDARY && y != yIndex ; y ++) {
			if(!impliedGrid[xIndex][y].isFilled() && y != yIndex) {
				impliedGrid[xIndex][y].addGivenAlternative(value);
				gridsToTackle.remove(impliedGrid[xIndex][y]);
				gridsToTackle.add(impliedGrid[xIndex][y]);
			}
		}
	}

	public void setWithdrawedGridasUntackled(Coordinates gridPos) {
		int xIndex = gridPos.getX();
		int yIndex = gridPos.getY();
		gridsToTackle.add(impliedGrid[xIndex][yIndex]);
    }

    public void printQueue() {
		for(GridWithImplication grid : gridsToTackle) {
			System.out.println(grid.getCoordinates().toString() + grid.getAlternatives());
		}
    }
}
