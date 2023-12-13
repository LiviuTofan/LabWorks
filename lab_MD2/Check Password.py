password = input("Enter your password: ")

da = 0
nu = 0
parola = []
result1, result2, result3, result4 = 0, 0 ,0 ,0
mare, mica, numar, caracter = 0, 0, 0, 0
uppercase = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
lowercase = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
digits = ['0','1','2','3','4','5','6','7','8','9']
characters = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','[',']','\\',';',"'",'<','>','/','{','}','|',':','"',',','.','?','~']

for i in password:
    parola.append(i)

for i in parola:
    for j in uppercase:
        if i==j:
            result1 += 1
    for k in lowercase:
        if i==k:
            result2 += 1
    for z in digits:
        if i==z:
            result3 += 1
    for x in characters:
        if i==x:
            result4 += 1
if result1 == 0:
    mare += 1
if result2 == 0:
    mica += 1
if result3 == 0:
    numar += 1
if result4 == 0:
    caracter += 1

#cazurile cand lungimea>20
i=0
move = 0
while(i in range(0, len(parola) - 2)):#scot repetarile
    if len(parola) > 20:
        if parola[i] == parola[i + 1] == parola[i + 2]:
            parola = parola[:i] + parola[i+1:] # scap de i
            move += 1
            i -= 1
    i += 1
i = 0
while(len(parola) > 20):#scot elemente din lista pana o fac 20
    if result1 > 1:
        for i in range(len(parola)-1):
            if parola[i] in uppercase:
                parola.remove(parola[i])
                move += 1
                break
    elif result2 > 1:
        for i in range(len(parola)-1):
            if parola[i] in lowercase:
                parola.remove(parola[i])
                move += 1
                break
    elif result3 > 1:
        for i in range(len(parola)-1):
            if parola[i] in digits:
                parola.remove(parola[i])
                move += 1
                break
    elif result4 > 1:
        for i in range(len(parola)-1):
            if parola[i] in characters:
                parola.remove(parola[i])
                move += 1
                break
    i += 1

ele = caracter+numar+mica+mare #cate tipuri lipsesc
i=0
c=0

#caut repetarile
if len(password) >= 3:
    while i < len(parola)-2:
        if password[i] == password[i+1] and password[i] == password[i+2]:
            c += 1
            i += 3
        else:
            i+= 1

#cazurile pentru lungimea < 8
if len(password) < 8:
    print("For good password you have to do steps: ")
    nu = 8-len(password)
    if nu >= 3:
       print(nu+c)
    if nu == 2:
        if ele <= 2:
            if c == 0:
                print(2)
            elif c == 1:
                print(3)
        elif ele == 3:
            if c == 0 or c == 1:
                print(3)
            if c == 2:
                print(4)
    if nu == 1:
        if ele == 0 or ele == 1:
            print(c+1)
        elif ele == 2:
            if c == 0 or c == 1:
                print(2)
            elif c == 2:
                print(3)
        elif ele == 3:
            print(3)


#cazurile pentru care lungimea parolei este buna
if len(parola) >= 8 and len(parola) <= 20:
    if ele == 0 and c == 0 and move == 0:
        print("Entered password is good :)")
    else:
        print("For a good password, you have to do steps: ")

        if ele == 0 and move > 0:
            if c == 0:
                print(move)
        elif ele == 0 and c > 0:
            print(c + move)
        elif ele == 1:
            if c == 0:
                print(1 + move)
            else:
                print(c + move)
        elif ele == 2:
            if c >= 3:
                print(3 + move)
            else:
                print(2 + move)
        elif ele == 3:
            if c <= 3:
                print(3 + move)
            else:
                print(c + move)
