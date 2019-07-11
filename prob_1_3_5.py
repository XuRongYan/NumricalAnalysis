import numpy as np
from scipy.optimize import *


def f(x):
    return (x - 1) * (x - 2) * (x - 3) * (x - 4) - 1e-6 * x ** 6


if __name__ == '__main__':
    ans = bisect(f, 3.5, 4.5)

    print(ans)
