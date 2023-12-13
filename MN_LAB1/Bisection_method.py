import math
import numpy as np

def f(x):
    return math.exp(x) - x**2

a, b = -2, 0
c = (a + b) / 2
err = 1e-8

while b - c >= err:
    if np.sign(f(a)) * np.sign(f(c)) < 0:
        b = c
    else:
        a = c
    c = (a + b) / 2

print("The root is:", c)
