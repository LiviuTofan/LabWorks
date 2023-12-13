import random

def probability():
    tries = 1000000
    cash = 0
    da = 0
    for i in range(tries):
        cash -= 0.25
        x = random.uniform(0,1)
        y = random.uniform(0, 1)
        if x >= 0.25 and x <= 0.75:
            if y >= 0.25 and y <= 0.75:
                cash += 1
                da += 1
    pda = (da/tries)*100
    return cash, pda

print(probability())