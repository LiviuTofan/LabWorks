#mesajul = input()

p = 61
q = 67
n = p*q
fi = (p-1)*(q-1)

def gcd(e,fi):
    if fi == 0:
        return e
    else:
        return gcd(fi,e%fi)

def findE():
    for e in range(2,fi):
        if gcd(e,fi) == 1:
            return e
    return False
e = findE()

def findD():
    for d in range(fi):
        if (d*e)%fi == 1:
            return d
    return 0
d = findD()

letters = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G",
    17: "H",
    18: "I",
    19: "J",
    20: "K",
    21: "L",
    22: "M",
    23: "N",
    24: "O",
    25: "P",
    26: "Q",
    27: "R",
    28: "S",
    29: "T",
    30: "U",
    31: "V",
    32: "W",
    33: "X",
    34: "Y",
    35: "Z",
    36: " "
}

mesajul = input()
lista = []
newlist = []
encryption = []
lista2 = []
newlist2 = []

print("Public Key = {",e,n,"}")
print("Private Key = {",d,n,"}")

    #transform literele in numere
for i in mesajul:
    lista.append(list(letters.keys())[list(letters.values()).index(i)]) #adauga in lista cheia valorii

    #lipesc numerele sa fie cate 4
for i in range(0,len(lista)-1):
    if (i+2)%2 == 0:
        newlist.append(lista[i]*100+lista[i+1])
if len(mesajul)%2 != 0:
    newlist.append(lista[len(lista)-1])
    #incriptez
print("Encrypted Message:")
for i in range(len(newlist)):
    encryption.append(pow(newlist[i],e,n))
[print(i, end=' ') for i in encryption] #scot elementele din lista
print(end='\n')

    #decriptez
for i in encryption:
    lista2.append(pow(i, d, n))
for i in lista2:
        newlist2.append(i//100)
        newlist2.append(i%100)
if len(mesajul)%2 != 0:
    newlist2.remove(newlist2[len(newlist2)-2])
print("Decrypted Message:")
for i in newlist2:
    print(letters[i], end = '')