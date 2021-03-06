import numpy as np


def gaussian_eliminate(a, b):
    x = np.zeros(a.shape[0])
    # 消去
    for i in range(a.shape[0]):
        if a[i, i] == 0:
            exit(-1)
        for j in range(i + 1, a.shape[0]):
            multi = a[j, i] / a[i, i]
            for k in range(j, a.shape[0]):
                a[j, k] -= multi * a[i, k]
            b[j] -= multi * b[i]
    print("a=", a)
    # 回代
    for i in range(a.shape[0] - 1, -1, -1):
        for j in range(i + 1, a.shape[0]):
            b[i] -= a[i, j] * x[j]
        x[i] = b[i] / a[i, i]
    print("b=", b)
    return x


if __name__ == '__main__':
    a = np.array([[2, -2, -1],
                  [4, 1, -2],
                  [-2, 1, -1]])
    b = np.array([-2, 1, 3])

    x = gaussian_eliminate(a, b)
    print("x=", x)
