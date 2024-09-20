# Import the datetime class from the datetime module so
# we can use in this program
from datetime import datetime

# Import the Math module from the math library to use the math.pi function
import math

# Print a description of this program for the user to see.

print("\nThis program computes and outputs the volume of space inside a car tire.\n")

# Get the width, aspect ratio and the diameter from the user.
width = int(input("Enter the width of the tire in mm (ex 205): "))
a_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Compute the volume of space inside a tire
volume = math.pi * (width **2) * a_ratio * ((width * a_ratio) + (2540 * diameter)) / 10000000000

# Round the volume to one digit after the decimal point.
volume = round(volume, 2)

# Call the now() method to get the current date and time from 
# the computer's operating system and store it in a variable
current_date_time = datetime.now()


# Print the volume of space in the tire
print(F"\nThe approximate volume inside the tire is {volume} liters")

with open("volumes1.txt", "at") as volumes:
    print(f"{current_date_time:%Y-%m-%d}, {width}, {a_ratio}, {diameter}, {volume}", file=volumes)

