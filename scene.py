# Example 2

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, draw_circle_with_vert_grad, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_height, scene_width)

    draw_ground(canvas, scene_height, scene_width)

    draw_cloud(canvas, 650, 400, 50)
    draw_cloud(canvas, 550, 350, 50)
    draw_cloud(canvas, 150, 350, 50)
    draw_cloud(canvas, 250, 400, 50)

    draw_sun(canvas, 400, 350, 50)

    draw_mountain(canvas, 300, 150, scene_height)
    draw_mountain(canvas, 500, 150, scene_height)
    draw_mountain(canvas, 200, 100, scene_height)
    draw_mountain(canvas, 600, 100, scene_height)
    
    # Draw a forest
    draw_pine_tree(canvas, 100, 90, 150)
    draw_pine_tree(canvas, 200, 90, 150)
    draw_pine_tree(canvas, 600, 90, 150)
    draw_pine_tree(canvas, 700, 90, 150)


    draw_lake(canvas, 400, 120, 150)
    draw_cloud(canvas, 365, 93, 25) # The reflection of the clouds in the lake

    draw_name(canvas, 730, 20, "Amon Reis")

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_height, scene_width):
    """Draw the sky."""
    top_y = scene_height
    top_X = scene_width
    
    draw_rectangle(canvas, 0, 0, top_X, top_y, width=0, fill="skyBlue3")

def draw_cloud(canvas, center_x, bottom, height):
    """Draw the clouds in the sky"""
    cloud_width = height * 3
    cloud_height = height
    left_cloud = center_x - cloud_width / 2
    cloud_bottom = bottom
    right_cloud = center_x + cloud_width / 2
    cloud_top = bottom + cloud_height
    draw_oval(canvas, left_cloud, cloud_bottom, right_cloud, cloud_top, width=0, fill="white")
    draw_oval(canvas, left_cloud +20, cloud_bottom - 20, right_cloud + 20, cloud_top -20, width=0, fill="white")


def draw_ground(canvas, scene_height, scene_width):
    """Draw the ground"""
    top_x = scene_width
    top_y = scene_height / 2.5

    draw_rectangle(canvas, 0, 0, top_x, top_y, width=0, fill="lawnGreen")

def draw_mountain(canvas, center_x, height, scene_height):
    mountain_width = height * 2
    mountain_left = center_x - mountain_width / 2 
    mountain_right = center_x + mountain_width / 2
    mountain_bottom = scene_height / 2.5
    peak_X = center_x
    peak_y = mountain_bottom + height
    
    draw_polygon(canvas, mountain_left, mountain_bottom, peak_X, peak_y, mountain_right, mountain_bottom, outline="rosyBrown4", fill="rosyBrown4")

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing"""
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, width=0, fill="tan3")

    skirt_width = height / 2
    peak_x = center_x
    skirt_bottom = trunk_top
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    peak_y = bottom + height
    # Draw the crown of a pine tree 
    draw_polygon(canvas, skirt_left - 10, skirt_bottom, peak_x, peak_y - 10, skirt_right + 10, skirt_bottom, outline="dark green", fill="dark green")
    draw_polygon(canvas, skirt_left -10, skirt_bottom + 25, peak_x, peak_y - 10, skirt_right + 10, skirt_bottom + 25, outline="dark green", fill="dark green")
    draw_polygon(canvas, skirt_left -5, skirt_bottom + 55, peak_x, peak_y - 10, skirt_right + 5, skirt_bottom + 55, outline="dark green", fill="dark green")
    draw_polygon(canvas, skirt_left -3, skirt_bottom + 80, peak_x, peak_y - 10, skirt_right + 3, skirt_bottom + 80, outline="dark green", fill="dark green")

def draw_lake(canvas, center_x, center_y, width):
    """Draw a lake reflecting the clouds"""
    lake_left = center_x - width / 1.5
    lake_right = center_x + width / 1.5
    lake_top = center_y + width / 3
    lake_bottom = center_y - width / 3
    
    draw_oval(canvas, lake_left, lake_top, lake_right, lake_bottom, width=0, outline="rosyBrown4", fill="steelBlue1")

def draw_sun(canvas, center_x, center_y, radius):
    """Draw the sun with gradient colors"""
    draw_circle_with_vert_grad(canvas, center_x, center_y, radius, color_center=[255,69,0], color_edge=[255, 140, 0])

def draw_name(canvas, center_x, center_y, text):
    """Draw my name"""
    draw_text(canvas, center_x, center_y, text, fill="Black")

# Call the main function so that
# this program will start executing.
main()
