import numpy as np

coef = [np.array([[2, -1]]), np.array([[3, 2]]), np.array([[1, 1]]), np.array([[4, -1]]), np.array([[1, -3]])]
constants = [4, 7, 3, 1, -2]
sol = []

for i in range(5):
    sol.append(np.linalg.lstsq(coef[i], [constants[i]], rcond=None)[0])

# Convert the solutions list to a numpy array
sol = np.array(sol)
# Determine the correct order
order = np.lexsort(sol.T)

print("The correct order to step on the stones is:")
for i, stone in enumerate(order, start=1):
    print("Stone", i, ":", stone+1)
