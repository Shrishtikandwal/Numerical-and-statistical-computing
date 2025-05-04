def f(x):
    return x**3 - x - 2

def regula_falsi(x0, x1, tol=1e-6, max_iter=100):
    if f(x0) * f(x1) >= 0:
        print("Invalid initial guesses.")
        return None
    print("Iter\tx0\t\tx1\t\tx2\t\tf(x2)")
    for i in range(max_iter):
        x2 = x0 - f(x0) * (x1 - x0) / (f(x1) - f(x0))
        print(f"{i+1}\t{round(x0,6)}\t{round(x1,6)}\t{round(x2,6)}\t{round(f(x2),6)}")
        if abs(f(x2)) < tol:
            print(f"\nRoot found: {x2} after {i+1} iterations")
            return x2
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
    print("\nMethod did not converge.")
    return None

x0 = 1
x1 = 2
regula_falsi(x0, x1)
