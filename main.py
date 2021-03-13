"""
    Generative art project. This utilizes PyCairo to create svg and png files of art randomly generated.
    Sources:
        https://www.geeksforgeeks.org/creating-svg-image-using-pycairo/
    __author__ = Ryan Smith
"""

import cairo
import math
import random


def main():
    with cairo.SVGSurface("test.svg", 1000, 1000) as surface:
        # creating a cairo context object
        context = cairo.Context(surface)

        # make background white
        context.set_source_rgba(1, 1, 1, 1)
        context.paint()
        
        # add circle to center
        context.arc(500, 500, 100, 0, 2 * math.pi)
        context.scale(1000, 1000)
        context.set_line_width(0.004)
        context.set_source_rgba(0.4, 1, 0.4, 1)
        context.stroke()


if __name__ == '__main__':
    main()
