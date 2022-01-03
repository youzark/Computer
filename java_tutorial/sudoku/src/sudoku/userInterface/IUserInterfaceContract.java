package sudoku.userInterface;

import sudoku.computationLogic.InvalidBoardException;
import sudoku.problemdomain.SudokuGame;

public interface IUserInterfaceContract
{
	interface EventListener
	{
		void onSudokuInput(int x,int y,int input);
		void onDialogClick();
		void onNewGameButtonClick();
        void onSolveButtonClicked() throws InvalidBoardException;
        void onEmptyBoardButtonClicked();
	}
	
	interface View
	{
		void setListener(IUserInterfaceContract.EventListener listener);
		void updateSquare(int x,int y,int input);
		void updateBoard(SudokuGame game);
		void showDialog(String message);
		void showError(String message);
	}
}
