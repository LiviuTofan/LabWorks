import json
from nltk import word_tokenize
import matplotlib.pyplot as plt
from collections import defaultdict

with open('C:\\Users\\liviu\\Desktop\\lab_PSA3\\Data\\tweets.json', encoding='utf8') as f:
    data = json.load(f)

text, d, secret_word = '', defaultdict(int), str(input("Write the word: "))

for textfield in data:
    sequence = word_tokenize(''.join(word.lower() for word in textfield['text']))
    if secret_word in sequence: d[textfield['created_at'][:7]] += sequence.count(secret_word)
plt.bar(d.keys(), d.values(), width=1)
plt.xlabel('Months'), plt.ylabel(f"Frequency of the word:   {secret_word}")
plt.show()