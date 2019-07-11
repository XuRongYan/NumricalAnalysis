import numpy as np

tol = 0.5e-8
max_it = 50


def f1(x):
    return (2 * x + 2) ** (1 / 3)


def f2(x):
    return ((7 - np.exp(x) + x) / 2 + x) / 2


def f3(x):
    return np.log(4 - np.sin(x))


def fpi(g, xi):
    """
    不动点迭代
    :param g: 函数
    :param xi: 初识点
    :return: 迭代结果
    """
    xi_1 = g(xi)
    i = 0
    while np.abs(xi_1 - xi) > tol and i in range(max_it):
        xi = xi_1
        xi_1 = g(xi)
        i += 1
    return xi_1


if __name__ == '__main__':
    ans1 = fpi(f1, 0)
    print(ans1, "error=", f1(ans1) - ans1)
    ans2 = fpi(f2, 0)
    print(ans2, "error=", f2(ans2) - ans2)
    ans3 = fpi(f3, 0)
    print(ans3, "error=", f3(ans3) - ans3)
