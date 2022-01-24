package sudoku;
import java.io.IOException;

import javafx.application.Application;
import javafx.stage.Stage;
import sudoku.buildLogic.SudokuBuildLogic;
import sudoku.userInterface.IUserInterfaceContract;
import sudoku.userInterface.UserInterfaceImpl;


public class SudokuApplication extends Application {
	private IUserInterfaceContract.View uiImpl;

	@Override
	public void start(Stage primaryStage) throws IOException {
		uiImpl = new UserInterfaceImpl(primaryStage);
		try {
			SudokuBuildLogic.build(uiImpl);
		} catch (IOException e) {
			e.printStackTrace();
			throw e;
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}

