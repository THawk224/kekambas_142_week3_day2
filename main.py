# main.py

# Import the functions from the geometry module
from geometry import circle_area, hypotenuse

# Calculate and print the area of a circle with a radius of 7cm
radius = 7
area = circle_area(radius)
print(f"The area of a circle with a radius of {radius}cm is {area:.2f} square cm.")

# Calculate and print the hypotenuse of a right angle with sides of 3in and 4in
side_a = 3
side_b = 4
hyp = hypotenuse(side_a, side_b)
print(f"The hypotenuse of a right angle with sides of {side_a}in and {side_b}in is {hyp:.2f} inches.")
