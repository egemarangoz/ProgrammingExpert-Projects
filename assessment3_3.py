"""
Assessment 3.3 - Geometry Inheritance

Create 4 classes: "Polygon", "Triangle", "Rectangle" and "Square" . The "Triangle" and "Rectangle" class should be subclasses of "Polygon",
and "Square" should be a subclass of "Rectangle".

Your "Polygon" class should raise a NotImplementedError when the get_area() and get_sides() methods are called. However, it should correctly
return the perimeter of the polygon when get_perimeter() is called. Treat the "Polygon" class as an abstract class.

Your "Triangle" class should have a constructor that takes in 3 arguments, which will be the lengths of the 3 sides of the triangle. You may
assume the sides passed to the constructor will always form a valid triangle.

Your "Rectangle" class should have a constructor that takes in 2 arguments, which will be the "width" and "height" of the "Rectangle".

Your "Square" class should have a constructor that takes in 1 argument, which will be the length of each side of the "Square".

Your "Triangle" and "Rectangle" classes should both mplement the following methods:
- get_sides(): This method returns a list containing the lengths of the sides of the shape.

- get_area(): This method should return the area of the polygon.

Your "Square" class should only have an implementation for its constructor, and rely on the "Rectangle" superclass for implementations of
"get_sides() and get_area()."

Note: To calculate the area of a triangle given three side lengths (x, y, z) you can use the following formula:
First calculate the semi perimeter s using: s = (x + y + z) / 2.
Then calculate the area A using: A = math.sqrt(s * (s - x) * (s - y) * (s - z)).
"""

import math


class Polygon:
    # Write your code here.
    def get_area(self):
        raise NotImplementedError
    
    def get_sides(self):
        raise NotImplementedError
    
    def get_perimeter(self):
        return sum(self.get_sides())


class Triangle(Polygon):
    # Write your code here.
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]

    def get_sides(self):
        return self.sides

    def get_area(self):
        side1, side2, side3 = self.sides
        return get_triangle_area(side1, side2, side3)


class Rectangle(Polygon):
    # Write your code here.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_sides(self):
        return [self.width, self.height, self.width, self.height]
    
    def get_area(self):
        return get_rectangle_area(self.width, self.height)


class Square(Rectangle):
    # Write your code here.
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


# Use this function in your solution.
def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )

# Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height

 