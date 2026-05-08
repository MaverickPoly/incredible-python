from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    def __repr__(self):
        return f"Square(width={self.width}, height={self.height})"

    def __str__(self):
        return f"Square(width={self.width}, height={self.height})"
