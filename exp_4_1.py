import numpy as np
from prob_2_1_1 import *
from prob_2_2_2 import *

def least_square(A, b):
    x = lu_factorization(np.matmul(A.transpose(), A), np.matmul(A.transpose(), b))
    SE = np.linalg.norm(b - np.matmul(A, x), 2)
    RMSE = SE / np.sqrt(x.shape[0])
    return x, SE, RMSE


if __name__ == '__main__':
    A = np.array([[1, 1],
                  [1, -1],
                  [1, 1]], np.float64)
    b = np.array([2, 1, 3], np.float64)
    x, SE, RMSE = least_square(A, b)
    print(x)
    print('SE =', SE)
    print('RMSE =', RMSE)