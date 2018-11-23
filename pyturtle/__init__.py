import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos
from mpl_toolkits.mplot3d import Axes3D

import logging
logging.basicConfig()

class Turtle(object):
    def __init__(self, debug=False):
        self._direction   = np.array([0, pi/2.])  # Theta-Phi Angles in Radians
        self._current_pos = np.array([0,0,0]) # Start at Origin
        self._pendown = False
        self._logger = logging.getLogger('Turtle')
        self._logger.setLevel('INFO' if not debug else 'DEBUG')
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
        return np.array([sin(phi)*sin(theta), sin(phi)*cos(theta), -cos(phi)])

    def forward(self, dist):
        self._logger.debug(f'Forward {dist}')
        self._current_pos = self._current_pos + dist*self._get_vector_from_angle()
        self._log_point(self._current_pos)

    def backward(self, dist):
        self._logger.debug(f'Backward {dist}')
        self._current_pos = self._current_pos - dist*self._get_vector_from_angle()
        self._log_point(self._current_pos)

    def right(self, angle):
        self._logger.debug(f'Right {angle}')
        self._direction[0] += self._deg2rad(angle)

    def left(self, angle):
        self._logger.debug(f'Left {angle}')
        self._direction[0] -= self._deg2rad(angle)

    def elevate(self, angle):
        self._logger.debug(f'Raise {angle}')
        self._direction[1] += self._deg2rad(angle)

    def declinate(self, angle):
        self._logger.debug(f'Lower {angle}')
        self._direction[1] -= self._deg2rad(angle)

    def penup(self):
        self._logger.debug('PenUp')
        self._pendown = False
        self._log.append([])

    def pendown(self):
        self._logger.debug('PenDown')
        self._pendown = True
        self._log_point(self._current_pos)

    def _check_if_2d(self):
        for route in self._log:
            for point in route:
                if point[2] > 1E-3:
                    return True
        return False

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for route in self._log:
            _route = np.array(route)
            try:
                    ax.plot(_route[:,0], _route[:,1], _route[:,2])
            except IndexError as e:
                self._logger.error("Failed to Plot Path, did you lower the pen?")
                raise e
        plt.show()

