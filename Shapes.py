# All the shapes and actions possible. Things that can be added to the canvas, and how they're added.


import math
import random
import Canvas
from Colors import ibm_color_blind_palate, choose_random_color
from Point import Point


# A line. Has a starting point and end point
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.context = Canvas.Context.context
        self.point1 = Point([x1, y1])
        self.point2 = Point([x2, y2])
        self.draw()

    def get_point1(self):
        return self.point1

    def get_point2(self):
        return self.point2

    def draw(self):
        self.context.move_to(self.point1.x(), self.point1.y())
        self.context.line_to(self.point2.x(), self.point2.y())
        line_width(10 * random.random())
        random_color(ibm_color_blind_palate())
        stroke()


# circle with a starting point and radius
class Circle:
    def __init__(self, x, y, radius):
        self.context = Canvas.Context.context
        self.point = Point([x, y])
        self.radius = radius
        self.draw()

    def get_point(self):
        return self.point

    def draw(self):
        self.context.arc(self.point.x(), self.point.y(), self.radius, 0, 2 * math.pi)
        line_width(10 * random.random())
        random_color(ibm_color_blind_palate())
        if random.randint(1, 2) % 2 == 0:
            fill()
        stroke()


# curved line with a starting point, an endpoint, and point the line goes to between start and end
class Curved_Line(Line):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.curve_point = Point([x3, y3])
        super().__init__(x1, y1, x2, y2)

    def draw(self):
        self.context.move_to(self.point1.x(), self.point1.y())
        self.context.curve_to(self.point1.x(), self.point1.y(), self.point2.x(), self.point2.y(),
                              self.curve_point.x(), self.curve_point.y())
        line_width(10 * random.random())
        random_color(ibm_color_blind_palate())
        stroke()


# set background color
def background(r, g, b, a):
    Canvas.Context.context.set_source_rgba(r, g, b, a)
    Canvas.Context.context.paint()


# set stroke color
def color(r, g, b, a):
    Canvas.Context.context.set_source_rgba(r, g, b, a)


# choose a random color from list of valid colors. 50% chance the color will be a random % of opaque
def random_color(colors):
    rand_color = choose_random_color(colors)
    if random.randint(1, 2) % 2 == 0:
        Canvas.Context.context.set_source_rgba(rand_color[0], rand_color[1], rand_color[2], random.random())  # opaque
    else:
        Canvas.Context.context.set_source_rgba(rand_color[0], rand_color[1], rand_color[2], 1)  # solid


# stroke. it essential paints it on the image
def stroke():
    Canvas.Context.context.stroke()


# fill's shape
def fill():
    Canvas.Context.context.fill()


# set thickness of stroke
def line_width(value):
    Canvas.Context.context.set_line_width(value)


# Set the scale
def scale(length, width):
    Canvas.Context.context.scale(length, width)


# get a random integer between 0 and the width dimension hardcoded 1000
def get_random_int():
    return random.randint(0, 1000)


# ********************** Randomize Shapes **********************

# completely random points
def create_curved_line():
    Curved_Line(get_random_int(), get_random_int(), get_random_int(), get_random_int(), get_random_int(),
                get_random_int())


# random starting point, 0 < radius <= 400
def create_circle():
    Circle(get_random_int(), get_random_int(), 400 * random.random())


# line between 2 points (random, 0) , (random, 1000)
def line_top_to_bottom():
    Line(get_random_int(), 0, get_random_int(), 1000)


# line between 2 points (0, random) , (1000, random)
def line_left_to_right():
    Line(0, get_random_int(), 1000, get_random_int())


# line between completely random points
def line_segment():
    Line(get_random_int(), get_random_int(), get_random_int(), get_random_int())


# 33.3% chance of a top to bottom line, left to right line, and a line segment
def create_random_line():
    r = random.randint(1, 3)
    if r == 1:
        line_segment()
    elif r == 2:
        line_left_to_right()
    else:
        line_top_to_bottom()
