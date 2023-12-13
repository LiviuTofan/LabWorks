import random
import matplotlib.pyplot as plt


def roulletered(tries):
    casino = ['R', 'B', 'G']
    money = 0
    for i in range(tries):
        money -= 20
        spin = random.choices(casino, weights=(18, 18, 2), k=1)
        if spin == ['R']:
            money += 40
        x.append(i)
        y.append(money)
    plt.plot(x, y)
    plt.savefig("red.jpg")


def stavka18(tries):
    money = 0
    for i in range(tries):
        money -= 1
        spin = random.randint(1, 38)
        if spin == 18:
            money += 1 + 35
        m.append(i)
        n.append(money)
    plt.plot(m, n)
    plt.savefig("stavka18.jpg")


m = []
n = []
x = []
y = []
roulletered(500)
stavka18(500)