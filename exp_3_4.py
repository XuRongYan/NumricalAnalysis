import numpy as np
from pylab import *


def splinecoeff(x, y):
    A = np.zeros((x.shape[0], x.shape[0]))
    r = np.zeros((x.shape[0], 1))
    dx = np.zeros(x.shape[0])
    dy = np.zeros(x.shape[0])
    for i in range(x.shape[0] - 1):
        dx[i] = x[i + 1] - x[i]
        dy[i] = y[i + 1] - y[i]

    for i in range(1, x.shape[0] - 1):
        A[i, i - 1:i + 2] = np.array([dx[i - 1], 2 * (dx[i - 1] + dx[i]), dx[i]])
        r[i] = 3 * (dy[i] / dx[i] - dy[i - 1] / dx[i - 1])

    A[0][0] = 1
    A[x.shape[0] - 1][x.shape[0] - 1] = 1

    coeff = np.zeros((x.shape[0], 3))
    coeff[:][1] = np.matmul(np.linalg.inv(A), r).reshape(3)
    for i in range(x.shape[0] - 1):
        coeff[i][2] = (coeff[i + 1][1] - coeff[i][1]) / (3 * dx[i])
        coeff[i][0] = dy[i] / dx[i] - dx[i] * (2 * coeff[i][1] + coeff[i + 1][1]) / 3

    return coeff[0: x.shape[0] - 1][0: 3]


def spline_plot(x, y, k = 50):
    n = x.shape[0]
    coeff = splinecoeff(x, y)
    x1 = np.array([])
    y1 = np.zeros([])
    for i in range(n - 1):
        xs = np.linspace(x[i], x[i + 1], k)
        dx = xs - x[i]
        ys = coeff[i][2] * dx
        ys = (ys + coeff[i][1]) * dx
        ys = (ys + coeff[i][0]) * dx + y[i]
        x1 = np.append(x1, xs[0: k])
        y1 = np.append(y1, ys[0: k])

    plot(x1, y1[1: y1.shape[0]])
    plot(x, y, 'or')
    show()

if __name__ == '__main__':
    x = np.array([0, 1, 2])
    y = np.array([3, -2, 1])
    spline_plot(x, y)


