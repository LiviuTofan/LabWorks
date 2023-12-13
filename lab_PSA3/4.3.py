import json
import nltk
from nltk import word_tokenize
from collections import defaultdict


with open('C:\\Users\\liviu\\Desktop\\lab_PSA3\\Data\\tweets.json', encoding='utf8') as f:
    data = json.load(f)
f.close()
text = ''
for textfield in data:
    text += (textfield['text'])

text = word_tokenize(text)
text = [word for word in text if word.isalpha() and word != 'https']
tags = nltk.pos_tag(text)
propernouns = [word for word,pos in tags if pos == 'NNP']
third = defaultdict(int)

for i in propernouns: third[i] += 1
third_arr = sorted(third, key=third.get, reverse=True)[:10]
print("Most common proper nouns are:")
for j in third_arr:
    print(j, propernouns.count(j))