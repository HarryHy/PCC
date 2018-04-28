import numpy as np
import math
def softmax(x):
    #x -- A numpy matrix of shape (n,m)

    #s -- A numpy matrix equal to the softmax of x, of shape (n,m)
    
    # Apply exp() element-wise to x. Use np.exp(...).
    x_exp = np.exp(x)

    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).
    x_sum = np.sum(x_exp,axis = 1, keepdims = True)
    
    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.
    s = x_exp/x_sum
    
    return s
    
