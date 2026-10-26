import math

class Point:
    """
    A Point in 2D space.
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self) -> float:
        """Return the distance from this point to the origin (0, 0)."""
        return math.hypot(self.x, self.y)

    def distance_to(self, other: "Point") -> float:
        """Return the distance from this point to another Point."""
        return math.hypot(self.x - other.x, self.y - other.y)

class Circle:
    """
    A Circle in 2D space.
    """
    def __init__(self, center: Point, radius: float):
        """
        Create a Circle object.
        :param center: A Point object representing the center of the circle.
        :param radius: A float representing the radius of the circle.
        """
        self.center = center
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius
