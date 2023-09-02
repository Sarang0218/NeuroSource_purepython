import math
from .matrix import Matrix
from .vector import Vector


class ActivationFunctions:
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
    
    @staticmethod
    def relu(x):
        return max(0, x)
      
    @staticmethod
    def sigmoid_derivative(x):
        return math.exp(-x)/((1+math.exp(-x))**2)

class ActivationUtils:
    @staticmethod
    def apply_sigmoid(input):
        if isinstance(input, Matrix):
            result = Matrix(input.rows, input.cols)
            for i in range(input.rows):
                for j in range(input.cols):
                    result[i][j] = ActivationFunctions.sigmoid(input[i][j])
            return result
        
        if isinstance(input, Vector):
            result = Vector(len(input))
            for i in range(len(input)):
                result[i] = ActivationFunctions.sigmoid(input[i])
            return result
        
        raise ValueError("Unsupported input type for sigmoid activation")

    @staticmethod
    def apply_relu(input):
        if isinstance(input, Matrix):
            result = Matrix(input.rows, input.cols)
            for i in range(input.rows):
                for j in range(input.cols):
                    result[i][j] = ActivationFunctions.relu(input[i][j])
            return result
        
        if isinstance(input, Vector):
            result = Vector(len(input))
            for i in range(len(input)):
                result[i] = ActivationFunctions.relu(input[i])
            return result
        
        raise ValueError("Unsupported input type for ReLU activation")

    @staticmethod
    def apply_sigmoid_derivative(input):
        if isinstance(input, Matrix):
            result = Matrix(input.rows, input.cols)
            for i in range(input.rows):
                for j in range(input.cols):
                    result[i][j] = ActivationFunctions.sigmoid_derivative(input[i][j])
            return result
        
        if isinstance(input, Vector):
            result = Vector(len(input))
            for i in range(len(input)):
                result[i] = ActivationFunctions.sigmoid_derivative(input[i])
            return result
        
        raise ValueError("Unsupported input type for sigmoid derivative")

# # Example usage
# matrix = Matrix(2, 2)
# matrix[0] = [1, -2]
# matrix[1] = [-3, 4]

# vector = Vector(3)
# vector[0] = -1
# vector[1] = 2
# vector[2] = 3

# print("Matrix:")
# print(matrix)

# print("Vector:")
# print(vector)

# sigmoid_matrix = ActivationUtils.apply_sigmoid(matrix)
# print("Sigmoid(Matrix):")
# print(sigmoid_matrix)

# relu_vector = ActivationUtils.apply_relu(vector)
# print("ReLU(Vector):")
# print(relu_vector)
