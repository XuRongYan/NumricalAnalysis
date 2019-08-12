import numpy as np


def qr_classical(A):
    r = np.zeros((A.shape[0], A.shape[0]))
    q = np.zeros((A.shape[0], A.shape[0]))
    Ad1 = A.shape[1]
    for i in range(A.shape[1], A.shape[0]):
        t = i - A.shape[1]
        s = np.zeros((A.shape[0], 1))
        s[t] = 1
        A = np.append(A, s, axis=1)
    for j in range(A.shape[1]):
        y = A[:, j]
        for i in range(j):
            r[i, j] = np.matmul(q[:, i].transpose(), A[:, j])
            y = y - r[i, j] * q[:, i]
        r[j, j] = np.linalg.norm(y)
        q[:, j] = y / r[j, j]
    return q, r[:, 0: Ad1]

def qr_improved(A):
    r = np.zeros((A.shape[0], A.shape[0]))
    q = np.zeros((A.shape[0], A.shape[0]))
    Ad1 = A.shape[1]
    for i in range(A.shape[1], A.shape[0]):
        t = i - A.shape[1]
        s = np.zeros((A.shape[0], 1))
        s[t] = 1
        A = np.append(A, s, axis=1)
    for j in range(A.shape[1]):
        y = A[:, j]
        for i in range(j):
            r[i, j] = np.matmul(q[:, i].transpose(), y)
            y = y - r[i, j] * q[:, i]
        r[j, j] = np.linalg.norm(y)
        q[:, j] = y / r[j, j]
    return q, r[:, 0: Ad1]

def qr_householder(A):
    R = A
    Q = np.eye(A.shape[0])
    for j in range(A.shape[1]):
        w = np.zeros(A.shape[0] - j)
        x = R[j:, j]
        w[0] = np.linalg.norm(x)
        v = w - x
        v = v[:, np.newaxis]
        P = (1 / np.matmul(v.transpose(), v)) * np.matmul(v, v.transpose())
        H = np.eye(A.shape[0])
        H[j:, j:] = np.eye(A.shape[0] - j) - 2 * P
        Q = np.matmul(Q, H)
        R = np.matmul(H, R)

    return Q, R



def least_square_qr(A, b):
    q, r = qr_householder(A)
    d = np.matmul(q.transpose(), b)
    x = np.zeros(A.shape[1])
    for i in range(A.shape[1] - 1, -1, -1):
        for j in range(i + 1, A.shape[1]):
            d[i] -= x[j] * r[i, j]
        x[i] = d[i] / r[i, i]
    return x




if __name__ == '__main__':
    A = np.array([[1, -4],
                  [2, 3],
                  [2, 2]])
    b = np.array([-3, 15, 9])
    x = least_square_qr(A, b)
    print(x)

