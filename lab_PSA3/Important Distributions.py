import random

deer = (50/8)*200
print('The estimated number of deer is:',deer)

pdeer = 1/25
c = 0
tries = 1000

for i in range(tries):
    x = 0
    while x < 50:
        c += 1
        if random.uniform(0, 1) <= pdeer:
            x += 1
print('Number of deer by simulation:', c/tries)