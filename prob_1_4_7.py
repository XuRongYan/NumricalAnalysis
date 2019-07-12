import numpy as np
from scipy.misc import *
from matplotlib import pyplot

tol = 0.5e-8

f1 = lambda x: np.exp(np.sin(x) ** 3) + x ** 6 - 2 * (x ** 4) - x ** 3 - 1


def newton(f, x0, m=1):
    xi = x0
    i = 0
    while np.abs(f(xi)) >= tol:
        xi_1 = xi - m * f(xi) / derivative(f, xi, 2e-12)
        i += 1
        xi = xi_1
        if i > 50:
            break
    return xi, i


def getM(f, r):
    if derivative(f, r, 2e-12) == 0:
        return False
    else:
        return derivative(f, r, 2e-12, 2) / derivative(f, r, 2e-12) / 2


def getm(f, r):
    i = 1
    while derivative(f, r, 1e-130, i, order=5) == 0:
        i += 1
    return i + 1


if __name__ == '__main__':
    x = np.linspace(-2, 2, 50)
    y = f1(x)
    pyplot.plot(x, y)
    pyplot.show()
    ans1, _ = newton(f1, 2)
    ans2, _ = newton(f1, -2)
    ans3, _ = newton(f1, 0)
    print(f1(1.53))
    print(ans1, f1(ans1))
    print(ans2, f1(ans2))
    print(ans3, f1(ans3))
    M1 = getM(f1, ans1)
    M2 = getM(f1, ans2)
    M3 = getM(f1, ans3)
    if M1 is False:
        m = getm(f1, ans1)
        print("M1不能二次收敛, 有%d重根" % m)
    else:
        print("M1可以二次收敛")

    if M2 is False:
        m = getm(f1, ans2)
        print("M2不能二次收敛, 有%d重根" % m)
    else:
        print("M2可以二次收敛")

    if M3 is False:
        m = getm(f1, ans3)
        print("M3不能二次收敛, 有%d重根" % m)
    else:
        print("M3可以二次收敛")
