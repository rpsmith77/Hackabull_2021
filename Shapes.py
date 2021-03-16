# All the shapes and actions possible. Things that can be added to the canvas, and how they're added.


import math
import random
import Canvas
from Colors import ibm_color_blind_palette, choose_random_color
from Point import Point


# A line. Has a starting point and end point
class Line:
    def __init__(self, x1, y1, x2, y2, draw=True):
        self.context = Canvas.Context.context
        self.point1 = Point([x1, y1])
        self.point2 = Point([x2, y2])
        if draw:
            self.draw()

    def get_point1(self):
        return self.point1

    def get_point2(self):
        return self.point2

    def draw(self):
        self.context.move_to(self.point1.x(), self.point1.y())
        self.context.line_to(self.point2.x(), self.point2.y())
        line_width(10 * random.random())
        random_color(ibm_color_blind_palette())
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
        random_color(ibm_color_blind_palette())
        if random.randint(1, 2) % 2 == 0:
            fill()
        stroke()


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.context = Canvas.Context.context
        self.lines = [Line(x1, y1, x2, y2, False),
                      Line(x2, y2, x3, y3, False),
                      Line(x3, y3, x1, y1, False)]
        self.draw()

    def draw(self):
        self.context.move_to(self.lines[0].point1.x(), self.lines[0].point1.y())
        for line in self.lines:
            self.context.line_to(line.point2.x(), line.point2.y())
        line_width(10 * random.random())
        random_color(ibm_color_blind_palette())
        if random.randint(1, 2) % 2 == 0:
            fill()
        stroke()


# curved line with a starting point, an endpoint, and point the line goes to between start and end
class Curved_Line(Line):
    def __init__(self, x1, y1, x2, y2, x3, y3, draw=True):
        self.curve_point = Point([x3, y3])
        super().__init__(x1, y1, x2, y2, False)
        if draw:
            self.draw()

    def draw(self):
        self.context.move_to(self.point1.x(), self.point1.y())
        self.context.curve_to(self.point1.x(), self.point1.y(), self.point2.x(), self.point2.y(),
                              self.curve_point.x(), self.curve_point.y())
        line_width(10 * random.random())
        random_color(ibm_color_blind_palette())
        stroke()


# create random shape with num_point number of points
class Polygon:
    def __init__(self, num_point, draw=True):
        self.context = Canvas.Context.context
        if num_point < 4:
            num_point = 4
        self.num_point = num_point
        self.points = []
        for i in range(num_point):
            self.points.append(Point([get_random_int(), get_random_int()]))
        if draw:
            self.draw()

    def draw(self):
        self.context.move_to(self.points[0].x(), self.points[0].y())
        for i in range(1, len(self.points)):
            self.context.line_to(self.points[i].x(), self.points[i].y())
        self.context.line_to(self.points[0].x(), self.points[0].y())
        line_width(10 * random.random())
        random_color(ibm_color_blind_palette())
        if random.randint(1, 2) % 2 == 0:
            fill()
        stroke()


# set background color
def background(r, g, b, a):
    Canvas.Context.context.set_source_rgba(r, g, b, a)
    Canvas.Context.context.paint()


# get random choice non-black or white, color-blind-friendly colored background
def background_random_color():
    rand_color = choose_random_color(ibm_color_blind_palette())
    background(rand_color[0], rand_color[1], rand_color[2], 1)


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
    r = random.randint(1, 4)

    if r == 1:  # curved line left to right
        Curved_Line(get_random_int(), 0, get_random_int(), 1000, get_random_int(), get_random_int())

    elif r == 2:  # curved line top to bottom
        Curved_Line(0, get_random_int(), get_random_int(), get_random_int(), get_random_int(), 1000)

    else:  # random curved line segment
        Curved_Line(get_random_int(), get_random_int(), get_random_int(), get_random_int(), get_random_int(),
                    get_random_int())


# random starting point, 0 < radius <= 400
def create_circle():
    Circle(get_random_int(), get_random_int(), 300 * random.random())


# random triangle
def create_triangle():
    Triangle(get_random_int() * 2 * random.random(), get_random_int() * 2 * random.random(),
             get_random_int() * 2 * random.random(), get_random_int() * 2 * random.random(),
             get_random_int() * 2 * random.random(), get_random_int() * 2 * random.random())


def create_polygon():
    Polygon(random.randint(4, 12))


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
    r = random.randint(1, 4)
    if r == 1:
        line_segment()
    elif r == 2:
        line_left_to_right()
    else:
        line_top_to_bottom()


# create a random shape. Chooses between curved lines, circles, triangles, other polygons, and straight lines
def random_shape():
    r = random.randint(1, 6)
    if r == 1:
        create_curved_line()
    elif r == 2:
        create_circle()
    elif r == 3:
        create_triangle()
    elif r == 4:
        create_polygon()
    else:
        create_random_line()


# random background color
def random_background():
    r = random.randint(1, 4)
    if r == 1:  # transparent
        background(0, 0, 0, 0)
    elif r == 2:  # white
        background(1, 1, 1, 1)
    elif r == 3:  # black
        background(0, 0, 0, 1)
    else:  # random color
        background_random_color()
