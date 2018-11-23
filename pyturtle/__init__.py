import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos
from mpl_toolkits.mplot3d import Axes3D

class Turtle(object):
    def __init__(self):
        self._direction   = np.array([0, pi/2.])  # Theta-Phi Angles in Radians
        self._current_pos = np.array([0,0,0]) # Start at Origin
        self._log = [[self._current_pos]]
        self._pendown = True

    def _deg2rad(self, angle):
        return angle*pi/180.

    def _get_vector_from_angle(self):
        theta, phi = self._direction
        print(np.array([sin(phi)*cos(theta), sin(phi)*sin(theta), cos(phi)]))
        return np.array([sin(phi)*cos(theta), sin(phi)*sin(theta), cos(phi)])

    def forward(self, dist):
        self._current_pos = self._current_pos + dist*self._get_vector_from_angle()
        if self._pendown:
            self._log[-1].append(self._current_pos)

    def backward(self, dist):
        self._current_pos = self._current_pos + dist*self._get_vector_from_angle()
        if self._pendown:
            self._log[-1].append(self._current_pos)

    def right(self, angle):
        self._direction[0] += self._deg2rad(angle)

    def left(self, angle):
        self._direction[0] -= self._deg2rad(angle)

    def elevate(self, angle):
        self._direction[1] += self._deg2rad(angle)

    def declinate(self, angle):
        self._direction[1] -= self._deg2rad(angle)

    def penup(self):
        self._pendown = False
        self._log.append([])

    def pendown(self):
        self._pendown = True
        self._log[-1].append(self._current_pos)

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for route in self._log:
            print(route)
            route = np.array(route)
            ax.plot(route[:,0], route[:,1], route[:,2])
        plt.show()

if __name__ in "__main__":
    x = Turtle()
    x.elevate(10)
    for i in range(100):
        x.forward(5)
        x.right(5)
    x.plot()
