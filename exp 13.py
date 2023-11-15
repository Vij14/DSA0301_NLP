import nltk
from nltk import CFG

# Define a context-free grammar
grammar_rules = """
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'man' | 'park'
    V -> 'chased' | 'saw'
    P -> 'in' | 'on'
"""

# Create a CFG object
grammar = CFG.fromstring(grammar_rules)

# Create a parser using the Earley parser from NLTK
parser = nltk.ChartParser(grammar)

# Function to generate a parse tree for a given sentence
def generate_parse_tree(sentence):
    words = sentence.split()
    try:
        trees = list(parser.parse(words))
        if len(trees) == 1:
            return trees[0]
        else:
            print("Ambiguous parsing. Multiple parse trees found.")
    except ValueError as e:
        print(f"Error parsing sentence: {e}")

# Example usage
sentence = "the cat chased the dog in the park"
parse_tree = generate_parse_tree(sentence)

# Display the parse tree
if parse_tree:
    parse_tree.pretty_print()
