x = "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats"
s = x.split()
se = []
fin = []
li = []
tot = []
with open('C:\\Users\\liviu\\Desktop\\lab_MD3\\Data\\matrix.txt') as file:
    with open('C:\\Users\\liviu\\Desktop\\lab_MD3\\Data\\influence.txt') as f:
        data = file.readline()
        while data != "":
            data = file.readline()
            d = f.readline()
            if data != "":
                le = d.split(":")[1]
                li = data.split("|")
                se.append((li[1].replace(" ", "").count('1'), li[0], float(le[:-1])))

for i in se:
    fin.append((i[0] * i[2], i[1]))

with open('C:\\Users\\liviu\\Desktop\\lab_MD3\\Data\\people_interests.txt') as file:
    data = file.readline()
    while data != "":
        data = file.readline()[:-1]
        if data != "":
            counter = 0
            txt = data.split(":")
            interests = txt[1].split()
            for i in s:
                if i in interests:
                    counter += 1
            li.append((txt[0], counter))

for i in li[2:]:
    tot.append(tuple((float(i[1]) * float(fin[li.index(i) - 2][0]), i[0])))
tot.sort(reverse=True)

for i in tot:
    print(i[1], i[0])