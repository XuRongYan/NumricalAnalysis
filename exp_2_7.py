import numpy as np

def F(x):
    y1 = x[0][1] - x[0][0] ** 3
    y2 = x[0][0] ** 2 + x[0][1] ** 2 - 1
    return np.array([[y1, y2]])

def broyden(F):
    B = np.eye(2)
    x = np.zeros((1, 2))
    for i in range(10):
        x_1 = x - np.matmul(B, F(x).transpose()).transpose()
        delta_x = x_1 - x
        delta_y = F(x_1) - F(x)
        delta_x_Bi_delta_y = delta_x - np.matmul(B, delta_y.transpose()).transpose()
        mat_up = np.matmul(delta_x_Bi_delta_y.transpose(), delta_x)
        mat_up = np.matmul(mat_up, B)
        mat_down = np.matmul(delta_x, B)
        mat_down = np.matmul(mat_down, delta_y.transpose())
        B = B + mat_up / mat_down
        x = x_1

    return x

if __name__ == '__main__':
    x = broyden(F)
    print(x)
