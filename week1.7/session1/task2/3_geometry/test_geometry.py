# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    
    # complete the implementation for
    # testing distance_to()

def test_circle_constructor():
    c = Circle(5)
    assert c.radius == 5
    assert c.centre.x == 0.0
    assert c.centre.y == 0.0
    

# Write test functions to test the __init__(), 
def test_circle_area():
    c = Circle(5)
    assert c.area() == 78.53981633974483
# area() and perimeter() methods in Circle class
def test_circle_perimeter():
    c = Circle(5)
    assert c.perimeter() == 31.41592653589793

def test_circle_constructor_with_centre():
    centre_point = Point(2, 3)
    c = Circle(5, centre_point)
    assert c.radius == 5
    assert c.centre.x == 2
    assert c.centre.y == 3
# you can use the default value for centre coordinates

print(test_circle_constructor_with_centre())
