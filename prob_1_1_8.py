import numpy as np
from scipy.linalg import hilbert

tol = 0.5e-6
A = hilbert(5)
def f(x):
    A[0, 0] = x
    a, _ = np.linalg.eig(A)
    return max(a) - np.pi


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
    ans = bisec(f, -10, 10, tol)
    print(ans)