from .piece import Piece

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'N' if color == 'White' else 'n'

    def valid_moves(self, board):
        moves = []
        x, y = self.position

        potential_moves = [
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 2, y + 1), (x + 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2)
        ]

        for move in potential_moves:
            if self.is_within_bounds(move) and self.is_valid_move(move, board):
                moves.append(move)

        return moves

    def is_within_bounds(self, position):
        x, y = position
        return 0 <= x < 8 and 0 <= y < 8

    def is_valid_move(self, position, board):
        target_piece = board.board[position[0]][position[1]]
        if target_piece is None:
            return True
        return target_piece.color != self.color