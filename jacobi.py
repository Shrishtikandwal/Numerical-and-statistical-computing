import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iter=100):
    n = len(A)
    x = x0.copy()
    print("Iter\tSolution")
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
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

jacobi(A, b, x0)
