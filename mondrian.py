"""
CSAP/X Mondrian recursion lab
Author: RIT CS
Author: Colin Rindge

Student starter code for the mondrian square lab.  It prompts for a depth of
recursion (between 1-8) and random subdivisions, and recursively generates
colored rectangles.
"""

import turtle
import random

# depth range for input
MIN_DEPTH=1
MAX_DEPTH=8

# the four colors of rectangles
COLORS = ['blue', 'red', 'white', 'yellow']

# screen dimensions and inlay offset for image
WIDTH = 800
HEIGHT = 800
INLAY = 20

def init(depth: int, rand: bool) -> None:
    """
    Set up the display.  This is called by:
        main
    :param depth: user's desired depth
    :param rand: random subdivisions or not
    """
    # use speed(0) when developing so you can see the animations
    # turtle.speed(0)
    turtle.tracer(0)
    # turtle.tracer(0) when finished developing turn animations of for fastest rendering
    # set screen dimensions
    turtle.Screen().setup(WIDTH, HEIGHT)
    # world coordinates are llx -20, lly -20, urx 820, ury 820
    turtle.setworldcoordinates(-INLAY, -INLAY, WIDTH+INLAY, HEIGHT+INLAY)
    # image will render in llx 0, lly 0, urx 800, ury 800
    turtle.setpos(0,0)
    # black pen outline size is 1
    turtle.pensize(1)
    # title includes key values
    turtle.title(f'Mondrian, depth={depth}, random={rand}, width={WIDTH}, height={HEIGHT}')
    # don't ever show turtle on screen - can be turned off when developing
    turtle.hideturtle()


def draw_rectangle(llx: int, lly: int, urx: int, ury: int, ) -> list:
    """
    Draw a rectangle.
    :param llx: Bottom left point x coordinate
    :param lly: Bottom left point y coordinate
    :param urx: Top right point x coordinate
    :param ury: Top right point y coordinate
    :return: list w/ index and surface area
    """
    index = random.randint(0, 3)
    length = urx-llx
    height = ury-lly
    turtle.fillcolor(COLORS[index])
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    return [index, length*height]

def move_to(x: int, y: int) -> None:
    """
    Pen up, move, pen down
    :param x: X coordinate to move to
    :param y: Y coordinate to move to
    :return: None
    """
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

def add_lists(list1: list, list2: list):
    """
    Add 2 lists together
    :param list1: list w/ int values
    :param list2: list w/ int values
    :return: list with sum of values in old and new
    """
    for i in range(4):
        list1[i] += list2[i]
    return list1


def draw_rectangles_rec(rando: str, depth: int, llx: int, lly: int, urx: int, ury: int) -> list:
    """
    Draw rectangles, but recursively
    :param rando: if y, random subdivisions, if n then not random
    :param depth: # of recursions
    :param llx: Bottom left point x coordinate
    :param lly: Bottom left point y coordinate
    :param urx: Top right point x coordinate
    :param ury: Top right point y coordinate
    :return: list of surface areas
    """
    surface_areas = [0, 0, 0, 0]
    if rando == 'y':
        cx = random.randint(llx, urx)
        cy = random.randint(lly, ury)
    else :
        cx = (llx + urx)//2
        cy = (lly + ury)//2
    if depth == 1:
        alist = draw_rectangle(llx, lly, urx, ury)
        surface_areas[alist[0]] += alist[1]
        return surface_areas
    else:
        new_surface_areas = draw_rectangles_rec(rando, depth-1, llx, lly, cx, cy)
        surface_areas = add_lists(surface_areas, new_surface_areas)
        move_to(cx, lly)
        new_surface_areas = draw_rectangles_rec(rando, depth-1, cx, lly, urx, cy)
        surface_areas = add_lists(surface_areas, new_surface_areas)
        move_to(cx, cy)
        new_surface_areas = draw_rectangles_rec(rando, depth-1, cx, cy, urx, ury)
        surface_areas = add_lists(surface_areas, new_surface_areas)
        move_to(llx, cy)
        new_surface_areas = draw_rectangles_rec(rando, depth-1, llx, cy, cx, ury)
        surface_areas = add_lists(surface_areas, new_surface_areas)
        move_to(llx, lly)
        return surface_areas

def main() -> None:
    """
    The main method.
    """
    # prompt for depth
    depth = 0
    while depth<1 or depth>8:
        depth = int(input('Input Depth (1-8): '))

    rando = input('Randomize subdivisions? (y/n): ')

    # initialize display
    init(depth, False)

    # draw the image
    surface_areas = draw_rectangles_rec(rando, depth, 0, 0, WIDTH, HEIGHT)
    print('Surface Areas:') #blue, red, white, yellow
    print('Blue: ' + str(surface_areas[0]))
    print('Red: ' + str(surface_areas[1]))
    print('White: ' + str(surface_areas[2]))
    print('Yellow: ' + str(surface_areas[3]))
    print('Total Surface Area: ' + str(surface_areas[0]+surface_areas[1]+surface_areas[2]+surface_areas[3]))

    # wait for user to exit
    turtle.mainloop()

if __name__ == '__main__':
    main()