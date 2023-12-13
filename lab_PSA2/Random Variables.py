import random

def variables():
        x = random.uniform(0,1)
        y = 0
        c = 0
        while(y<x):
            y = random.uniform(0, 1)
            c += 1
        zarplata = c - 1
        return zarplata

tries = 10000
zarplata = 0
for i in range(tries):
    zarplata += variables()

print(zarplata/tries)