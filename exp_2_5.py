import numpy as np

tol = 0.5e-8

def jacobi(A, b):
    D = np.zeros(A.shape)
    L = np.zeros(A.shape)
    U = np.zeros(A.shape)
    u = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i < j:
                U[i, j] = A[i, j]
            elif i > j:
                L[i, j] = A[i, j]
            else:
                D[i, j] = A[i, j]
    while np.abs(np.max(np.dot(A, u) - b)) > tol:
        u = np.linalg.inv(D).dot(b - np.dot(L + U, u))
    return u

def gauss_seidel(A, b):
    D = np.zeros(A.shape)
    R = np.zeros(A.shape)
    u = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i != j:
                R[i, j] = A[i, j]
            else:
                D[i, j] = A[i, j]
    D_inv = np.linalg.inv(D)

    while np.abs(np.max(np.dot(A, u) - b)) > tol:
        for i in range(A.shape[0]):
            u[i] = D_inv[i, i] * (b[i] - np.dot(R[i], u.transpose()))
    return u

def SOR(A, b, w):
    D = np.zeros(A.shape)
    R = np.zeros(A.shape)
    u = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i != j:
                R[i, j] = A[i, j]
            else:
                D[i, j] = A[i, j]
    D_inv = np.linalg.inv(D)

    while np.abs(np.max(np.dot(A, u) - b)) > tol:
        for i in range(A.shape[0]):
            u[i] = (1 - w) * u[i] + w * (D_inv[i, i] * (b[i] - np.dot(R[i], u.transpose())))
    return u

if __name__ == '__main__':
    A = np.array([[3, 1],
                  [1, 2]])
    b = np.array([5, 5])
    x = SOR(A, b, 1.25)
    print(x, np.dot(A, x) - b)
