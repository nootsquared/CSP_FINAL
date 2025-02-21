from .piece import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'P' if color == 'White' else 'p'
        self.has_moved = False

    def valid_moves(self, board):
        moves = []
        direction = 1 if self.color == "White" else -1
        start_row = 1 if self.color == "White" else 6

        forward_move = (self.position[0] + direction, self.position[1])
        if board.is_empty(forward_move):
            moves.append(forward_move)

            if not self.has_moved:
                double_move = (self.position[0] + 2 * direction, self.position[1])
                if board.is_empty(double_move):
                    moves.append(double_move)

        for dx in [-1, 1]:
            diagonal_move = (self.position[0] + direction, self.position[1] + dx)
            if board.is_enemy(diagonal_move, self.color):
                moves.append(diagonal_move)

        return moves

    def move(self, new_position):
        super().move(new_position)
        self.has_moved = True