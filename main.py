"""
    Generative art project. This utilizes PyCairo to create svg and png files of art randomly generated. This is
    basic version
    Sources:
        https://www.geeksforgeeks.org/creating-svg-image-using-pycairo/
    __author__ = Ryan Smith
"""

import random
from Shapes import Line, Circle, Curved_Line, background, create_curved_line, create_circle, create_random_line
from Context import setup, export


# create a random shape 25% chance to be a curved line, 25% chance to be a circle, 50%  chance to be a random type of
# straight line
def random_shape():
    r = random.randint(1, 4)
    if r == 1:
        create_curved_line()
    elif r == 2:
        create_circle()
    else:
        create_random_line()


# Perform Shapes.py's actions
def draw():
    # color background white
    background(1, 1, 1, 1)

    # create 20 to 50 random shapes
    for i in range(random.randint(20, 50)):
        random_shape()


def main():
    setup(1000, 1000)
    draw()
    export()


if __name__ == '__main__':
    main()
