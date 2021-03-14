import math

import cairo
import numpy as np

from Colors import choose_random_color, ibm_color_blind_palatte
from Point import Point


class Line:
    def __init__(self, x1, y1, x2, y2, context):
        self.context = context
        self.point1 = Point([x1, y1])
        self.point2 = Point([x2, y2])

    def get_point1(self):
        return self.point1

    def get_point2(self):
        return self.point2

    # Distance formula: sqrt((x_2 - x_1)^2 + (y_2 - y_1)^2)
    def get_length(self):
        return np.sqrt((self.point2.x() - self.point1.x()) ** 2 + (self.point2.y() - self.point1.y()) ** 2)

    def draw(self):
        self.context.move_to(self.point1.x(), self.point1.y())
        self.context.line_to(self.point2.x(), self.point2.y())
        line_width(.004, self.context)
        random_color(ibm_color_blind_palatte(), self.context)


class Circle:
    def __init__(self, x, y, radius, context):
        self.context = context
        self.point = Point([x, y])
        self.radius = radius
        self.draw()

    def get_point(self):
        return self.point

    def draw(self):
        self.context.arc(self.point.x(), self.point.y(), self.radius, 0, 2 * math.pi)
        line_width(.004, self.context)
        scale(1000, 1000, self.context)
        random_color(ibm_color_blind_palatte(), self.context)


def background(r, g, b, a, context):
    context.set_source_rgba(r, g, b, a)
    context.paint()


def color(r, g, b, a, context):
    context.set_source_rgba(r, g, b, a)


def random_color(colors, context):
    rand_color = choose_random_color(colors)
    context.set_source_rgba(rand_color[0], rand_color[1], rand_color[2], 1)


def stroke(context):
    context.stroke()


def fill(context):
    context.fill()


def line_width(value, context):
    context.set_line_width(value)


def scale(l, w, context):
    context.scale(l, w)
