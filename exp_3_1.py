import numpy as np
from pylab import *

def newtondd(x, y):
    v = np.zeros((y.shape[0], y.shape[0]))
    c = np.zeros(y.shape[0])
    for i in range(y.shape[0]):
        v[0][i] = y[i]

    for i in range(1, y.shape[0]):
        for j in range(y.shape[0] - i):
            v[i][j] = (v[i - 1][j + 1] - v[i - 1][j]) / (x[j + i] - x[j])
    for i in range(y.shape[0]):
        c[i] = v[i][0]

    return c

def p(x, p, c):
    res = 0
    plus = 1
    for i in range(c.shape[0]):
        res += c[i] * plus
        plus *= (x - p[i])
    return res


if __name__ == '__main__':
    x = np.array([0, 2, 3])
    y = np.array([1, 2, 4])
    c = newtondd(x, y)
    print(c)
    plot(x, y, 'or')
    _x = np.linspace(0, 3)
    _y = p(_x, x, c)
    plot(_x, _y)
    show()