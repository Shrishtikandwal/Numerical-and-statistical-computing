def f(x):
    return x**3 - x - 2

def secant_method(x0, x1, tol=1e-6, max_iter=100):
    print("Iter\tx0\t\tx1\t\tx2\t\tf(x2)")
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Divide by zero error!")
            return None
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"{i+1}\t{round(x0,6)}\t{round(x1,6)}\t{round(x2,6)}\t{round(f(x2),6)}")
        if abs(x2 - x1) < tol:
            print(f"\nRoot found: {x2} after {i+1} iterations")
            return x2
        x0, x1 = x1, x2
    print("\nMethod did not converge.")
    return None

x0 = 1
x1 = 2
secant_method(x0, x1)
