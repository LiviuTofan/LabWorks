import random
import math

def probability():
    tries = 1000000
    triangle = 0
    for i in range(tries):
        grad1 = random.uniform(0,math.pi*2)
        grad2 = random.uniform(0,math.pi*2)
        grad3 = random.uniform(0,math.pi*2)
        x1 = math.cos(grad1)
        y1 = math.sin(grad1)
        x2 = math.cos(grad2)
        y2 = math.sin(grad2)
        x3 = math.cos(grad3)
        y3 = math.sin(grad3)
        segment1 = math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
        segment2 = math.sqrt(pow((x2-x3),2)+pow((y2-y3),2))
        segment3 = math.sqrt(pow((x3-x1),2)+pow((y3-y1),2))
        if segment1>segment2 and segment1>segment3:
            if pow(segment2, 2) + pow(segment3, 2) > pow(segment1, 2):
                triangle += 1
        elif segment2>segment1 and segment2>segment3:
            if pow(segment3, 2) + pow(segment1, 2) > pow(segment2, 2):
                triangle += 1
        elif segment3>segment1 and segment3>segment2:
            if pow(segment1, 2) + pow(segment2, 2) > pow(segment3, 2):
                triangle += 1
    ptriangle = (triangle/tries)*100
    return ptriangle

print("Probability is:")
print(probability(),"%")