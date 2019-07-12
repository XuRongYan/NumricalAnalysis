import numpy as np
from scipy.misc import *

tol = 0.5e-8

f1 = lambda x: 27 * x ** 3 + 54 * x ** 2 + 36 * x + 8

f2 = lambda x: 36 * x ** 4 - 12 * x ** 3 + 37 * x ** 2 - 12 * x + 1

f3 = lambda x: np.exp(x) + np.sin(x) - 4


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


def root(f, r):
    i = 1
    while derivative(f, r, dx=2e-12, n=i, order=5) == 0:
        i += 1
    return i + 1


if __name__ == '__main__':
    ans1, _ = newton(f1, -2)
    m1 = root(f1, ans1)
    print(ans1, f1(ans1), m1)
    ans1, _ = newton(f1, -2, m1)
    print(ans1, f1(ans1))
    ans2, _ = newton(f2, 1)
    m2 = root(f2, ans2)
    print(ans2, f2(ans2), m2)
    ans2, _ = newton(f2, 1, m2)
    print(ans2, f2(ans2))
