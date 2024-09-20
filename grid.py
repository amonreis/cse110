# Example 2

from draw2d import \
    draw_circle_with_vert_grad, draw_oval, draw_rectangle, start_drawing, draw_line, draw_text, finish_drawing

def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Grid", scene_width, scene_height)

    draw_grid(canvas, scene_width, scene_height, 50)
    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


def draw_grid(canvas, width, height, interval, color="black"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)


# Call the main function so that
# this program will start executing.
main()