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
text = [word.lower() for word in text if word.isalpha() and word != 'https']

tags = nltk.pos_tag(text)
nouns = [word for word,pos in tags if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS') and word != 'i' and word != 'kind']
second = defaultdict(int)
for i in nouns: second[i] += 1
second_arr = sorted(second, key=second.get, reverse=True)[:10]
print("Most common nouns are:")
for j in second_arr:
    print(j, nouns.count(j))