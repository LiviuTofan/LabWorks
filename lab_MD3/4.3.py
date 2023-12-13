import json
import nltk

tweets, emotions = {}, {}
tt = nltk.TweetTokenizer()


def count(text):
    value = 0
    for k in text:
        if k.lower() in emotions.keys():
            value += emotions[k.lower()]
    return value


with open('C:\\Users\\liviu\\Desktop\\lab_MD3\\Data\\AFINN-111.txt', 'r', encoding='utf-8') as emotions_doc:
    emot = emotions_doc.readlines()
    for i in emot:
        word = nltk.word_tokenize(i)
        st = ''
        for j in range(len(word)-1):
            st += word[j] + ' '
        emotions[st[:-1]] = int(word[-1])

with open('C:\\Users\\liviu\\Desktop\\lab_MD3\\Data\\tweets.json', 'r', encoding='utf-8') as json_tweets:
    data = json.load(json_tweets)
    for i in data:
        text = tt.tokenize(i['text'])
        value = count(text)
        tweets[i['text']] = value


tweets = dict(sorted(tweets.items(), key=lambda item: item[1], reverse=True))

print('10 positive tweets:')
nr = 1
for i in tweets:
    print(str(nr) + ". ", i, ' ', tweets[i])
    nr += 1
    if nr > 10:
        break


tweets = dict(sorted(tweets.items(), key=lambda item: item[1]))

print('\n10 negative tweets:')
nr = 1
for i in tweets:
    print(str(nr) + ". ", i, ' ', tweets[i])
    nr += 1
    if nr > 10:
        break