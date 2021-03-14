import numpy as np


# A point in space represented by a numpy array
# cite: https://numpy.org/doc/1.18/user/basics.subclassing.html
class Point(np.ndarray):
    def __new__(cls, input_array):
        point = np.asarray(input_array).view(cls)
        return point

    def x(self):
        return self[0]

    def set_x(self, x):
        self[0] = x

    def y(self):
        return self[1]

    def set_y(self, y):
        self[1] = y
