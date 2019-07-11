import numpy as np

tol = 0.5e-8
max_it = 50


def f1(x):
    return (1 - x) ** (1 / 5)


def f2(x):
    return (np.sin(x) - 5) / 6


def f3(x):
    return np.log(3 - x ** 2)


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
    ans1 = fpi(f1, 0.5)
    print("%.8f" % ans1, "error=", f1(ans1) - ans1)
    ans2 = fpi(f2, 0)
    print("%.8f" % ans2, "error=", f2(ans2) - ans2)
    ans3 = fpi(f3, 0)
    print("%.8f" % ans3, "error=", f3(ans3) - ans3)
