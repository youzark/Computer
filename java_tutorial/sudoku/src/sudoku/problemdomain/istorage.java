package sudoku.problemdomain;
import java.io.IOException;

public interface istorage 
{
	void update_game_data(sudokugame game) throws IOException;
	sudokugame get_game_data() throws IOException; 
}
