test = input()
substr = {}
for i in range(len(test) + 1):
    for j in range(len(test) + 1):
        if len(test[i:j]) > 0:
            substr.update({test[i:j]: 0})

for x in substr:
    for i in range(len(test) + 1):
        for j in range(len(test) + 1):
            if len(x) == len(test[i:j]) and x == test[i:j]:
                substr[x] += 1
    substr[x] -= 1

maxlen = 0
result = ""

for x in substr:
    if len(x) > maxlen and substr[x] != 0:
        maxlen = len(x)
        result = x

if (result == ""):
    print("The longest possible duplicated substring: ''")
else:
    print("The longest possible duplicated substring: ", result)

maxlen = 0
for x in substr:
    repeats = False
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j and x[i] == x[j]:
                repeats = True
    if not repeats and len(x) > maxlen:
        maxlen = len(x)
        result = x

print("The longest substring without repeating characters:", result, ", with length:", len(result))