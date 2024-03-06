# geometry.py

import math

def circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters:
    - radius: The radius of the circle.

    Returns:
    The area of the circle.
    """
    return math.pi * radius ** 2

def hypotenuse(side_a, side_b):
    """
    Find the hypotenuse of a right-angled triangle given its two other sides.

    Parameters:
    - side_a: One side of the right-angled triangle.
    - side_b: The other side of the right-angled triangle.

    Returns:
    The length of the hypotenuse.
    """
    return math.sqrt(side_a ** 2 + side_b ** 2)
