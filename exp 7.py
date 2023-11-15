import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger') 
text = "The quick brown fox jumps over the lazy dog."
words = word_tokenize(text)
tags = pos_tag(words)
for word, tag in tags:
    print(f"{word}: {tag}")
