import nltk
import random

# CFG rules
rules = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N'], ['NP', 'PP']],
    'VP': [['V', 'NP'], ['VP', 'PP']],
    'PP': [['P', 'NP']],
}

# CFG terminals
terminals = {
    'Det': ['the', 'a'],
    'N': ['dog', 'cat', 'mouse'],
    'V': ['chased', 'saw', 'liked'],
    'P': ['in', 'on', 'by'],
}

# Function to generate a random sentence
def generate_sentence():
    sentence = []
    stack = ['S']

    while stack:
        symbol = stack.pop()

        if symbol in terminals:
            sentence.append(random.choice(terminals[symbol]))
        else:
            rule = random.choice(rules[symbol])
            stack.extend(rule[::-1])

    return ' '.join(sentence)

# Generate and print 10 random sentences
for _ in range(10):
    print(generate_sentence())
