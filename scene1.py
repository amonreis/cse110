# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from turtle import width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_cloud(canvas, 500, 350, 95)
    draw_cloud(canvas, 550, 350, 95)
    draw_cloud(canvas, 600, 350, 80)
    draw_cloud(canvas, 470, 350, 80)
    draw_cloud(canvas, 120, 350, 80)
    draw_cloud(canvas, 150, 350, 95)
    draw_cloud(canvas, 200, 350, 95)
    draw_cloud(canvas, 250, 350, 80)
    draw_pine_tree(canvas, 170, 100, 200)
    draw_pine_tree(canvas, 90, 70, 220)
    draw_pine_tree(canvas, 630, 100, 200)
    draw_pine_tree(canvas, 710, 70, 220)
    draw_house(canvas, 400, 165, 250)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="skyBlue1")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="tan4")

def draw_cloud(canvas, cloud_x, cloud_y, diameter):
    draw_oval(canvas, cloud_x, cloud_y, cloud_x + diameter, cloud_y + diameter, width=0, fill="white")

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree"""

    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="black", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree
    draw_polygon(canvas, center_x, skirt_top, skirt_right, trunk_top, skirt_left, trunk_top, outline="black", width=1, fill="dark green")

def draw_house(canvas, center_x, bottom, height):

    wall_width = height / 2
    wall_height = height / 2
    wall_left = center_x - wall_width 
    wall_right = center_x + wall_width 
    wall_top = bottom + wall_height

    # Draw the walls of the house
    draw_rectangle(canvas, wall_left, wall_top, wall_right, bottom, outline="black", width=1, fill="red3")

    roof_width = wall_width
    roof_height = height - wall_height
    roof_left = wall_left
    roof_right = wall_right
    roof_top = bottom + height / 1.2

    # Draw roof
    draw_polygon(canvas, center_x, roof_top, roof_right, wall_top, roof_left, wall_top, outline="black", width=1, fill="royalBlue")

    door_width = height / 4
    door_height = height / 3
    door_left = center_x - door_width / 1.2
    door_right = center_x + door_width / 1.2
    door_top = bottom + door_height

    # Draw door
    draw_rectangle(canvas, door_left, door_top, door_right, bottom, outline="black", width=1, fill="white")

    diameter = 15
    x = 420
    y = 200
    # Draw a door handle
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill="slateGray")

# Call the main function so that
# this program will start executing.
main()