import numpy as np


#画出三个函数的图，利用二分法求出长度为1的解区间，求精确到小数点六位的根

tol = 0.5e-6


def f1(x):
    mat = np.array([[1, 2, 3, x],
                    [4, 5, x, 6],
                    [7, x, 8, 9],
                    [x, 10, 11, 12]])
    return np.linalg.det(mat) - 1000

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
    ans1 = bisec(f1, 9, 10, tol)
    print(f1(ans1) + 1000)
    print(ans1)