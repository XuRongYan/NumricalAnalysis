import numpy as np
from scipy.optimize import *


def f(x):
    return np.sin(x) - x


if __name__ == '__main__':
    ans = fsolve(f, np.array([0.1]))
    print("FE=", ans - np.zeros(1), "BE=", f(ans))
