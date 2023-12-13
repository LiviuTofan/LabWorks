import json, os, nltk
from nltk import TweetTokenizer

tt = TweetTokenizer()
while (True):
    cwd = os.getcwd()
    # citim json file
    with open("C:\\Users\\liviu\\Desktop\\lab_PSA3\\Data\\tweets.json", "r", encoding='utf-8') as f:
        data = f.read()

    word = input("Introduce word: ")

    if word.lower() == "break":
        break

    li = [];
    lis = []
    user_dict = json.loads(data)
    for i in user_dict:
        if i["id"] not in lis:
            lis.append(i["id"])
            li.append([x.lower() for x in tt.tokenize(i["text"]) if x.isalnum() if "#" not in x])

    s = []
    for i in li:
        for j in i:
            if word in j:
                fodder = 0
                for z in range(len(word)):
                    if word[z] == j[z]:
                        fodder += 1
                if fodder == len(word):
                    s.append(j)

    # we remove all caracters that are not words and isn't https, and apend to a touple
    li3 = []
    for i in s:
        if i.isalnum() and i not in [word, "https"]:
            li3.append((s.count(i), i))

    li3 = sorted(set(li3))[::-1]

    print()
    nr = 0
    for i in range(3):
        try:
            y, x = li3[i]
            print(x, f"({y})")
        except:
            pass

    print()