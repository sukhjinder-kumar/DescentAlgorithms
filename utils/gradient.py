import numpy as np


def calculate_grad(f, X, dim, h=0.01):
    if dim == 1:
        return (f.subs({'x': X+h}).evalf() -
                f.subs({'x': X}).evalf()) / h
    else:
        gx = (f.subs({'x': X[0][0]+h, 'y': X[1][0]}).evalf()
              - f.subs({'x': X[0][0], 'y': X[1][0]}).evalf()) / h
        gy = (f.subs({'x': X[0][0], 'y': X[1][0] + h}).evalf()
              - f.subs({'x': X[0][0], 'y': X[1][0]}).evalf()) / h
        return np.array([gx, gy]).reshape(2, 1)
