import json
from nltk import word_tokenize
from collections import defaultdict


with open('C:\\Users\\liviu\\Desktop\\lab_PSA3\\Data\\tweets.json', encoding='utf8') as f:
    data = json.load(f)
f.close()
text = ''
for textfield in data:
    text += (textfield['text'])
text = word_tokenize(text)
text = [word.lower() for word in text if word.isalpha() and word != 'https']



first = defaultdict(int)
for i in text:
    first[i] += 1
first_arr = sorted(first, key=first.get, reverse=True)[:10]
print("Most common 10 words are: ")
for j in first_arr:
    print(j, text.count(j))