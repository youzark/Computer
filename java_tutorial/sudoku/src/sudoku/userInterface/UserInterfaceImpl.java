package sudoku.userInterface;

import java.util.HashMap;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
import javafx.scene.control.Dialog;
import javafx.scene.control.TextField;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.Background;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import sudoku.computationLogic.InvalidBoardException;
import sudoku.constants.GameState;
import sudoku.problemdomain.Coordinates;
import sudoku.problemdomain.SudokuGame;
import sudoku.userInterface.IUserInterfaceContract.EventListener;

public class UserInterfaceImpl implements IUserInterfaceContract.View, EventHandler<KeyEvent> 
{
	private final Stage stage;
	private final Group root;

	private HashMap<Coordinates, SudokuTextField> textFieldCoordinates;
	private IUserInterfaceContract.EventListener listener;

	private static final double WINDOW_Y = 732;
	private static final double WINDOW_X = 868;
	private static final double BOARD_PADDING = 50;
	private static final double BOARD_X_AND_Y = 576;
	private static final double BUTTON_WIDTH = 100;
	private static final double BUTTON_HEIGHT = 30;
	private static final double BUTTON_PADDING = 658;
	
	private static final Color WINDOW_BACKGROUND_COLOR = Color.rgb(0, 150, 136);
	private static final Color BOARD_BACKGROUND_COLOR = Color.rgb(224, 242, 241);
	private static final String SUDOKU = "Sudoku";

	public UserInterfaceImpl(Stage stage) {
		this.stage = stage;
		this.root = new Group();
		this.textFieldCoordinates = new HashMap<>();
		initializeUserInterface();
	}

	private void initializeUserInterface() 
	{
		drawBackground(root);
		drawTitle(root);
		drawSudokuBoard(root);
		drawTextFields(root);
		drawGridLines(root);
		drawButton();
		stage.show();
	}

	public void drawButton() {
		Button newGame = drawNewGame();
		Button Solve = drawSolveButton();
		Button emptyBoard = drawEmptyBoardButton();
		// Button withdraw = drawWithdraw();
		root.getChildren().addAll(newGame,
				Solve,
				emptyBoard);
	}

	// private Button drawWithdraw() {
	// 	Button load = new Button();
	// 	load.setText("Withdraw");
	// 	load.setFont(Font.font("Arial",30));
	// 	load.setLayoutX(BUTTON_PADDING);
	// 	load.setLayoutY(BOARD_PADDING + 80);
	// 	load.setMinWidth(BUTTON_WIDTH);
	// 	load.setMinHeight(BUTTON_HEIGHT);
	// 	return load;
	// }


	private Button drawEmptyBoardButton() {
		Button emptyBoard = new Button();
		emptyBoard.setText("Empty Board");
		emptyBoard.setFont(Font.font("Arial",30));
		emptyBoard.setLayoutX(BUTTON_PADDING);
		emptyBoard.setLayoutY(BOARD_PADDING + 150);
		emptyBoard.setMinWidth(BUTTON_WIDTH);
		emptyBoard.setMinHeight(BUTTON_HEIGHT);
		emptyBoard.setOnAction(event -> {
			listener.onEmptyBoardButtonClicked();
			event.consume();
		});
		return emptyBoard;
	}

	private Button drawSolveButton() {
		Button solve = new Button();
		solve.setText("Solve");
		solve.setFont(Font.font("Arial",30));
		solve.setLayoutX(BUTTON_PADDING);
		solve.setLayoutY(BOARD_PADDING + 80);
		solve.setMinWidth(BUTTON_WIDTH);
		solve.setMinHeight(BUTTON_HEIGHT);
		solve.setOnAction(event -> {
			try {
				listener.onSolveButtonClicked();
			} catch (InvalidBoardException e) {
				e.printStackTrace();
			}
			event.consume();
		});
		return solve;
	}

	private Button drawNewGame() {
		Button newGame = new Button();
		newGame.setText("New Game");
		newGame.setFont(Font.font("Arial",30));
		newGame.setLayoutX(BUTTON_PADDING);
		newGame.setLayoutY(BOARD_PADDING + 10);
		newGame.setMinWidth(BUTTON_WIDTH);
		newGame.setMinHeight(BUTTON_HEIGHT);
		newGame.setOnAction(event -> {
			listener.onNewGameButtonClick();
			event.consume();
		});
		return newGame;
	}

	private void drawGridLines(Group root) {
		int xAndy = 114;
		int index = 0;
		while( index < 8 ) {
			int thickness;
			if (index == 2 || index == 5) {
				thickness = 3;
			}
			else {
				thickness = 2;
			}

			Rectangle verticalLine = getLine(
					xAndy + 64 * index,
					BOARD_PADDING,
					BOARD_X_AND_Y,
					thickness
					);
			Rectangle horizontalLine = getLine(
					BOARD_PADDING,
					xAndy + 64 * index,
					thickness,
					BOARD_X_AND_Y
					);
			root.getChildren().addAll(
					verticalLine,
					horizontalLine
					);

			index++;
		}
	}

