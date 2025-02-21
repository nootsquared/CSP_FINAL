class Game:
    def __init__(self):
        self.board = None
        self.current_turn = "White"
        self.game_over = False

    def start_game(self):
        from board import Board
        self.board = Board()
        self.board.initialize_board()
        while not self.game_over:
            self.board.print_board()
            self.player_turn()
            self.check_winner()
            self.switch_turn()

    def player_turn(self):
        print(f"{self.current_turn}'s turn")
        piece_type = self.display_menu()
        piece_status = self.get_piece_status(piece_type)
        print(piece_status)
        move_from, move_to = self.get_move_input()
        if self.validate_move(move_from, move_to):
            self.move_piece(move_from, move_to)
        else:
            print("Invalid move. Please try again.")

    def display_menu(self):
        print("Select a piece type:")
        print("1. Rook")
        print("2. Knight")
        print("3. Bishop")
        print("4. Queen")
        print("5. King")
        print("6. Pawn")
        choice = input("Enter the number of your choice: ")
        piece_map = {
            "1": "Rook",
            "2": "Knight",
            "3": "Bishop",
            "4": "Queen",
            "5": "King",
            "6": "Pawn"
        }
        return piece_map.get(choice, "Pawn")

    def get_piece_status(self, piece_type):
        status = []
        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]
                if piece and piece.__class__.__name__.lower() == piece_type.lower() and piece.color == self.current_turn:
                    position = chr(col + ord('A')) + str(8 - row)
                    status.append(f"{piece_type} at {position}")
        return "\n".join(status) if status else f"No {piece_type}s on the board."

    def get_move_input(self):
        move_from = input("Enter the position of the piece to move (e.g., E2): ")
        move_to = input("Enter the position to move to (e.g., E4): ")
        return move_from, move_to

    def validate_move(self, move_from, move_to):
        start_pos = (8 - int(move_from[1]), ord(move_from[0]) - ord('A'))
        end_pos = (8 - int(move_to[1]), ord(move_to[0]) - ord('A'))
        piece = self.board.board[start_pos[0]][start_pos[1]]
        if piece and piece.color == self.current_turn:
            valid_moves = piece.valid_moves(self.board)
            return end_pos in valid_moves
        return False

    def move_piece(self, move_from, move_to):
        start_pos = (8 - int(move_from[1]), ord(move_from[0]) - ord('A'))
        end_pos = (8 - int(move_to[1]), ord(move_to[0]) - ord('A'))
        self.board.move_piece(start_pos, end_pos)

    def check_winner(self):
        pass

    def switch_turn(self):
        self.current_turn = "Black" if self.current_turn == "White" else "White"

if __name__ == "__main__":
    game = Game()
    game.start_game()