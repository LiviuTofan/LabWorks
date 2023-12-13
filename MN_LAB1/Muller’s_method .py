import math

def muller_method(equation, x0, x1, x2, tolerance=1e-8, max_iterations=100):
    for iteration in range(max_iterations):
        h0 = x1 - x0
        h1 = x2 - x1
        delta0 = (equation(x1) - equation(x0)) / h0
        delta1 = (equation(x2) - equation(x1)) / h1
        a = (delta1 - delta0) / (h1 + h0)
        b = a * h1 + delta1
        c = equation(x2)
        discriminant = math.sqrt(b ** 2 - 4 * a * c)
        den_plus = b + discriminant
        den_minus = b - discriminant
        den = den_plus if abs(den_minus) < abs(den_plus) else den_minus
        dx = -2 * c / den
        x_new = x2 + dx
        if abs(dx) < tolerance:
            return x_new
        x0, x1, x2 = x1, x2, x_new
    raise Exception("Muller's method failed to converge")

def equation(x):
    return x ** 3 + 2 * x ** 2 + 10 * x - 20

x0 = 0
x1 = 1
x2 = 2
tolerance = 1e-8

root = muller_method(equation, x0, x1, x2, tolerance)

print("The root of the equation is:", f"{root:.8f}")