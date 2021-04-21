"""
    Generative art project. This utilizes PyCairo to create svg and png files of art randomly generated. This is
    basic version
    Sources:
        https://www.geeksforgeeks.org/creating-svg-image-using-pycairo/
"""
__author__ = "Ryan Smith"

import random
from Context import setup, export
from Shapes import random_shape, random_background


# Perform Shapes.py's actions
def draw():
    """
    get random background ( 1/3 white, 1/3 black, 1/3 color-blind-friendly color)
    """

    random_background()

    # create 20 to 50 random shapes
    for i in range(random.randint(10, 30)):
        random_shape()


def main():
    """
    main
    """
    setup(1000, 1000)
    draw()
    export()


if __name__ == '__main__':
    main()
