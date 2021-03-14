""" This github repo – https://github.com/JakobGlock/Generative-Art – showed me how to make unique file names,
and how to use cairo.Context, across multiple files and classes, in a way that works """

from datetime import datetime
from uuid import uuid4
import cairo
import Canvas


# Stores cairo.Context within Canvas.py
def setup(width, height):
    draw_context = DrawContext(width, height)
    Canvas.Context = draw_context


def export():
    Canvas.Context.export()


# Generate unique file name (Year-Day-Month_Hour-Minute-Second-UniqueID)
def generate_filename():
    now = datetime.now()
    timestamp = now.strftime("%Y-%d-%m_%H-%M-%S")
    unique_id = uuid4().hex[:8]
    return str(timestamp + "-" + unique_id)


# create cairo.Context with SVG file and unique file name
class DrawContext:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.file_name = generate_filename()
        self.surface = cairo.SVGSurface(self.file_name + ".svg", self.width, self.height)
        self.cairo_context = self.setup_surface()

    def setup_surface(self):
        return cairo.Context(self.surface)

    def finish_surface(self):
        self.surface.finish()

    def export(self):
        self.finish_surface()

    @property
    def context(self):
        return self.cairo_context
