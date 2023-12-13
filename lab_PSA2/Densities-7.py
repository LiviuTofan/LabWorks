import random

def aranjare():
    aranjarea = list(range(10))
    random.shuffle(aranjarea)
    return aranjarea

def probability():
    dinner = aranjare()
    lunch = aranjare()
    dinner.insert(0, dinner[len(dinner)-1])
    dinner.append(dinner[1])
    lunch.insert(0, lunch[len(lunch)-1])
    lunch.append(lunch[1])
    for i in range(1, len(dinner)-1):
        for j in range(1, len(lunch)-1):
            if dinner[i] == lunch[j]:
                if dinner[i-1] == lunch[j-1] or dinner[i+1] == lunch[j+1] or dinner[i+1] == lunch[j-1] or dinner[i-1] == lunch[j+1]:
                    return False
    return True

tries = 1000000
wins = 0
for z in range(tries):
    if probability():
        wins += 1

print("Probability is:")
print((wins/tries)*100,"%")