import math



class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def length(self):
        return self.diameter() * math.pi

    def area(self):
        return pow(self.radius, 2) * math.pi

    def diameter(self):
        return 2 * self.radius
        
    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __str__(self):
        return f"Circle(radius={self.radius})"
