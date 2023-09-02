# Import necessary classes from the NeuroSRC package
from NeuroSRC.LinearAlgebra import activations, matrix, vector

class NeuralNetwork:
  def __init__(self, inp, hdn, out):
    self.input_size  = inp
    self.output_size = out
    self.hidden_size = hdn

    layn = len(hdn) + 2
    self.layn = layn
    all_layers = [inp] + hdn + [out]
    self.weights = []
    for i in range(layn):
      if i-1 < 0: continue
      w = matrix.Matrix(all_layers[i-1],all_layers[i])
      
      w.randomize(-1,1)
      print(f"W_{i} as index {i-1}: {w}")
      self.weights.append(w)

  def forward(self, X):
    self.zl = ["NULL"]
    self.al = [X]
    holding = X
    i = 0
    for layerW in self.weights:
      i+=1
      z = layerW.multiply_addingon(holding)
      print(f"Z_{i+1} denoted as {i}: {z}")
      self.zl.append(z)
      a_n = activations.ActivationUtils.apply_sigmoid(z)
      print(f"A_{i+1} denoted as {i}: {a_n}")
      self.al.append(a_n)
      holding = a_n
    y_hat = holding
    return y_hat

  def cost_function(self, x, y):
    self.y_hat = self.forward(x)
    diffy =  y.subtract(self.y_hat)
    C = 0.5 * diffy.square().sumup()
    return C

  def cost_function_deriv(self, x,y):
    self.y_hat = self.forward(x)

    delta3 = self.y_hat.subtract(y).multiply_elementwise(activations.ActivationUtils.apply_sigmoid_derivative(self.zl[2]))
    print("DELTA3",delta3)
    a2t = self.al[1]
    a2t.transpose()
    dJdW2 = a2t.multiply_addingon(delta3)

    w2t = self.weights[1]
    w2t.transpose()
    print("HE",delta3.multiply_addingon(w2t))
    delta2 = delta3.multiply_addingon(w2t).multiply_brodcast(self.zl[1])
    dJdW1 = x.transpose().multiply(delta2)
    print(dJdW2, dJdW1)
    return dJdW1, dJdW2
    # self.y_hat = self.forward(x)
    # dJdW_n_last = []
    # print("SZL",self.layn-1)
    # print("AZL",self.layn-2)
    
    # delta_current = y.subtract(self.y_hat).multiply_scalar(-1).multiply_elementwise(activations.ActivationUtils.apply_sigmoid_derivative(self.zl[self.layn-1]))
    # an_t = self.al[self.layn-1]
    # an_t.transpose()
  
    # print("ANT",an_t)
    # print("DC",delta_current)
    # dJdW_n_last.append(an_t.multiply_addingon(delta_current))
    # for r in range(self.layn-1,1,-1):
    #   print(f"SZLR({r})",r-1)
    #   print(f"AZLR({r})",r-2)
    #   print(f"WZLR({r})",r-1)
    #   wt = self.weights[r-1]
    #   wt.transpose()
    #   print("DC*WT", delta_current.multiply_addingon(wt))
    #   print("Z",self.zl[r])
    #   delta_current = delta_current.multiply_addingon(wt).multiply_addingon(activations.ActivationUtils.apply_sigmoid_derivative((self.zl[r-1])))
    #   print("DCAA",delta_current)
    #   dJdW_n_last.append(self.al[r-2].multiply_addingon(delta_current))
    # print(dJdW_n_last)
    
    

                                                                               
                                                                               
    
    
    
    