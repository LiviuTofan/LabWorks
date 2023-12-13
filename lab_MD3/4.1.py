import json
import nltk

hashtag = {}
tt = nltk.TweetTokenizer()
with open('C:\\Users\liviu\\Desktop\\lab_MD3\\Data\\tweets.json', 'r', encoding='utf-8') as json_tweets:
    data = json.load(json_tweets)
    for i in data:
        text = tt.tokenize(i['text'])
        for j in text:
            if j[0] == '#' and len(j) > 1:
                if j not in hashtag.keys():
                    hashtag[j] = 1
                else:
                    hashtag[j] += 1

hashtag = dict(sorted(hashtag.items(), key=lambda item: item[1], reverse=True))

nr = 1
for i in hashtag:
    print(str(nr) + ". ", i, ' ', hashtag[i])
    nr += 1
    if nr > 10:
        break
