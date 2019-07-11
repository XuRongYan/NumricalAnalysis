import numpy as np


def f(x):
    return np.cos(x)


def fpi(g, x0, k):
    """
    不动点迭代
    :param g: 函数
    :param x0: 初识点
    :param k: 迭代次数
    :return: 迭代结果
    """
    for i in range(k):
        x0 = g(x0)
    return x0


if __name__ == '__main__':
    ans = fpi(f, 0, 50)
    print(ans)
