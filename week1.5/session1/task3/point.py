import math


class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self) -> float:
        """Return the distance from this point to the origin (0, 0)."""
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other: "Point") -> float:
        """Return the distance from this point to another Point."""
        return math.hypot(self.x - other.x, self.y - other.y)


# Finally, add code here to demonstrate use of Point
if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(6, 8)

    print(f"Distance of p1 from origin: {p1.distance():.2f}")
    print(f"Distance of p2 from origin: {p2.distance():.2f}")
    print(f"Distance between p1 and p2: {p1.distance_to(p2):.2f}")