	private Rectangle getLine(double x, double y, double height, double width) {
		Rectangle line = new Rectangle();

		line.setX(x);
		line.setY(y);
		line.setWidth(width);
		line.setHeight(height);

		line.setFill(Color.BLACK);
		return line;
	}

	private void drawTextFields(Group root) {
		final int xOrigin = 50;
		final int yOrigin = 50;

		final int xAndyDelta = 64;

		for(int xIndex = 0 ; xIndex < SudokuGame.GRID_BOUNDARY ;xIndex ++) {
			for(int yIndex = 0;yIndex < SudokuGame.GRID_BOUNDARY ;yIndex ++) {
				int x = xOrigin + xAndyDelta * xIndex;
				int y = yOrigin + xAndyDelta * yIndex;

				SudokuTextField tile  = new SudokuTextField(xIndex,yIndex);
				styleSudokuTile(tile,x,y);
				tile.setOnKeyPressed(this);

				textFieldCoordinates.put(new Coordinates(xIndex,yIndex), tile);
				
				root.getChildren().add(tile);
			}
		}
	}

	private void styleSudokuTile(SudokuTextField tile, int x, int y) {
		Font numberFont = new Font(32);

		tile.setFont(numberFont);
		tile.setAlignment(Pos.CENTER);

		tile.setLayoutX(x);
		tile.setLayoutY(y);
		tile.setPrefWidth(64);
		tile.setPrefHeight(64);

		tile.setBackground(Background.EMPTY);
	}

	private void drawSudokuBoard(Group root) {
		Rectangle boardBackground = new Rectangle();
		boardBackground.setX(BOARD_PADDING);
		boardBackground.setY(BOARD_PADDING);

		boardBackground.setWidth(BOARD_X_AND_Y);
		boardBackground.setHeight(BOARD_X_AND_Y);
		
		boardBackground.setFill(BOARD_BACKGROUND_COLOR);

		root.getChildren().add(boardBackground);
	}

	private void drawTitle(Group root) {
		Text title = new Text(235,690,SUDOKU);
		title.setFill(Color.WHITE);
		Font font = new Font(43);
		title.setFont(font);
		root.getChildren().add(title);
	}

	private void drawBackground(Group root) {
		Scene scene = new Scene(root, WINDOW_X,WINDOW_Y);
		scene.setFill(WINDOW_BACKGROUND_COLOR);
		stage.setScene(scene);
	}

	@Override
	public void setListener(EventListener listener) {
		this.listener = listener;
	}

	@Override
	public void updateSquare(int x, int y, int input) {
		SudokuTextField tile = textFieldCoordinates.get(new Coordinates(x, y));
		
		String value = Integer.toString(
				input
				);

		if (value.equals("0")) value = "";
		tile.textProperty().setValue(value);

	}

	@Override
	public void updateBoard(SudokuGame game) {
		for(int xIndex = 0;xIndex < SudokuGame.GRID_BOUNDARY;xIndex++) {
			for(int yIndex = 0;yIndex < SudokuGame.GRID_BOUNDARY;yIndex++) {
				TextField tile = textFieldCoordinates.get(new Coordinates(xIndex, yIndex));

				String value = Integer.toString(
						game.getGridStateCopy()[xIndex][yIndex]
						);

				if (value.equals("0")) value = "";

				tile.setText(value);

				if(game.getGameState() == GameState.NEW) {
					if(value.equals("")) {
						tile.setStyle("-fx-opacity: 0.8;");
						tile.setDisable(false);
					} else {
						tile.setStyle("-fx-opacity: 0.8;");
						tile.setDisable(true);
					}
				}
			}
		}
	}

	@Override
	public void showDialog(String message) {
		Alert dialog = new Alert(Alert.AlertType.CONFIRMATION, message, ButtonType.OK);
		dialog.showAndWait();

		if(dialog.getResult() == ButtonType.OK) listener.onDialogClick();
	}

	@Override
	public void showError(String message) {
		Alert dialog = new Alert(Alert.AlertType.ERROR, message, ButtonType.OK);
		dialog.showAndWait();
		
	}

	@Override
	public void handle(KeyEvent event) {
		if (event.getEventType() == KeyEvent.KEY_PRESSED) {
			if(
					event.getText().matches("[0-9]")
			  ) {
				int value = Integer.parseInt(event.getText());
				handleInput(value, event.getSource());
			} else if (
					event.getCode() == KeyCode.BACK_SPACE
					) {
				handleInput(0 , event.getSource());
			} else {
				((TextField) event.getSource()).setText("");
			}
		}
		event.consume();
	}

	private void handleInput(int value, Object source) {
		listener.onSudokuInput(
				 ((SudokuTextField) source).getX(),
				 ((SudokuTextField) source).getY(),
				 value
				 );
	}
}
