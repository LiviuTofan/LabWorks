import random
import math

def probability():
    tries = 1000000
    real = 0
    positive = 0
    for i in range(tries):
        b = random.uniform(-1,1)
        c = random.uniform(-1, 1)
        delta = pow(b,2) - (4*c)
        if delta > 0:
            real += 1
            x1 = (-b-math.sqrt(delta))/2
            x2 = (-b+math.sqrt(delta))/2
            if x1 >= 0 and x2 >= 0:
                positive +=1
    ppositive = (positive/tries)*100
    preal = (real/tries)*100
    return ppositive, preal

ppositive, preal = probability()
print("Probability that the roots of this equation are both real:")
print(preal,"%")
print("Probability that the roots of this equation are both positive:")
print(ppositive,"%")