import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos

class Turtle(object):
    def __init__(self):
        self._direction   = 0               # Angle in Radians
        self._current_pos = np.array([0,0]) # Start at Origin
        self._log = [[self._current_pos]]
        self._pendown = True

    def _deg2rad(self, angle):
        return angle*pi/180.

    def _get_vector_from_angle(self):
        angle = self._direction
        return np.array([sin(angle), cos(angle)])

    def forward(self, dist):
        self._current_pos = self._current_pos + dist*self._get_vector_from_angle()
        if self._pendown:
            self._log[-1].append(self._current_pos)

    def backward(self, dist):
        self._current_pos = self._current_pos + dist*self._get_vector_from_angle()
        if self._pendown:
            self._log[-1].append(self._current_pos)

    def right(self, angle):
        self._direction += self._deg2rad(angle)

    def left(self, angle):
        self._direction -= self._deg2rad(angle)

    def penup(self):
        self._pendown = False
        self._log.append([])

    def pendown(self):
        self._pendown = True
        self._log[-1].append(self._current_pos)

    def plot(self):
        for route in self._log:
            route = np.array(route)
            plt.plot(route[:,0], route[:,1])
        plt.show()

if __name__ in "__main__":
    x = Turtle()
    x.forward(10)
    x.right(90)
    x.forward(10)
    x.right(45)
    x.forward(10)
    x.penup()
    x.right(45)
    x.forward(10)
    x.left(90)
    x.pendown()
    x.forward(10)
    x.plot()
