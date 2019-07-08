import numpy as np

tol = 0.5e-4

def f(x):
    return np.pi * x ** 2 * (1 - (1 / 3) * x) - 1


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
    ans = bisec(f, 0, 2, tol)
    print(ans)