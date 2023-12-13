import random

def probability():
    tries = 10000000
    triangle = 0
    for i in range(tries):
        point1 = random.random()
        point2 = random.random()
        if point1 > point2:
            temp = point1
            point1 = point2
            point2 = temp
        segment1 = point1
        segment2 = point2 - point1
        segment3 = 1 - point2
        if segment1 + segment2 > segment3 and segment1 + segment3 > segment2 and segment2 + segment3 > segment1:
            triangle += 1
    ptriangle = (triangle / tries) * 100
    return ptriangle

print("Probability is:")
print(probability(), "%")