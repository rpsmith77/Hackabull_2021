""" All the shapes and actions possible. Things that can be added to the canvas, and how they're added. """

import math
import random
import Canvas
from Colors import ibm_color_blind_palette, choose_random_color
from Point import Point


# A line. Has a starting point and end point
class Line:
    """
    Line with two points
    """

    def __init__(self, x1, y1, x2, y2, draw=True):
        self.context = Canvas.Context.context
        self.point1 = Point([x1, y1])
        self.point2 = Point([x2, y2])
        if draw:
            self.draw()

    def get_point1(self):
        """
        get point 1
        :return: point 1
        """
        return self.point1

    def get_point2(self):
        """
        get point 2
        :return: point 2
        """
        return self.point2

    def draw(self):
        """
        Draw the line with a random width and color
        """
        self.context.move_to(self.point1.x(), self.point1.y())
        self.context.line_to(self.point2.x(), self.point2.y())
        line_width(10 * random.random())
        random_color(ibm_color_blind_palette())
        stroke()


# circle with a starting point and radius
class Circle:
    """
    Circle starting from point x, y, and radius
    """

    def __init__(self, x, y, radius):
        self.context = Canvas.Context.context
        self.point = Point([x, y])
        self.radius = radius
        self.draw()

    def get_point(self):
        """
        Get starting pint
        :return: point object
        """
        return self.point

    def draw(self):
        """
        Draw circle with random line width, color, and 50% chance to be filled
        """
        self.context.arc(self.point.x(), self.point.y(), self.radius, 0, 2 * math.pi)
        line_width(10 * random.random())
        random_color(ibm_color_blind_palette())
        if random.randint(1, 2) % 2 == 0:
            fill()
        stroke()


class Triangle:
    """
    Triangle made of 3 line objects
    """

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.context = Canvas.Context.context
        self.lines = [Line(x1, y1, x2, y2, False),
                      Line(x2, y2, x3, y3, False),
                      Line(x3, y3, x1, y1, False)]
        self.draw()

    def draw(self):
        """
        Draw triangle with random width, color, and 50% chance to be filled
        """
        self.context.move_to(self.lines[0].point1.x(), self.lines[0].point1.y())
        for line in self.lines:
            self.context.line_to(line.point2.x(), line.point2.y())
        line_width(10 * random.random())
        random_color(ibm_color_blind_palette())
        if random.randint(1, 2) % 2 == 0:
            fill()
        stroke()


# curved line with a starting point, an endpoint, and point the line goes to between start and end
class CurvedLine(Line):
    """
    Draw a curved line with point 1 and point 2 being end points and point 3 being the point to curve to
    """

    def __init__(self, x1, y1, x2, y2, x3, y3, draw=True):
        self.curve_point = Point([x3, y3])
        super().__init__(x1, y1, x2, y2, False)
        if draw:
            self.draw()

    def draw(self):
        """
        Draw curved line with random width and color
        """
        self.context.move_to(self.point1.x(), self.point1.y())
        self.context.curve_to(self.point1.x(), self.point1.y(), self.point2.x(), self.point2.y(),
                              self.curve_point.x(), self.curve_point.y())
        line_width(10 * random.random())
        random_color(ibm_color_blind_palette())
        stroke()


# create random shape with num_point number of points
class Polygon:
    """
    Create random polygonal shape with at least 4 points
    """

    def __init__(self, num_point, draw=True):
        self.context = Canvas.Context.context
        if num_point < 4:
            num_point = 4
        self.num_point = num_point
        self.points = []
        for i in range(num_point):
            self.points.append(Point([random.randint(-100, 1100), random.randint(-100, 1100)]))
        if draw:
            self.draw()

    def draw(self):
        """
        Draw polygon with random line width, color, and 50% chance of being filled
        """
        self.context.move_to(self.points[0].x(), self.points[0].y())
        for i in range(1, len(self.points)):
            self.context.line_to(self.points[i].x(), self.points[i].y())
        self.context.line_to(self.points[0].x(), self.points[0].y())
        line_width(10 * random.random())
        random_color(ibm_color_blind_palette())
        if random.randint(1, 4) == 1:
            fill()
        stroke()


