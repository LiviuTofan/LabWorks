import numpy as np

def evaluate_equations(num_eq, equations):
    def evaluate_f(x):
        f = np.zeros(num_eq)
        for i in range(num_eq):
            f[i] = eval(equations[i])
        return f

    def evaluate_jacobian(x):
        Jf = np.zeros((num_eq, num_eq))
        eps = 1e-6
        for i in range(num_eq):
            for j in range(num_eq):
                dx = np.zeros(num_eq)
                dx[j] = eps
                Jf[i, j] = (evaluate_f(x + dx)[i] - evaluate_f(x - dx)[i]) / (2 * eps)
        return Jf

    return evaluate_f, evaluate_jacobian


def solve_nonlinear_equations(evaluate_f, evaluate_jacobian, initial_guess, tol=1e-6, max_iter=100):
    x = np.array(initial_guess)
    for _ in range(max_iter):
        f = evaluate_f(x)
        Jf = evaluate_jacobian(x)
        dx = np.linalg.solve(Jf, -f)
        x = x + dx
        if np.linalg.norm(dx) < tol:
            return x
    raise ValueError("The Newton-Raphson method did not converge.")


num_eq = int(input("Enter the number of equations: "))
equations = []
initial_guess = []
for i in range(num_eq):
    equations.append(input(f"Enter equation {i+1}: "))
    initial_guess.append(float(input(f"Enter initial guess for x{i+1}: ")))
evaluate_f, evaluate_jacobian = evaluate_equations(num_eq, equations)
tol = float(input("Enter the tolerance: "))

roots = solve_nonlinear_equations(evaluate_f, evaluate_jacobian, initial_guess, tol=tol)
print("Roots found:", roots)


#Input example
# 2
# x[0]**2 + x[1]**2 - 1   |    0.5
# x[0] - x[1] - 0.5       |    0.5
# 1e-6