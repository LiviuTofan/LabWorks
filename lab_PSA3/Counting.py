import random

tries = 10000
def seat():
    ans = 0
    total = 0
    for i in range(tries):
        seats = [0 for i in range(100)]
        seats[random.randint(0, 99)] = 1
        for i in range(1, 100):
            if seats[i] > 0:
                while True:
                    x = random.randint(0, 99)
                    if seats[x-1] == 0:
                        break
                seats[x-1] = i
            else:
                seats[i] = i + 1
        if seats[99] == 100:
            ans += 1
        total += 1
    p = (ans/total)*100
    return p

print('Probability is:',seat())