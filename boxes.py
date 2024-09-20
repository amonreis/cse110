# Import the math module so that we can call the math.ceil function.
import math

"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python
program named boxes.py that asks the user for two integers:  1) the
number of manufactured items and 2) the number of items that the user
will pack per box. Your program must compute and print the number of
boxes necessary to hold the items. This must be a whole number. Note
that the last box may be packed with fewer items than the other boxes.
"""

# Ask the user for the number of manufactured items to be packed
num_items = int(input("Enter the number of items: "))

# Then we'll ask the user the number of packed items per box
items_per_box = int(input("Enter the number of items per box: "))

# Next we use the math.ceil() function to round a number up to the nearest integer that is greater than or equal to a number
num_boxes = math.ceil(num_items / items_per_box)
print()

print(f"For {num_items} items, packing {items_per_box} per box, you will need {num_boxes} boxes.")