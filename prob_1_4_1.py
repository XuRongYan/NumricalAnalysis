import numpy as np
from scipy.misc import *

tol = 0.5e-8

f1 = lambda x: x ** 3 - 2 * x - 2

f2 = lambda x: np.exp(x) + x - 7

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


if __name__ == '__main__':
    ans1, _ = newton(f1, 3)
    print(ans1, f1(ans1))
    ans2, _ = newton(f2, 0)
    print(ans2, f2(ans2))
    ans3, _ = newton(f3, 0)
    print(ans3, f3(ans3))
