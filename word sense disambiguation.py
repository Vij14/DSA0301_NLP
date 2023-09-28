import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk

# Download WordNet data (if not already downloaded)
nltk.download('wordnet')

# Sample sentence with a polysemous word
sentence = "I saw a bat flying in the sky."

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Perform word sense disambiguation using the Lesk algorithm
for word in tokens:
    synset = lesk(tokens, word)
    if synset:
        print(f"Word: {word}")
        print(f"Synset: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print()
