package sudoku.buildLogic;

import java.io.IOException;

import sudoku.computationLogic.GameLogic;
import sudoku.persistence.LocalStorageImpl;
import sudoku.problemdomain.IStorage;
import sudoku.problemdomain.SudokuGame;
import sudoku.userInterface.IUserInterfaceContract;
import sudoku.userInterface.IUserInterfaceContract.View;
import sudoku.userInterface.logic.ControlLogic;

public class SudokuBuildLogic {

    public static void build(View uiImpl) throws IOException {
		SudokuGame initGameState;
		IStorage storage = new LocalStorageImpl();


		try {
			initGameState = storage.getGameData();
		} catch (IOException e) {
			initGameState = GameLogic.getNewGame();
			storage.updateGameData(initGameState);
		}

		IUserInterfaceContract.EventListener uiLogic = 
			new ControlLogic(storage, uiImpl);
		 
		uiImpl.setListener(uiLogic);
		uiImpl.updateBoard(initGameState);
    }
}

