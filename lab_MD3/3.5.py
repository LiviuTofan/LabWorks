x = "From T-Rex to Multi Universes: How the Internet has Changed Politics , Art and Cute Cats"
s = x.split()
ian = []
with open('C:\\Users\\liviu\\Desktop\\lab_MD3\\Data\\matrix.txt') as file:
    data = file.readline()
    while data != "":
        data = file.readline()
        for i in s:
            if i in data:
                ian.append(data[:-1])

    print(ian)