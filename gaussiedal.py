import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    n = len(A)
    x = x0.copy()
    print("Iter\tSolution")
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i+1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        print(f"{k+1}\t{np.round(x_new, 6)}")
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"\nSolution found after {k+1} iterations")
            return x_new
        x = x_new
    print("\nMethod did not converge.")
    return x

A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]], dtype=float)
b = np.array([6, 25, -11], dtype=float)
x0 = np.zeros(len(b))

gauss_seidel(A, b, x0)
