from .piece import Piece

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'R' if color == 'White' else 'r'

    def valid_moves(self, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in directions:
            x, y = self.position
            while True:
                x += direction[0]
                y += direction[1]
                if 0 <= x < 8 and 0 <= y < 8:
                    target_piece = board.get_piece((x, y))
                    if target_piece is None:
                        moves.append((x, y))
                    elif target_piece.color != self.color:
                        moves.append((x, y))
                        break
                    else:
                        break
                else:
                    break

        return moves

    def __str__(self):
        return f"{self.color} Rook"