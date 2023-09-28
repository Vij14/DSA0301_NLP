import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')

def canonicalize_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Tokenize the text
    words = word_tokenize(text)

    # Initialize a stemmer (Porter Stemmer)
    stemmer = PorterStemmer()

    # Stem each word in the list
    canonical_words = [stemmer.stem(word) for word in words]

    # Join the stemmed words back into a canonicalized sentence
    canonical_text = ' '.join(canonical_words)

    return canonical_text

# Example usage
input_text = "The dog chases the cat"
canonicalized_text = canonicalize_text(input_text)
print("Input Text:")
print(input_text)
print("\nCanonicalized Text:")
print(canonicalized_text)


























