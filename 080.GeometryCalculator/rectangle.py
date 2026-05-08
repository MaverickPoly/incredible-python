import math


class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"