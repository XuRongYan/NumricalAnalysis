import numpy as np
from scipy.optimize import *

ebshino = 1e-3


def f(x):
    return x ** 3 - 3 * x ** 2 + x - 3


if __name__ == '__main__':
    deltaR = -ebshino * 3 ** 3 / 10
    ans = fsolve(f, np.array(0))
    print(deltaR)
    print(ans)