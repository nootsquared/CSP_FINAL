class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def initialize_board(self):
        from pieces.rook import Rook
        from pieces.knight import Knight
        from pieces.bishop import Bishop
        from pieces.queen import Queen
        from pieces.king import King
        from pieces.pawn import Pawn

        self.board[0][0] = Rook("White", (0, 0))
        self.board[0][1] = Knight("White", (0, 1))
        self.board[0][2] = Bishop("White", (0, 2))
        self.board[0][3] = Queen("White", (0, 3))
        self.board[0][4] = King("White", (0, 4))
        self.board[0][5] = Bishop("White", (0, 5))
        self.board[0][6] = Knight("White", (0, 6))
        self.board[0][7] = Rook("White", (0, 7))
        for col in range(8):
            self.board[1][col] = Pawn("White", (1, col))

        self.board[7][0] = Rook("Black", (7, 0))
        self.board[7][1] = Knight("Black", (7, 1))
        self.board[7][2] = Bishop("Black", (7, 2))
        self.board[7][3] = Queen("Black", (7, 3))
        self.board[7][4] = King("Black", (7, 4))
        self.board[7][5] = Bishop("Black", (7, 5))
        self.board[7][6] = Knight("Black", (7, 6))
        self.board[7][7] = Rook("Black", (7, 7))
        for col in range(8):
            self.board[6][col] = Pawn("Black", (6, col))

    def print_board(self):
        print("  A B C D E F G H")
        print(" +-----------------+")
        for row in range(8):
            print(f"{8 - row}|", end="")
            for col in range(8):
                piece = self.board[row][col]
                if piece is None:
                    print(".", end=" ")
                else:
                    print(piece.symbol, end=" ")
            print(f"|{8 - row}")
        print(" +-----------------+")

    def is_valid_move(self, piece, start_pos, end_pos):
        valid_moves = piece.valid_moves(self)
        return end_pos in valid_moves

    def move_piece(self, start_pos, end_pos):
        piece = self.board[start_pos[0]][start_pos[1]]
        if piece and self.is_valid_move(piece, start_pos, end_pos):
            self.board[end_pos[0]][end_pos[1]] = piece
            self.board[start_pos[0]][start_pos[1]] = None
            piece.position = end_pos
        else:
            print("Invalid move")

    def is_empty(self, position):
        row, col = position
        return self.board[row][col] is None

    def is_enemy(self, position, color):
        row, col = position
        piece = self.board[row][col]
        return piece is not None and piece.color != color

    def get_piece(self, position):
        row, col = position
        return self.board[row][col]