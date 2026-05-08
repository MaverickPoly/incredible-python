import argparse

from square import Square
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle


def test_square():
    square = Square(4)

    print("====== Square ======")
    print(f"Area: {square.area()}")
    print(f"Perimeter: {square.perimeter()}")
    print(f"Diagonal: {square.diagonal()}")

def test_rect():
    rect = Rectangle(12, 5)

    print("====== Rect ======")
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Diagonal: {rect.diagonal()}")

def test_circle():
    circle = Circle(6)

    print("====== Circle ======")
    print(f"Diameter: {circle.diameter()}")
    print(f"Area: {circle.area()}")
    print(f"Length: {circle.length()}")

def test_triangle():
    triangle = Triangle(11, 5, 5)

    print("====== Triangle ======")
    print(f"Area: {triangle.area()}")
    print(f"Perimeter: {triangle.perimeter()}")
    print(f"Angles: {triangle.angles()}")
    print(f"Type by angle: {triangle.type_by_angle()}")
    print(f"Type by side: {triangle.type_by_side()}")


def main():
    parser = argparse.ArgumentParser(description="Geometry Calculator Tester Script")

    subparsers = parser.add_subparsers(dest="option")

    _ = subparsers.add_parser("square", help="Test Square")
    _ = subparsers.add_parser("rect", help="Test Rectangle")
    _ = subparsers.add_parser("circle", help="Test Circle")
    _ = subparsers.add_parser("triangle", help="Test Triangle")

    args = parser.parse_args()

    match args.option:
        case "square": test_square()
        case "rect": test_rect()
        case "circle": test_circle()
        case "triangle": test_triangle()


if __name__ == '__main__':
    main()
