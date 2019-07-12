import numpy as np
import math
from scipy.optimize import *
from scipy.misc import *
from matplotlib import pyplot


def f(x):
    res = 1
    for i in range(15):
        res = res * (x - i - 1)
    return res - 2e-12 * x ** 15


if __name__ == '__main__':
    ans = bisect(f, 14.5, 15.1)
    print(ans, 2e-12 * 15 ** 15 / math.factorial(14))
