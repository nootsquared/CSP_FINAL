from .piece import Piece

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'K' if color == 'White' else 'k'
        self.has_moved = False

    def valid_moves(self, board):
        row, col = self.position
        moves = []

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (r, c) != (row, col) and self.is_within_bounds(r, c):
                    target_piece = board.get_piece((r, c))
                    if target_piece is None or target_piece.color != self.color:
                        moves.append((r, c))

        return moves

    def is_within_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def move(self, new_position):
        self.has_moved = True
        self.position = new_position