import numpy as np


def f(x):
    return x ** 3 + x - 1


# 二分法逼近
def bisec(f, a, b, tol):
    if np.sign(f(a)) * np.sign(f(b)) >= 0:
        print("f(a)*f(b)<0 isn't satisfied")
        return
    while (b - a) / 2 > tol:
        c = (b + a) / 2
        if f(c) == 0:
            break
        elif np.sign(f(a)) * np.sign(f(c)) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


if __name__ == '__main__':
    xc = bisec(f, 0, 1, 0.00005)
    print(xc)
    print(f(xc))
