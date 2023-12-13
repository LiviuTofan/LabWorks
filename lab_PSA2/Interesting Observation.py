import random
import matplotlib.pyplot as plt

def probability():
    tries = 1000000
    ten = 0
    nine = 0
    x = 0
    nines = []
    tens = []
    xaxis = []
    for i in range(tries):
        x += 1
        xaxis.append(x)
        cub1 = random.randint(1, 6)
        cub2 = random.randint(1, 6)
        cub3 = random.randint(1, 6)
        sum = cub1+cub2+cub3
        if sum == 9:
            nines.append(1+nine)
            nine += 1
        else:
            nines.append(nine)
        if sum == 10:
            tens.append(1+ten)
            ten += 1
        else:
            tens.append(ten)
    return nines, tens, xaxis


nines, tens, xaxis = probability()
plt.plot(xaxis,nines, label="Occurance of 9")
plt.plot(xaxis,tens, label="Occurance of 10")
plt.legend()
plt.show()