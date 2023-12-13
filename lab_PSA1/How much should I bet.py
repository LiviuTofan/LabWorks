import random

def game():
        t = 0
        coin = 0
        while coin < 0.5:
                coin = random.uniform(0, 1)
                t += 1
        return 2**t


sum = 0
tries = 100000
for i in range(tries):
        sum += game()
med = sum/tries
print(med)
