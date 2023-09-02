import random
class Vector:
    def __init__(self, size):
        if isinstance(size, list):
          self.size = len(size)
          self.data = size
        else:
          self.size = size
          self.data = [0] * size
    
    def __str__(self):
        return '[' + ', '.join(map(str, self.data)) + ']'
    def __repr__(self):
        return 'Vector ('+'[' + ', '.join(map(str, self.data)) + ']' + ')'
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
    
    def __len__(self):
        return self.size
    
    def dot(self, other):
        if len(self) != len(other):
            raise ValueError("Vector sizes are not compatible for dot product")
        
        return sum(self[i] * other[i] for i in range(self.size))
    def cross(self, other):
        if len(self) != 3 or len(other) != 3:
            raise ValueError("Cross product is only defined for 3-dimensional vectors")

        result = Vector(3)
        result[0] = self[1] * other[2] - self[2] * other[1]
        result[1] = self[2] * other[0] - self[0] * other[2]
        result[2] = self[0] * other[1] - self[1] * other[0]
        
        return result
    def randomize(self, min_value=0, max_value=1):
        for i in range(self.size):
            self[i] = random.uniform(min_value, max_value)

      
    @staticmethod
    def random_vector(size):
        data = [random.random() for _ in range(size)]
        return Vector(data)

    def add(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must have the same length for addition")
        result_data = [self.data[i] + other.data[i] for i in range(len(self.data))]
        return Vector(result_data)

    def subtract(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must have the same length for subtraction")
        result_data = [self.data[i] - other.data[i] for i in range(len(self.data))]
        return Vector(result_data)

    def multiply_scalar(self, scalar):
        result_data = [self.data[i] * scalar for i in range(len(self.data))]
        return Vector(result_data)

    def multiply_elementwise(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must have the same length for element-wise multiplication")
        result_data = [self.data[i] * other.data[i] for i in range(len(self.data))]
        return Vector(result_data)

    def outer_product(self, other):
        outer_data = [[self.data[i] * other.data[j] for j in range(len(other.data))] for i in range(len(self.data))]
        return Matrix(outer_data)

    def magnitude(self):
        return sum(x ** 2 for x in self.data) ** 0.5

              



# # Example usage
# vector1 = Vector(3)
# vector1[0] = 1
# vector1[1] = 2
# vector1[2] = 3

# vector2 = Vector(3)
# vector2[0] = 4
# vector2[1] = 5
# vector2[2] = 6

# print("Vector 1:", vector1)
# print("Vector 2:", vector2)

# dot_product = vector1.dot(vector2)
# print("Dot Product:", dot_product)
