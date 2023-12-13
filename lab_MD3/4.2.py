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
    elena_emotions = emotions_doc.readlines()
    for i in elena_emotions:
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
        tweets[i['id']] = value


with open('emotions.txt', 'w') as f:
    for key, value in tweets.items():
        f.write('%s  %s\n' % (str(key), value))

