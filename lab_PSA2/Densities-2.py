import random

def probability():
    tries = 1000000
    triangle = 0
    for i in range(tries):
        point1 = random.uniform(0, 1)
        if (point1>0.5):
            point2 = random.uniform(0, point1)
            segment1 = point2
            segment2 = point1-point2
            segment3 = 1-point1
        else:
            point2 = random.uniform(point1, 1)
            segment1 = point1
            segment2 = point2-point1
            segment3 = 1-point2
        if segment1 + segment2 > segment3 and segment1 + segment3 > segment2 and segment2 + segment3 > segment1:
            triangle += 1
    ptriangle = (triangle/tries)*100
    return ptriangle

print("Probability is:")
print(probability(),"%")