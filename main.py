"""
    Generative art project. This utilizes PyCairo to create svg and png files of art randomly generated. This is
    basic version
    Sources:
        https://www.geeksforgeeks.org/creating-svg-image-using-pycairo/
    __author__ = Ryan Smith
"""

import random
from Context import setup, export
from Shapes import background, random_shape


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
