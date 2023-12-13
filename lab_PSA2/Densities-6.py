import random
import matplotlib.pyplot as plt

def coin():
    tries = 100
    head = 0
    for i in range(tries):
        capika = random.randint(0,1) #Head is 1
        if capika == 1:
            head += 1
    return head

data = {}
for i in range(35, 66):
    data.update({i: 0})
tries = 1000
for i in range(tries):
    head = coin()
    if head >= 35 and head <= 65:
        data[head] += 1
x = list(data.keys())
y = list(data.values())
fig = plt.figure(figsize = (10, 5))
plt.bar(x, y)
plt.xlabel("Number of Heads")
plt.ylabel("Occurrence")
plt.title("Distribution of Heads")
plt.show()
