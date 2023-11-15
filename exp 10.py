# Define a list of example sentences
import re
sentences = [
    "The cat jumps over the fence.",
    "She quickly runs to catch the ball.",
    "A bird is singing in the tree."
]

# Define a set of transformation rules to tag words
transformation_rules = [
    (r'\b(cat|dog|bird)\b', 'NOUN'),  # Words matching cat, dog, or bird are tagged as nouns
    (r'\b(jumps|runs|singing)\b', 'VERB'),  # Words matching jumps, runs, or singing are tagged as verbs
    (r'\b(quickly)\b', 'ADV'),  # Words matching quickly are tagged as adverbs
    (r'\b(\w+ly)\b', 'ADV'),  # Words ending in "ly" are tagged as adverbs
    (r'\b(\w+ing)\b', 'VERB'),  # Words ending in "ing" are tagged as verbs
    (r'\b(\w+ed)\b', 'VERB'),  # Words ending in "ed" are tagged as verbs
]

# Function to perform transformation-based tagging
def transform_based_pos_tag(text):
    tagged_text = text
    for pattern, pos_tag in transformation_rules:
        tagged_text = re.sub(pattern, f'\\1 ({pos_tag})', tagged_text)
    return tagged_text

# Tag the sentences using the transformation-based system
for sentence in sentences:
    tagged_sentence = transform_based_pos_tag(sentence)
    print(tagged_sentence)
