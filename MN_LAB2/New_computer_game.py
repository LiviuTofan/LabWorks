import numpy as np
import math

roots_weights = {
    1: (np.array([0]), np.array([2])),
    2: (np.array([-1/math.sqrt(3), 1/math.sqrt(3)]), np.array([1, 1])),
    3: (np.array([-math.sqrt(3/5), 0, math.sqrt(3/5)]), np.array([5/9, 8/9, 5/9])),
    4: (np.array([-math.sqrt((3/7)-2/7*math.sqrt(6/5)), math.sqrt((3/7)-2/7*math.sqrt(6/5)), -math.sqrt((3/7)+2/7*math.sqrt(6/5)), math.sqrt((3/7)+2/7*math.sqrt(6/5))]), np.array([(18+math.sqrt(30))/36, (18+math.sqrt(30))/36, (18-math.sqrt(30))/36, (18-math.sqrt(30))/36])),
}

def integrate(func, a, b, order=2):
    if order < 1 or order > 4:
        raise ValueError("Order must be between 1 and 4")

    roots, weights = roots_weights[order]

    shifted_roots = a + ((roots + 1) / 2) * (b - a)

    # approximation value of integral
    return ((b - a) / 2) * np.sum(weights * np.vectorize(func)(shifted_roots))

def main():
    equation = input("Enter the equation of motion (use 'x' as the variable): ")
    a = float(eval(input("Enter the start of the integration range: ")))
    b = float(eval(input("Enter the end of the integration range: ")))
    tolerance = float(eval(input("Enter the desired tolerance: ")))

    func = lambda x: eval(equation)

    prev_approx = integrate(func, a, b, order=1)
    for order in range(2, 5):
        cur_approx = integrate(func, a, b, order=order)
        if abs(cur_approx - prev_approx) < tolerance:
            print(cur_approx)
            return
        prev_approx = cur_approx

    print("Failed to reach the desired tolerance")

main()

# input example:
# math.exp(-x**2)    or    2*x**2 + 3*x - 4
# -1 | 1 | 1e-2      or    -5 | 5 | 1e-5