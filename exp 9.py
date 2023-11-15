import re

# Define a list of example sentences
sentences = [
    "The cat jumps over the fence.",
    "She quickly runs to catch the ball.",
    "A bird is singing in the tree."
]

# Define a set of regular expression patterns and their corresponding POS tags
patterns = [
    (r'\b(cat|dog|bird)\b', 'NOUN'),  # Words matching cat, dog, or bird are tagged as nouns
    (r'\b(jumps|runs|singing)\b', 'VERB')  # Words matching jumps, runs, or singing are tagged as verbs
]

# Function to perform rule-based tagging
def rule_based_pos_tag(text):
    tagged_text = text
    for pattern, pos_tag in patterns:
        tagged_text = re.sub(pattern, f'\\1 ({pos_tag})', tagged_text)
    return tagged_text

# Tag the sentences using the rule-based system
for sentence in sentences:
    tagged_sentence = rule_based_pos_tag(sentence)
    print(tagged_sentence)
