import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos
from mpl_toolkits.mplot3d import Axes3D

class Turtle(object):
    def __init__(self):
        self._direction   = np.array([0, pi/2.])  # Theta-Phi Angles in Radians
        self._current_pos = np.array([0,0,0]) # Start at Origin
        self._pendown = False
        self._log = [[]]

    def _deg2rad(self, angle):
        return angle*pi/180.

    def _log_point(self, vector):
            vector = list(vector)
            if self._pendown:
                for i,j  in enumerate(vector):
                    if abs(vector[i]) < 1E-2:
                        vector[i] = int(vector[i])
                self._log[-1].append(vector)

    def _get_vector_from_angle(self):
        theta, phi = self._direction
        return np.array([sin(phi)*cos(theta), sin(phi)*sin(theta), cos(phi)])

    def forward(self, dist):
        self._current_pos = self._current_pos - dist*self._get_vector_from_angle()
        self._log_point(self._current_pos)

    def backward(self, dist):
        self._current_pos = self._current_pos + dist*self._get_vector_from_angle()
        self._log_point(self._current_pos)

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
        self._log_point(self._current_pos)

    def _check_if_2d(self):
        for route in self._log:
            for point in route:
                if point[2] > 1E-3:
                    return True
        return False

    def plot(self):
        if self._check_if_2d():
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
        plt.clf()
        for route in self._log:
            route = np.array(route)
            if self._check_if_2d():
                ax.plot(route[:,0], route[:,1], route[:,2])
            else:
                plt.plot(route[:,0], route[:,1], route[:,2])
        plt.show()

