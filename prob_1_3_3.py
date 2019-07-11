import numpy as np
from scipy.optimize import *


def f(x):
    return 2 * x * np.cos(x) - 2 * x + np.sin(x ** 3)


# 二分法逼近
def bisec(f, a, b, tol):
    if np.sign(f(a)) * np.sign(f(b)) >= 0:
        print("f(a)*f(b)<0 isn't satisfied")
        return
    i = 0
    while (b - a) / 2 > tol:
        c = (b + a) / 2
        if f(c) == 0:
            break
        elif np.sign(f(a)) * np.sign(f(c)) < 0:
            b = c
        else:
            a = c
        i += 1
    return (a + b) / 2, i


if __name__ == '__main__':
    ans = bisect(f, -0.1, 0.2)
    print("FE=", ans - np.zeros(1), "BE=", f(ans))
    ans1, i = bisec(f, -0.1, 0.2, 0.5e-12)
    print("FE=", ans1 - 0, "BE=", f(ans1), "iteration=", i)
