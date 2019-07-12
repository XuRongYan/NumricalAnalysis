import numpy as np
from scipy.misc import *
from matplotlib import pyplot

tol = 0.5e-8

f1 = lambda x: (1 - 3 / (4 * x)) ** (1 / 3)


def newton(f, x0, m=1):
    iter = np.zeros(50)
    xi = x0
    i = 0
    while derivative(f, xi, 1e-12) != 0 and np.abs(f(xi)) >= tol:
        iter[i] = xi
        xi_1 = xi - m * f(xi) / derivative(f, xi, 1e-12)
        i += 1
        xi = xi_1
        if i >= 50:
            break
    return xi, iter


if __name__ == '__main__':
    ans, iter = newton(f1, 1.75)
    x = np.linspace(-5, 5, 50)
    y1 = f1(x[(x != 0.)])
    idx = (iter != 0)
    y2 = f1(iter[idx])
    pyplot.plot(x[x != 0], y1)
    pyplot.plot(iter[idx], y2, 'or')
    pyplot.show()
