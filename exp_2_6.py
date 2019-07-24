import numpy as np

tol = 0.5e-8


def cholesky(A, b):
    #cholesky分解
    R = np.zeros(A.shape)
    for i in range(A.shape[0]):
        if A[i, i] <= 0:
            exit(-1)
        R[i, i] = np.sqrt(A[i, i])
        u = A[i, i + 1:] / R[i, i]
        u = u[np.newaxis, :]
        R[i, i + 1:] = u
        A[i + 1:, i + 1:] = A[i + 1:, i + 1:] - np.matmul(u.transpose(), u)
    #R_t * c = b
    R_t = R.transpose()
    c = np.zeros(R_t.shape[0])
    for i in range(R_t.shape[0]):
        for j in range(i):
            b[i] -= R_t[i, j] * c[j]
        c[i] = b[i] / R_t[i, i]
    x = np.zeros(A.shape[0])
    #Rx = c
    for i in range(R.shape[0] - 1, -1, -1):
        for j in range(i + 1, R.shape[0]):
            c[i] -= R[i, j] * x[j]
        x[i] = c[i] / R[i, i]
    return x

def conjugate_gradient_method(A, b):
    x = np.zeros(A.shape[0])
    d = r = b - np.matmul(A, x.transpose())
    for i in range(A.shape[0]):
        if np.abs(np.max(A)) == 0:
            exit(-1)
        a = np.matmul(r, r.transpose()) / np.matmul(np.matmul(d.transpose(), A), d)
        x = x + a * d
        r_k = r - a * np.matmul(A, d.transpose())
        beta = np.matmul(r_k, r_k.transpose()) / np.matmul(r, r.transpose())
        d = r_k + beta * d
        r = r_k
    return x







if __name__ == '__main__':
    A = np.array([[2, 2],
                  [2, 5]])

    b = np.array([6, 3], dtype=np.float64)

    x = conjugate_gradient_method(A, b)
    print(x, np.matmul(A, x.transpose()) - b)

