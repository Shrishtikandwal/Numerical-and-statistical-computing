def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def newton_raphson(x0, tol=1e-6, max_iter=100):
    print("Iter\tx\t\tf(x)")
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Zero derivative. No solution found.")
            return None
        x1 = x0 - fx / dfx
        print(f"{i+1}\t{round(x0,6)}\t{round(fx,6)}")
        if abs(x1 - x0) < tol:
            print(f"\nRoot found: {x1} after {i+1} iterations")
            return x1
        x0 = x1
    print("\nMethod did not converge.")
    return None

x0 = 1.5
newton_raphson(x0)
