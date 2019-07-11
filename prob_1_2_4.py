import numpy as np

tol = 0.5e-8
max_it = 50


def f1(x):
    return (1 / 3) * (2 / x ** 2 + 2 * x)


def f2(x):
    return (1 / 3) * (3 / x ** 2 + 2 * x)


def f3(x):
    return (1 / 3) * (5 / x ** 2 + 2 * x)


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
    return xi_1, i


if __name__ == '__main__':
    ans1, i1 = fpi(f1, 1)
    print("%.8f" % ans1, "error=", f1(ans1) - ans1, "it=", i1)
    ans2, i2 = fpi(f2, 1)
    print("%.8f" % ans2, "error=", f2(ans2) - ans2, "it=", i2)
    ans3, i3 = fpi(f3, 1)
    print("%.8f" % ans3, "error=", f3(ans3) - ans3, "it=", i3)
