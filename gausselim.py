import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    Ab = np.hstack([A.astype(float), b.reshape(-1,1)])

    for i in range(n):
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]

        for j in range(i+1, n):
            factor = Ab[j][i] / Ab[i][i]
            Ab[j] = Ab[j] - factor * Ab[i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i][-1] - np.dot(Ab[i][i+1:n], x[i+1:n])) / Ab[i][i]

    print("Solution:")
    for i in range(n):
        print(f"x{i+1} = {round(x[i], 6)}")
    return x

A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

gauss_elimination(A, b)
