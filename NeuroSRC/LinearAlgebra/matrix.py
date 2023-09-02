import random
from . import vector


class Matrix:

  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols

    self.data = [[0] * cols for _ in range(rows)]

  def __repr__(self):  # intriguing # lol
    matrix_str = ""
    for row in self.data:
      matrix_str += ' '.join(map(str, row)) + '\n'
    return "\nMATRIX (\n" + matrix_str + ")\n"

  def __repr__(self):  # intriguing # lol
    matrix_str = ""
    for row in self.data:
      matrix_str += ' '.join(map(str, row)) + '\n'
    return "\nMATRIX (\n" + matrix_str + ")\n"

  def __getitem__(self, index):
    return self.data[index]

  def __setitem__(self, index, value):
    self.data[index] = value

  def shape(self):
    return (self.rows, self.cols)

  def transpose(self):
    transposed_data = [[self.data[j][i] for j in range(self.rows)]
                       for i in range(self.cols)]
    self.data = transposed_data
    self.rows, self.cols = self.cols, self.rows
    return self

  def add(self, other):
    if self.shape() != other.shape():

      raise ValueError("Matrix shapes are not compatible for addition")

    result = Matrix(self.rows, self.cols)
    for i in range(self.rows):
      for j in range(self.cols):
        result[i][j] = self[i][j] + other[i][j]

    return result

  def multiply_brodcast(self, other):
    if 1 in [self.cols, self.rows, other.cols, other.rows]:
      defs = self
      defo = other

      if self.rows == 1:
        self = self.stretch(axis="x", amt=other.rows)
      if self.cols == 1:
        self = self.stretch(axis="y", amt=other.cols)
      if other.rows == 1:
        other = other.stretch(axis="x", amt=other.rows)
      if other.cols == 1:
        other = other.stretch(axis="y", amt=other.cols)
      res = self.multiply_elementwise(other)
      self = defs
      other = defo
      return res
    else:
      raise ValueError("Failed to brodcast.")

  def multiply_sumdot(self, other):
    pack = []
    f = 0
    for r in self.data:
      print("70", r)
      print(other)
      m = Matrix(len(r), 1)
      m.data = [r]
      ans = m.multiply_elementwise(other)
      pack.append(ans[0])
      f = r
    mres = Matrix(len(f), len(self.data))
    return mres

  def multiply(self, other):
    if other.cols == 1 and other.rows == 1:
      sc = other.data[0][0]
      return self.multiply_scalar(sc)
    if self.cols != other.rows:
      print("WTFTFT", self.cols, other.rows, self, other)
      raise ValueError("Matrix shapes are not compatible for multiplication")

    result = Matrix(self.rows, other.cols)

    for i in range(self.rows):
      for j in range(other.cols):
        dot_product = sum(self[i][k] * other[k][j] for k in range(self.cols))
        result[i][j] = dot_product

    return result

  def multiply_addingon(self, other):
    try:
      return other.multiply(self)
    except ValueError:
      return self.dot(other)

  def multiply_vector(self, vector):
    if self.cols != len(vector):
      raise ValueError(
          "Matrix and vector sizes are not compatible for multiplication")

    result = vector.Vector(self.rows)
    for i in range(self.rows):
      dot_product = sum(self[i][j] * vector[j] for j in range(self.cols))
      result[i] = dot_product

    return result

  def multiply_scalar(self, scalar):
    result = Matrix(self.rows, self.cols)
    for i in range(self.rows):
      for j in range(self.cols):
        result[i][j] = self[i][j] * scalar
    return result

  def add(self, other):
    if self.shape() != other.shape():
      raise ValueError("Matrix shapes are not compatible for addition")

    result = Matrix(self.rows, self.cols)
    for i in range(self.rows):
      for j in range(self.cols):
        result[i][j] = self[i][j] + other[i][j]
    return result

  def subtract(self, other):
    if self.shape() != other.shape():
      raise ValueError("Matrix shapes are not compatible for subtraction")

    result = Matrix(self.rows, self.cols)
    for i in range(self.rows):
      for j in range(self.cols):
        result[i][j] = self[i][j] - other[i][j]
    return result

  def randomize(self, min_value=0, max_value=1):
    for i in range(self.rows):
      for j in range(self.cols):
        self[i][j] = random.uniform(min_value, max_value)

  def square(self):

    np1 = []
    for i in self.data:
      np2 = []
      for j in i:
        np2.append(j**2)
      np1.append(np2)
    m = Matrix(self.rows, self.cols)
    m.data = np1

    return m

  def stretch(self, axis, amt):
    if axis == "x":
      pack = []
      for item in self.data:
        pack.append(item * amt)
      m = Matrix(amt, self.cols)
      m.data = pack
      return m
    elif axis == "y":
      vec_sample = self.data[0]
      pack = []
      for i in range(amt):
        pack.append(vec_sample)
      m = Matrix(self.rows, amt)
      m.data = pack
      return m
    else:
      return self

  def sumup(self):
    s = 0
    for i in self.data:
      for j in i:
        s += j
    return s

  def multiply_numpydot(self, other):
    # I CANNOT DO THIS ANYMORE!
    # I NEED NUMPY!!!
    # IF ANYONE CAN IMPLEMENT THIS WITHOUT NUMPY, GOOD LUCK!
    import numpy as np
    a = np.array(self.data)
    b = np.array(other.data)
    c = np.dot(a, b)
    m = Matrix(c.shape[0], c.shape[1])
    m.data = list(c)
    return m

  def multiply_elementwise(self, other):
    if self.shape() != other.shape():
      raise ValueError(
          "Matrix shapes are not compatible for element-wise multiplication")

    result = Matrix(self.rows, self.cols)
    for i in range(self.rows):
      for j in range(self.cols):
        result[i][j] = self[i][j] * other[i][j]
    return result

  def dot(self, other):
    # Check if the number of columns in the first matrix is equal to the number of rows in the second matrix
    if self.cols != other.rows:
      raise ValueError("Matrix shapes are not compatible for dot product.")

    result = Matrix(self.rows, other.cols)

    for i in range(self.rows):
      for j in range(other.cols):
        dot_product = sum(self[i][k] * other[k][j]
                          for k in range(self.cols))
        result[i][j] = dot_product

    return result

  def multiply_GPT(self, other):
    if isinstance(other, Matrix):
      if self.cols != other.rows:
        raise ValueError("Matrix shapes are not compatible for multiplication")

      result = Matrix(self.rows, other.cols)

      for i in range(self.rows):
        for j in range(other.cols):
          dot_product = sum(self[i][k] * other[k][j] for k in range(self.cols))
          result[i][j] = dot_product

      return result
    elif isinstance(other, (int, float)):  # Scalar multiplication
      result = Matrix(self.rows, self.cols)
      for i in range(self.rows):
        for j in range(self.cols):
          result[i][j] = self[i][j] * other
      return result
    else:
      raise ValueError("Unsupported data type for multiplication")


# Example usage

# matrix1 = Matrix(2, 3)
# matrix1[0] = [1, 2, 3]
# matrix1[1] = [4, 5, 6]

# matrix2 = Matrix(3, 2)
# matrix2[0] = [7, 8]
# matrix2[1] = [9, 10]
# matrix2[2] = [11, 12]

# print("Matrix 1:")
# print(matrix1)

# print("Matrix 2:")
# print(matrix2)

# result = matrix1.multiply(matrix2)
# print("Matrix 1 * Matrix 2:")
# print(result)
