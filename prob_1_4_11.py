import numpy as np
from scipy.misc import *

tol = 0.5e-8
p = 15
n = 1
a = 1.36
b = 0.003183
t = 320
r = 0.0820578

f1 = lambda v: (p + a * n ** 2 / v ** 2) * (v - n * b) - n * r * t


def newton(f, x0, m=1):
    # ei_1 = 0
    xi = x0
    i = 1
    while derivative(f, xi, 1e-12) != 0 and np.abs(f(xi)) >= tol:
        # ei = f(xi)
        # if ei_1 != 0:
        #     ei_divide_ei_1 = ei / ei_1
        # else:
        #     ei_divide_ei_1 = 0
        # print("%d:" % i, "xi =", xi, "ei =", f(xi), "ei/ei-1 = ", ei_divide_ei_1)
        xi_1 = xi - m * f(xi) / derivative(f, xi, 1e-12)
        i += 1
        xi = xi_1
        # ei_1 = ei
        if i > 50:
            break
    return xi, i


if __name__ == '__main__':
    v, _ = newton(f1, 0.5)
    print(0.5, v)
