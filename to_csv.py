import os
from nltk import word_tokenize

data = []
with open('aol-data-1.txt', 'r') as file:
    for line in file:
        qry = line.split('\t')
        if len(qry) > 2:
            data.append(qry[1])

tokenized_data = map(lambda x: word_tokenize(x), data)
n = 5

n_grams = map(lambda tokens: list(ngrams(tokens, n)), tokenized_data)

