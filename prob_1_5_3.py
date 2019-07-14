import numpy as np

tol = 0.5e-8

f1 = lambda x: x ** 3 - 2 * x - 2

f2 = lambda x: np.exp(x) + x - 7

f3 = lambda x: np.exp(x) + np.sin(x) - 4


def IQI(f, x0, x1, x2):
    xi = x0
    xi1 = x1
    xi2 = x2
    while np.abs(f(xi)) > tol:
        q = f(xi) / f(xi1)
        r = f(xi2) / f(xi1)
        s = f(xi2) / f(xi)
        xi3 = xi2 - (r * (r - q) * (xi2 - xi1) + (1 - r) * s * (xi2 - xi)) / ((q - 1) * (r - 1) * (s - 1))
        xi = xi3

    return xi


if __name__ == '__main__':
    ans1 = IQI(f1, 1, 2, 3)
    ans2 = IQI(f2, 1, 2, 3)
    ans3 = IQI(f3, 1, 2, 3)
    print(ans1, f1(ans1))
    print(ans2, f2(ans2))
    print(ans3, f3(ans3))
