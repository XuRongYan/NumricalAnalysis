import numpy as np

tol = 0.5e-8

f1 = lambda x: x ** 3 - 2 * x - 2

f2 = lambda x: np.exp(x) + x - 7

f3 = lambda x: np.exp(x) + np.sin(x) - 4


def secant(f, x0, x1):
    xi = x1
    xi_1 = x0
    i = 0
    while f(xi) - f(xi_1) != 0 and np.abs(f(xi)) >= tol:
        xi1 = xi - (f(xi) * (xi - xi_1)) / (f(xi) - f(xi_1))
        xi_1 = xi
        xi = xi1
        i += 1
    return xi


if __name__ == '__main__':
    ans1 = secant(f1, 1, 2)
    ans2 = secant(f2, 1, 2)
    ans3 = secant(f3, 1, 2)
    print(ans1, f1(ans1))
    print(ans2, f2(ans2))
    print(ans3, f3(ans3))