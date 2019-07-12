import numpy as np
from scipy.misc import *

tol = 0.5e-8

f1 = lambda x: 2 / 3 * np.pi * x ** 3 + 10 * np.pi * x ** 2 - 400


def newton(f, x0, m=1):
    xi = x0
    i = 0
    while derivative(f, xi, 2e-12) != 0 and np.abs(f(xi) / derivative(f, xi, 2e-12)) >= tol:
        xi_1 = xi - m * f(xi) / derivative(f, xi, 2e-12)
        i += 1
        xi = xi_1
        if i > 50:
            break
    return xi, i


if __name__ == '__main__':
    ans1, _ = newton(f1, 5)
    print("%.4f" % ans1, f1(ans1))
