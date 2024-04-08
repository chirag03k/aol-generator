import pickle
import random
import sys

# Load the model from a file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def generate_text(model, starting_words, num_words=20):
    sentence = list(starting_words)

    for _ in range(num_words):
        next_options = model[tuple(sentence[-2:])]
        k = len(next_options)
        if k < 1:
            break
        chosen = random.randint(0, k-1)
        next_word = next_options.most_common()[chosen][0]
        sentence.append(next_word)

    return ' '.join(sentence)

print(generate_text(model, sys.argv[1].split(' ')))