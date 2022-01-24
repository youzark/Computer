package sudoku.problemdomain;
import java.io.Serializable;

import sudoku.computationLogic.SudokuUtilities;
import sudoku.constants.GameState;

public class SudokuGame implements Serializable
{
	private final GameState game_state;
	private final int[][] grid_state;
	
	public static final int GRID_BOUNDARY = 9;

	public SudokuGame(GameState game_state, int[][] grid_state)
	{
		this.game_state = game_state;
		this.grid_state = grid_state;
	}

	public GameState getGameState() {
		return game_state;
	}

	public int[][] getGridStateCopy() {
		return SudokuUtilities.copyToNewArray(grid_state);
	}
}
