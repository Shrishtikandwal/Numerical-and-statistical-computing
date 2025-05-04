 def f(x):
    return x**3 - x - 2

def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Invalid interval.")
        return None
    print("Iter\ta\t\tb\t\tc\t\tf(c)")
    for i in range(max_iter):
        c = (a + b) / 2
        print(f"{i+1}\t{round(a,6)}\t{round(b,6)}\t{round(c,6)}\t{round(f(c),6)}")
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            print(f"\nRoot found: {c} after {i+1} iterations")
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("\nMethod did not converge.")
    return None

a = 1
b = 2
bisection(a, b)
