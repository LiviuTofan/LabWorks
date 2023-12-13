from prettytable import PrettyTable

x = PrettyTable()


def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


a = str(input())
parameters = {}
t = []
List = []
final = []
names = []

for i in a:
    if i.isalpha():
        parameters[i] = 5
for i in parameters.keys():
    names.append(i)
names.append(a)
x.field_names = names
a = a.replace("+", " or ").replace("*", " and ").replace("!", " not ")
t = list(list(product([0, 1], repeat=len(parameters.keys()))))

for i in range(0, len(parameters.keys())):
    for item in t:
        List.append(item[i])
    x.add_column("\u2588", List)
    List.clear()

for item in t:
    c = 0
    for key in parameters.keys():
        parameters[key] = item[c]
        c += 1
    final.append(eval(a, {}, parameters))

for i in range(0, len(final)):
    if final[i] == True:
        final[i] = 1
    elif final[i] == False:
        final[i] = 0

x.add_column("\u2588", final)

for i in range(0, len(parameters.keys()) + 1):
    x.field_names.remove("\u2588")
print(x)

#Input example: (!x + y) * z + (!z * y * k)