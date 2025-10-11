import math

class Shape:
    def area(self):
        """Base method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override area method to calculate rectangle area."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle with a radius."""
        self.radius = radius

    def area(self):
        """Override area method to calculate circle area."""
        return math.pi * (self.radius ** 2)


def main():
    # Create instances of Rectangle and Circle
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Demonstrate polymorphism
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


if __name__ == "__main__":
    main()
