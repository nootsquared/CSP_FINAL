from .piece import Piece

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'Q' if color == 'White' else 'q'

    def valid_moves(self, board):
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]  # Diagonal and straight directions

        for direction in directions:
            x, y = self.position
            while True:
                x += direction[0]
                y += direction[1]
                if 0 <= x < 8 and 0 <= y < 8:  # Check board boundaries
                    target_piece = board.get_piece((x, y))
                    if target_piece is None:
                        moves.append((x, y))  # Empty square
                    elif target_piece.color != self.color:
                        moves.append((x, y))  # Capture opponent's piece
                        break
                    else:
                        break  # Blocked by own piece
                else:
                    break  # Out of bounds

        return moves

    def __str__(self):
        return f"{self.color} Queen"