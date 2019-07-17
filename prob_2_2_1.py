import numpy as np


def lu_factorization(A) :
    L = np.identity(A.shape[0])
    U = A
    for i in range(A.shape[0]):
        if U[i, i] == 0:
            exit(-1)
        for j in range(i + 1, A.shape[0]):
            multi = A[j, i] / A[i, i]
            L[j, i] = multi
            for k in range(i, A.shape[0]):
                U[j, k] = A[j, k] - multi * A[i, k]
    return L, U


if __name__ == '__main__':
    A = np.array([[3, 1, 2],
                  [6, 3, 4],
                  [3, 1, 5]])

    L, U = lu_factorization(A)
    print("L=", L)
    print("U=", U)
