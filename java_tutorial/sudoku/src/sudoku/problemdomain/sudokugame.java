package sudoku.problemdomain;

public class sudokugame implements Serializable
{
	private final GameState game_state;
	private final int[][] grid_state;
	
	private static final int GRID_BOUNDARY = 9;

	public sudokugame(GameState game_state, int[][] grid_state)
	{
		this.game_state = game_state;
		this.grid_state = grid_state;
	}

	public GameState getgame_state() {
		return game_state;
	}

	public int[][] getGrid_state() {
		return sudoku_utilities.copy_to_new_array(grid_state);
	}
}