def background(r, g, b, a):
    """
    set canvas background color
    :param r: red %
    :param g: green %
    :param b: blue %
    :param a: alpha(transparency) %
    """
    Canvas.Context.context.set_source_rgba(r, g, b, a)
    Canvas.Context.context.paint()


def background_random_color():
    """
    get random choice non-black or white, color-blind-friendly colored background
    """
    rand_color = choose_random_color(ibm_color_blind_palette())
    background(rand_color[0], rand_color[1], rand_color[2], 1)


def color(r, g, b, a):
    """
    set stroke color
    :param r:
    :param g:
    :param b:
    :param a:
    """
    Canvas.Context.context.set_source_rgba(r, g, b, a)


def random_color(colors):
    """
    choose a random color from list of valid colors. 50% chance the color will be a random % of opaque
    :param colors: colors to choose from
    """
    rand_color = choose_random_color(colors)
    if random.randint(1, 2) % 2 == 0:
        Canvas.Context.context.set_source_rgba(rand_color[0], rand_color[1], rand_color[2], random.random())  # opaque
    else:
        Canvas.Context.context.set_source_rgba(rand_color[0], rand_color[1], rand_color[2], 1)  # solid


def stroke():
    """
    stroke. it essentially paints it on the image
    """
    Canvas.Context.context.stroke()


def fill():
    """
    fill's shape
    """
    Canvas.Context.context.fill()


def line_width(value):
    """
    set thickness of stroke
    :param value: line width
    """
    Canvas.Context.context.set_line_width(value)


def scale(length, width):
    """
    Set the scale
    :param length: Length
    :param width: Width
    """
    Canvas.Context.context.scale(length, width)


def get_random_int():
    """
    get a random integer between 0 and the width dimension hardcoded 1000
    :return: random integer between 0 and 1000
    """
    return random.randint(0, 1000)


# ********************** Randomize Shapes **********************


def create_curved_line():
    """
    completely random points
    """
    r = random.randint(1, 4)

    if r == 1:  # curved line left to right
        CurvedLine(get_random_int(), 0, get_random_int(), 1000, get_random_int(), get_random_int())

    elif r == 2:  # curved line top to bottom
        CurvedLine(0, get_random_int(), get_random_int(), get_random_int(), get_random_int(), 1000)

    else:  # random curved line segment
        CurvedLine(get_random_int(), get_random_int(), get_random_int(), get_random_int(), get_random_int(),
                   get_random_int())


def create_circle():
    """
    random starting point, 0 < radius <= 400
    """
    Circle(get_random_int(), get_random_int(), 300 * random.random())


def create_triangle():
    """
    random triangle
    """
    Triangle(get_random_int() * 2 * random.random(), get_random_int() * 2 * random.random(),
             get_random_int() * 2 * random.random(), get_random_int() * 2 * random.random(),
             get_random_int() * 2 * random.random(), get_random_int() * 2 * random.random())


def create_polygon():
    """
    random polygon with between 4 and 8 points
    """
    Polygon(random.randint(4, 8))


def line_top_to_bottom():
    """
    line between 2 points (random, 0) , (random, 1000)
    """
    Line(get_random_int(), 0, get_random_int(), 1000)


def line_left_to_right():
    """
    line between 2 points (0, random) , (1000, random)
    """
    Line(0, get_random_int(), 1000, get_random_int())


def line_segment():
    """
    line between completely random points
    """
    Line(get_random_int(), get_random_int(), get_random_int(), get_random_int())


def create_random_line():
    """
    33.3% chance of a top to bottom line, left to right line, and a line segment
    """
    r = random.randint(1, 4)
    if r == 1:
        line_segment()
    elif r == 2:
        line_left_to_right()
    else:
        line_top_to_bottom()


def random_shape():
    """
    create a random shape. Chooses between curved lines, circles, triangles, other polygons, and straight lines
    """
    r = random.randint(1, 12)
    if r == 1:
        create_polygon()
    elif r <= 3:
        create_circle()
    elif r <= 5:
        create_triangle()
    elif r <= 7:
        create_curved_line()
    else:
        create_random_line()


def random_background():
    """
    random background color
    """
    r = random.randint(1, 4)
    if r == 1:  # transparent
        background(0, 0, 0, 0)
    elif r == 2:  # white
        background(1, 1, 1, 1)
    elif r == 3:  # black
        background(0, 0, 0, 1)
    else:  # random color
        background_random_color()
