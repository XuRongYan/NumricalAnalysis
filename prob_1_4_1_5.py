import numpy as np
from pylab import *

# 求平方根和立方根，精确到小数点六位的根

tol = 0.5e-8


def f1(x, A):
    return x ** 2 - A


def f2(x, A):
    return x ** 3 - A


# 二分法逼近
def bisec(f, a, b, tol, A):
    if np.sign(f(a, A)) * np.sign(f(b, A)) >= 0:
        print("f(a)*f(b)<0 isn't satisfied")
        return
    i = 0
    while (b - a) / 2 > tol:
        c = (b + a) / 2
        if f(c, A) == 0:
            break
        elif np.sign(f(a, A)) * np.sign(f(c, A)) < 0:
            b = c
        else:
            a = c
        i += 1
    return (a + b) / 2, i


if __name__ == '__main__':
    x = np.linspace(-20, 20, 100)
    ans1, it1 = bisec(f1, 0.1, 100, tol, 2)
    ans2, it2 = bisec(f2, -100, 100, tol, 2)
    ans3, it3 = bisec(f1, 0.1, 100, tol, 3)
    ans4, it4 = bisec(f2, -100, 100, tol, 3)
    print("平方根：", ans1, "迭代次数：", it1, "A=", 2)
    print("立方根：", ans2, "迭代次数：", it2, "A=", 2)
    print("平方根：", ans3, "迭代次数：", it3, "A=", 3)
    print("立方根：", ans4, "迭代次数：", it4, "A=", 3)


