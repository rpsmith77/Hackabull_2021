""" Point object using numpy vectors to define the coordinates """

import numpy as np


class Point(np.ndarray):
    """
    A point in space represented by a numpy array
    cite: https://numpy.org/doc/1.18/user/basics.subclassing.html
    """
    def __new__(cls, input_array):
        point = np.asarray(input_array).view(cls)
        return point

    def x(self):
        """
        x coordinate
        :return: x coordinate
        """
        return self[0]

    def set_x(self, x):
        """
        set x coordinate
        :param x: value to set x
        """
        self[0] = x

    def y(self):
        """
        y coordinate
        :return: y coordinate
        """
        return self[1]

    def set_y(self, y):
        """
        set y coordinate
        :param y: value to set y
        """
        self[1] = y
