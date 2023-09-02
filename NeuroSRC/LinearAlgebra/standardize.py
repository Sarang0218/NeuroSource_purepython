import math
from .matrix import Matrix
from .vector import Vector

class Standardize:

  # This turns a list of vectors so they range 0 to 1.
  # Each "row"'s maximum becomes 1.0
  @staticmethod
  def standardize(lvc):
    maxvector = [0] * lvc[0].size
    i = 0
    for k in maxvector:
      a = -999
      for vec in lvc:
        if vec[i] > a:
          a = vec[i]
      for vec in lvc:
        vec[i] = vec[i]/a
      i += 1
    return lvc

  # This turns a list of Vectors into a Matrix
  @staticmethod
  def to_mat(vector_list):
    x_ax = vector_list[0].size
    y_ax = len(vector_list)
    
    m = Matrix(y_ax, x_ax)
    
    for i in range(y_ax): 
      m.data[i] = vector_list[i].data
    return m
    
    
