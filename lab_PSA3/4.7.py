import json, os
from nltk import word_tokenize

while (True):

    cwd = os.getcwd()

    with open("C:\\Users\\liviu\\Desktop\\lab_PSA3\\Data\\tweets.json", "r", encoding='utf-8') as f:
        data = f.read()

    word = input("Introduce word: ")

    li = []
    user_dict = json.loads(data)
    for i in user_dict:
        li.append([x.lower() for x in word_tokenize(i["text"])])

    s = []
    for i in li:
        if f"{word}" in i:
            try:
                s.append(i[i.index(f"{word}") + 1])
            except:
                pass

    li3 = []
    for i in s:
        if i.isalnum() and i != "https":
            li3.append((s.count(i), i))

    li3 = sorted(set(li3))[::-1]

    print()
    nr = 0
    if len(li3) > 3:
        for i in range(3):
            y, x = li3[i]
            print(x, f"({y})")
    else:
        for i in range(len(li3)):
            y, x = li3[i]
            print(x, f"({y})")

    print()
    if word.lower() == "break":
        break