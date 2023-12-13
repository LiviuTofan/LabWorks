def g(x, c):
    return 2 * x - c * x ** 2

def dg_dx(x, c):
    return 2 - 2 * c * x

def newton_iteration(c, initial_guess, num_iterations):
    p = initial_guess
    for _ in range(num_iterations):
        p = g(p, c)
    return p

def calculate_limit(c, initial_guess):
    num_iterations = 100
    limit = 1 / c
    result = newton_iteration(c, initial_guess, num_iterations)
    return limit, result

# Test for different values of c
for i in range(1, 10):
    limit, result = calculate_limit(i, 0.1)
    print(f"Limit for c = {i}: {limit}")
    print(f"Result for c = {i}: {result}")
    print()