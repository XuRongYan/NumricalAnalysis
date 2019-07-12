import numpy as np
from scipy.misc import *

tol = 0.5e-8

f1 = lambda x: 14 * x * np.exp(x - 2) - 12 * np.exp(x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12


def newton(f, x0, m=1):
    ei_1 = 0
    xi = x0
    i = 1
    while derivative(f, xi, 1e-12) != 0 and np.abs(f(xi)) >= tol:
        ei = f(xi)
        if ei_1 != 0:
            ei_divide_ei_1 = ei / ei_1
        else:
            ei_divide_ei_1 = 0
        print("%d:" % i, "xi =", xi, "ei =", f(xi), "ei/ei-1 = ", ei_divide_ei_1)
        xi_1 = xi - m * f(xi) / derivative(f, xi, 1e-12)
        i += 1
        xi = xi_1
        ei_1 = ei
        if i > 50:
            break
    return xi, i


if __name__ == '__main__':
    ans1, _ = newton(f1, 3)
    print(ans1, f1(ans1))
    ans2, _ = newton(f1, 0)
    print(ans2, f1(ans2))

