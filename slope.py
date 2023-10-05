# Programmer: 
# Description: Calculate the slope between two points.

from fractions import Fraction

# Get the points file name from the user
points_file_name = input("Enter the points file: ")
print()

# Read the points from the file
points_file = open(points_file_name, "r")
x1, y1 = points_file.readline().rstrip().split(",")
x2, y2 = points_file.readline().rstrip().split(",")
points_file.close()

# Convert the coordinates to integers
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

# Calculate the slope as a fractions
slope = Fraction(y2 - y1, x2 - x1)

# Print the slope
print(f"The slope is {slope}")
