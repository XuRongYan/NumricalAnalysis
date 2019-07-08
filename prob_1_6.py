import numpy as np
from pylab import *

#画出三个函数的图，利用二分法求出长度为1的解区间，求精确到小数点六位的根

tol = 0.5e-6


def f1(x):
    return np.sin(x) - np.cos(x)

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
    ans1 = bisec(f1, 0, 1, tol)
    print(ans1)

