# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py
from geometry import Point
from geometry import Circle

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
centre = Point(0, 0)

#  - Creates a Circle object, using the Point object and a value for radius
my_circle = Circle(centre, 5)

#  - Displays the area of the circle
print(f"Area: {my_circle.area()}")

#  - Displays the perimeter of the circle
print(f"Perimeter: {my_circle.perimeter()}")
