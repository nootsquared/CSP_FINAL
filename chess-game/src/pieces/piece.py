class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def move(self, new_position):
        if self.is_valid_move(new_position):
            self.position = new_position
            return True
        return False

    def is_valid_move(self, new_position):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def get_position(self):
        return self.position

    def get_color(self):
        return self.color

    def __str__(self):
        return f"{self.color} {self.__class__.__name__} at {self.position}"