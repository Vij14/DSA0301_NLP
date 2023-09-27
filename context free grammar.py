import nltk
from nltk import CFG

# Define a context-free grammar for English sentences
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'man' | 'park'
    V -> 'chased' | 'saw'
    P -> 'in' | 'on'
""")

# Create a parser using the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to parse
sentence = "I saw the dog in the park"

# Tokenize the sentence
tokens = sentence.split()

# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()
