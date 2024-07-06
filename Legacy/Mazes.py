from turtle import *

def draw_maze_line(turtle, room_size, pen_up, segments):
    """ Draw a line in a maze in segments.

        The parameter room_size is the width of a square room
        in the maze in pixels. If go_right = 1, the line will
        be drawn to the right, otherwise to the left. If
        pen_up = 1, then the first segment will be drawn with
        the pen_up (i.e. it will be blank), then the second
        segment with the pen down and so on. If pen_up = 0,
        it will draw the first segment, and skip over the
        second and so on. The parameter segments is a list of
        numbers indicating the length in rooms for each segment.
    """

    
    # Draw the line in segments
    for s in segments:
        if pen_up:
            turtle.up()
        turtle.forward(s*room_size)
        if pen_up:
            turtle.down()
        pen_up = not(pen_up)

