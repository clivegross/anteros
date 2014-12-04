import math
import numpy as np

class Part(object):
  def __init__(self, mass):
    self.mass = mass

  def position_vector_cartesian(self, polar_vector):
    r, theta, phi = polar_vector
    x = r * math.cos(theta) * math.sin(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(phi)
    return [x, y, z]

  def position_vector_polar(self, cartesian_vector):
    x, y, z = cartesian_vector
    r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    theta = math.atan(y/z)
    phi = math.acos(z/r)
    return [r, theta, phi]
