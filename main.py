"""
    Generative art project. This utilizes PyCairo to create svg and png files of art randomly generated. This
    project also uses Vector math to figure out what the shapes and lines will look like.
    Sources:
        https://www.geeksforgeeks.org/creating-svg-image-using-pycairo/
    __author__ = Ryan Smith
"""

import cairo
import math
import random
import numpy as np
import Canvas
from Colors import ibm_color_blind_pallate, choose_random_color


def random_color(colors, context):
    rand_color = choose_random_color(colors)
    context.set_source_rgba(rand_color[0], rand_color[1], rand_color[2], 1)


def main():
    with cairo.SVGSurface("test.svg", 1000, 1000) as surface:
        # creating a cairo context object
        context = cairo.Context(surface)

        # make background white
        context.set_source_rgba(1, 1, 1, 1)
        context.paint()

        Canvas.Circle(500, 400, 200, context)
        random_color(ibm_color_blind_pallate(), context)
        Canvas.stroke(context)

        lines = []
        for i in range(random.randint(1, 10)):
            lines.append(Canvas.Line(random.random(), random.random(), random.random(), random.random(), context))

        for line in lines:
            context.save()
            context.set_line_width(0.004)
            random_color(ibm_color_blind_pallate(), context)
            line.draw()
            Canvas.stroke(context)
            context.restore()
        context.stroke()


if __name__ == '__main__':
    main()
