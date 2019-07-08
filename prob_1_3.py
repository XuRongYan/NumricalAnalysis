import numpy as np
from pylab import *

#画出三个函数的图，利用二分法求出长度为1的解区间，求精确到小数点六位的根

tol = 0.5e-6


def f1(x):
    return 2 * x ** 3 - 6 * x - 1

def f2(x):
    return np.exp(x - 2) + x ** 3 - x


def f3(x):
    return 1 + 5 * x - 6 * x ** 3 - exp(2 * x)


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
    x = np.linspace(-20, 20, 100)
    y1 = f1(x)
    y2 = f2(x)
    y3 = f3(x)
    subplot(2, 2, 1)
    plot(x, y1, 'r')
    subplot(2, 2, 2)
    plot(x, y2, 'g')
    subplot(2, 2, 3)
    plot(x, y3, 'b')
    show()
    ans1 = bisec(f1, -100, 100, tol)
    ans2 = bisec(f2, -100, 100, tol)
    ans3 = bisec(f3, -100, 100, tol)
    print("区间1：[%d, %d]" % (int(ans1), int(ans1) + 1))
    print("区间2：[%d, %d]" % (int(ans2), int(ans2) + 1))
    print("区间3：[%d, %d]" % (int(ans3), int(ans3) + 1))
    print("ans1 = " + str(ans1))
    print("ans2 = " + str(ans2))
    print("ans3 = " + str(ans3))