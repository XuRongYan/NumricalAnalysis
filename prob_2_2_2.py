import numpy as np

def lu_factorization(A, b) :
    L = np.identity(A.shape[0])
    U = A
    #LU分解
    for i in range(A.shape[0]):
        if U[i, i] == 0:
            exit(-1)
        for j in range(i + 1, A.shape[0]):
            multi = A[j, i] / A[i, i]
            L[j, i] = multi
            for k in range(i, A.shape[0]):
                U[j, k] = A[j, k] - multi * A[i, k]

    #第一次回代Lc = b
    c = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        for j in range(i):
            b[i] -= L[i, j] * c[j]
        c[i] = b[i] / L[i, i]

    #第二次回代Ux = c
    x = np.zeros(A.shape[0])
    for i in range(A.shape[0] - 1, -1, -1):
        for j in range(i + 1, A.shape[0]):
            c[i] -= U[i, j] * x[j]
        x[i] = c[i] / U[i, i]
    return x


if __name__ == '__main__':
    A = np.array([[4, -2, 2],
                  [-2, 2, -4],
                  [2, -4, 11]])
    b = np.array([0, 1, 2])
    x = lu_factorization(A, b)
    print("x=", x, "Ax", A.dot(x.transpose()))
