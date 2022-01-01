package sudoku.userInterface.logic;

import java.io.IOException;

import sudoku.computationLogic.GameLogic;
import sudoku.constants.GameState;
import sudoku.constants.Messages;
import sudoku.problemdomain.Coordinates;
import sudoku.problemdomain.IStorage;
import sudoku.problemdomain.SudokuGame;
import sudoku.userInterface.IUserInterfaceContract;
import sudoku.userInterface.IUserInterfaceContract.View;

public class ControlLogic implements IUserInterfaceContract.EventListener {

	private IStorage storage;
	private IUserInterfaceContract.View view;

	public ControlLogic(IStorage storage, View view) {
		this.storage = storage;
		this.view = view;
	}

	@Override
	public void onSudokuInput(int x, int y, int input) {
		try {
			SudokuGame gameData = storage.getGameData();
			int[][] newGridState = gameData.getGridStateCopy();
			newGridState[x][y] = input;

			if(!GameLogic.givenTileIsInvalid(newGridState, new Coordinates(x,y))) {
				gameData = new SudokuGame(
						GameLogic.checkForCompletion(newGridState),
						newGridState
						);
				storage.updateGameData(gameData);
				view.updateSquare(x, y, input);
				if (gameData.getGameState() == GameState.COMPLETE) {
					view.showDialog(Messages.GAME_COMPELTE);
				}
			} 
		} catch (IOException e) {
			e.printStackTrace();
			view.showError(Messages.ERROR);
		}
	}

	@Override
	public void onDialogClick() {
		try {
			storage.updateGameData(
					GameLogic.getNewGame()
					);
			view.updateBoard(storage.getGameData());

		}
		catch (IOException e) {
			view.showError(Messages.ERROR);
		}
	}

	@Override
	public void onNewGameButtonClick() {
		System.out.println("test");
		try {
			storage.updateGameData(
					GameLogic.getNewGame()
					);
			view.updateBoard(storage.getGameData());

		}
		catch (IOException e) {
			view.showError(Messages.ERROR);
		}
	}
}


