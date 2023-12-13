import random
import numpy


def random_point():
    grade = random.uniform(0, numpy.pi)
    r = random.uniform(0, 10)
    x = r * numpy.cos(grade)
    y = r * numpy.sin(grade)
    return [x, y, r]

def distance(a, b):
    return numpy.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

right = 0
less5 = 0
more5 = 0
inRange = 0
tries = 10000
for i in range(tries):
    point = random_point()
    if point[0] > 0:
        right += 1
    if point[2] < 5:
        less5 += 1
    else:
        more5 += 1
    if distance([point[0], point[1]], [0, 5]) < 5:
        inRange += 1

print('It lands in the right half of the target: ', right/tries)
print('Its distance from the center is less than 5 inches: ', less5/tries)
print('Its distance from the center is greater than 5 inches: ', more5/tries)
print('It lands within 5 inches of the point (0, 5): ', inRange/tries)