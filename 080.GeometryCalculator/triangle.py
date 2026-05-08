import math

RADIAN = 57.29


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

        if not self._is_valid():
            raise ValueError("Invalid triangle!")

    def _is_valid(self):
        val_a = self.a >= self.b + self.c
        val_b = self.b >= self.a + self.c
        val_c = self.c >= self.a + self.b

        return all([val_a, val_b, val_c])

    @property
    def a(self): return self._a
    @property
    def b(self): return self._b
    @property
    def c(self): return self._c

    def area(self):
        """Heron's formula"""
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    @staticmethod
    def _cos_theorem(x: float, y: float, z: float):
        return (- pow(x, 2) + pow(y, 2) + pow(z, 2)) / (2 * y * z)

    def angles(self) -> list[float]:
        # Angle in front of side a
        angle_a = math.acos(self._cos_theorem(self.a, self.b, self.c))
        angle_b = math.acos(self._cos_theorem(self.b, self.a, self.c))
        angle_c = math.acos(self._cos_theorem(self.c, self.a, self.b))

        return list(map(lambda x: round(x * RADIAN), [angle_a, angle_b, angle_c]))

    def type_by_angle(self):
        """
        Acute - all angles are less than 90deg
        Right - 90deg
        Obtuse - one angle is greater than 90deg
        :return:
        """
        angles = self.angles()
        max_angle = max(angles)

        if max_angle > 90:
            return "Obtuse"
        elif max_angle == 90:
            return "Right"
        else:
            return "Acute"

    def type_by_side(self):
        """
        Equilateral - all sides equal
        Isosceles - 2 sides equal
        Scalene - no sides equal
        """
        cnt = sum([self.a == self.b, self.a == self.c, self.b == self.c])

        if cnt == 3:
            return "Equilateral"
        elif cnt == 1:
            return "Isosceles"
        else:
            return "Scalene"
