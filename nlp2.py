import nltk
nltk.download('punkt')  # Download the necessary data for tokenization
nltk.download('averaged_perceptron_tagger')  # Download the necessary data for POS tagging

from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Input text
text = "NLTK is a leading platform for building Python programs to work with human language data."

# Tokenize the text
tokens = word_tokenize(text)

# Perform POS tagging
pos_tags = pos_tag(tokens)

# Print the POS tags
print(pos_tags)
