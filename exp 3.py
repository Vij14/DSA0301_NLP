import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
words = ["running", "flies", "better", "jumps"]
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stemmed_words = [stemmer.stem(word) for word in words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("Original words:", words)
print("Porter Stemmer:", stemmed_words)
print("WordNet Lemmatizer:", lemmatized_words)
