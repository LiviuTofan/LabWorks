
number_of_flights = int(input('number of flights: '))
start = int(input('start: '))
destination = int(input('destination: '))
k = int(input('k:'))
flights = [[0]*3]*number_of_flights


def cheapest_route(fl, st, dest, k):
    if st == dest:
        return 0
    if k < 0:
        return float('inf')
    cost = float('inf')

    for i in fl:
        if i[0] == st:
            new_cost = i[2] + cheapest_route(fl, i[1], dest, k-1)
            cost = min(cost, new_cost)
    if cost == float('inf'):
        return 'no route'
    else:
        return cost


for q in range(number_of_flights):
    flights[q] = [int(x) for x in input().split()]
ans = cheapest_route(flights, start, destination, k)

print(ans)

'''Example of input:
number_of_flights = 5
start = 0
destination = 2
k = 1
flights = [
    [0, 1, 100],
    [1, 2, 200],
    [0, 2, 500],
    [2, 3, 300],
    [1, 3, 150]
'''

