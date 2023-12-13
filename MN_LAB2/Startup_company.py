import matplotlib.pyplot as plt

def piecewise_linear_interp(x, y, x_interp):
    n = len(x)
    if x_interp <= x[0]:
        return y[0]
    if x_interp >= x[-1]:
        return y[-1]
    for i in range(1, n):
        if x_interp <= x[i]:
            t = (x_interp - x[i - 1]) / (x[i] - x[i - 1])
            y_interp = (1 - t) * y[i - 1] + t * y[i]
            return y_interp

x_data = []
y_data = []
x_interp = []
y_interp = []
days = 1

with open(r"dataset_2.txt") as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("Date"):
        continue
    date, visitors = line.strip().split(",")
    if visitors == 'Nan':
        visitors = piecewise_linear_interp(x_data, y_data, days - 1)
        x_interp.append(days)
        y_interp.append(int(visitors))
    x_data.append(days)
    y_data.append(int(visitors))
    days += 1

plt.plot(x_data, y_data, '-', label='Original data')
plt.plot(x_interp, y_interp, 'o', label='Interpolated data')
plt.legend()
plt.show()