import numpy as np

# 二分法求f1, f2, f3三个函数的零点，误差小于小数点后8位

tol = 0.5e-8


def f1(x):
    return x ** 5 + x - 1

def f2(x):
    return np.sin(x) - 6 * x - 5


def f3(x):
    return np.log(x) + x ** 2 - 3


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
    ans1 = bisec(f1, -100, 100, tol)
    ans2 = bisec(f2, -100, 100, tol)
    ans3 = bisec(f3, 0.01, 100, tol)
    print("ans1 = " + str(ans1))
    print("ans2 = " + str(ans2))
    print("ans3 = " + str(ans3))
