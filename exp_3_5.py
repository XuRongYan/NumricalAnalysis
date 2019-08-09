import numpy as np
from pylab import *


def bessel(x, y):
    b_x = 3 * (x[1] - x[0])
    c_x = 3 * (x[2] - x[1]) - b_x
    d_x = x[3] - x[0] - b_x - c_x
    b_y = 3 * (y[1] - y[0])
    c_y = 3 * (y[2] - y[1]) - b_y
    d_y = y[3] - y[0] - b_y - c_y

    x_t = np.array([x[0], b_x, c_x, d_x])
    y_t = np.array([y[0], b_y, c_y, d_y])
    return x_t, y_t


def poly(x, t):
    res = 0
    eq = 1
    for i in range(x.shape[0]):
        res += x[i] * eq
        eq *= t
    return res


if __name__ == '__main__':
    x = np.array([1, 1, 3, 2])
    y = np.array([1, 3, 3, 2])
    x_t, y_t = bessel(x, y)
    t = np.linspace(-1, 1)
    x_ = poly(x_t, t)
    y_ = poly(y_t, t)
    plot(x, y, 'or')
    plot(x_, y_)
    show()
