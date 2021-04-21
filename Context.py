""" This github repo – https://github.com/JakobGlock/Generative-Art – showed me how to make unique file names,
and how to use cairo.Context, across multiple files and classes, in a way that works """

from datetime import datetime
from uuid import uuid4
import cairo
import Canvas


def setup(width, height):
    """
    Stores cairo.Context within Canvas.py
    :param width: canvas width
    :param height: canvas height
    """
    draw_context = DrawContext(width, height)
    Canvas.Context = draw_context


def export():
    """
    Export the SVG file
    """
    Canvas.Context.export()


def generate_filename():
    """
    Generate unique file name (Year-Day-Month_Hour-Minute-Second-UniqueID)
    :return: file name
    """
    now = datetime.now()
    timestamp = now.strftime("%Y-%d-%m_%H-%M-%S")
    unique_id = uuid4().hex[:8]
    return str(timestamp + "-" + unique_id)


class DrawContext:
    """
    create cairo.Context with SVG file and unique file name
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.file_name = generate_filename()
        self.surface = cairo.SVGSurface(self.file_name + ".svg", self.width, self.height)
        self.cairo_context = self.setup_surface()

    def setup_surface(self):
        """
        setup surface to draw on
        :return:
        """
        return cairo.Context(self.surface)

    def finish_surface(self):
        """
        finish the surface
        """
        self.surface.finish()

    def export(self):
        """
        export
        """
        self.finish_surface()

    @property
    def context(self):
        """
        https://cairographics.org/documentation/pycairo/2/reference/context.html
        :return: the cairo's context to do things within
        """
        return self.cairo_context
