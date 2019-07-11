import numpy as np
from scipy.optimize import *

tol = 0.5e-6
max_it = 50


def f11(x):
    return ((6 * x + 1) / 2) ** (1 / 3)


def fpi(g, xi):
    """
    不动点迭代
    :param g: 函数
    :param xi: 初识点
    :return: 迭代结果
    """
    xi_1 = g(xi)
    i = 0
    while np.abs(xi_1 - xi) > tol and i in range(max_it):
        xi = xi_1
        xi_1 = g(xi)
        i += 1
    return xi_1, i + 1


if __name__ == '__main__':
    fsolve()
    pass
