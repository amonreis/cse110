'''Compute and print the the volume, surface and 
storage efficiency of all 12 can sizes'''

# Import the standard math module so that
# math.pi can be used in this program.
import math

def main():

    compute_volume()
    compute_surface_area()

def compute_volume(radius, height):
    '''Compute and return the volume of a cylinder'''
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    '''Compute and return the surface area of a cylinder'''
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

