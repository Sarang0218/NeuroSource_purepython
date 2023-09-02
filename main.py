from NeuroSRC.Models.Classic.classic import *
from NeuroSRC.LinearAlgebra.standardize import Standardize


# Create training data
input_data = [vector.Vector([3, 5,4,2]), vector.Vector([5, 1,3,4]), vector.Vector([10, 2,4,2])]
target_data = [vector.Vector([75]), vector.Vector([82]), vector.Vector([93])]

test = matrix.Matrix(3,1)
print(test)
print(test.stretch(axis="x",amt=10))
# Make the range 0 to 1
input_data  = Standardize.standardize(input_data)
target_data = Standardize.standardize(target_data)
inp_matrix = Standardize.to_mat(input_data)
trg_matrix = Standardize.to_mat(target_data)
print("INP MATRIX",inp_matrix)
print("TRG MATRIX",trg_matrix)
nn = NeuralNetwork(4, [3], 1)
print("WEIGHTS (first layer)",nn.weights[0])
print("WEIGHTS, data (first)",nn.weights[0].data)
print("FORWARD",nn.forward(inp_matrix))
print("COST",nn.cost_function(inp_matrix, trg_matrix))
nn.cost_function_deriv(inp_matrix, trg_matrix)