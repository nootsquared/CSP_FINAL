# Chess Game

This project is a simple command-line chess game implemented in Python. It allows two players to play chess against each other, with a well-defined chessboard displayed in the terminal. Players can select pieces from a menu, view their status and positions, and move them to valid spots on the board while adhering to the rules of chess.

## Project Structure

The project consists of the following files:

- **src/game.py**: Contains the main game logic. Defines the `Game` class with methods to start the game, handle player turns, display menus for piece selection, check the status of pieces, validate moves, and switch turns between players.

- **src/board.py**: Defines the `Board` class, which manages the chessboard's state. Includes methods to initialize the board, print the current state of the board in a well-defined format, and check for valid moves.

- **src/pieces/**: Contains individual files for each chess piece, implementing specific movement logic:
  - **__init__.py**: Initializes the pieces module.
  - **piece.py**: Defines the base `Piece` class with common attributes and methods for all chess pieces.
  - **rook.py**: Implements the `Rook` class.
  - **knight.py**: Implements the `Knight` class.
  - **bishop.py**: Implements the `Bishop` class.
  - **queen.py**: Implements the `Queen` class.
  - **king.py**: Implements the `King` class.
  - **pawn.py**: Implements the `Pawn` class.

- **requirements.txt**: Lists the dependencies required for the project, such as any libraries needed for input handling or game logic.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies listed in `requirements.txt` using pip:
   ```
   pip install -r requirements.txt
   ```

## Gameplay Rules

- The game is played between two players, White and Black, who take turns moving their pieces.
- Players can select a piece from a menu and view its current status and position on the board.
- Moves must adhere to the rules of chess, and the game will validate each move before allowing it.
- The game continues until a checkmate or stalemate condition is reached.

## Running the Game

To start the game, run the following command in your terminal:
```
python src/game.py
```

Enjoy playing chess!