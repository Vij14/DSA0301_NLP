import random
corpus = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "."]
transition_matrix = {
    'DET': {'NOUN': 0.6, 'ADJ': 0.4},
    'NOUN': {'VERB': 0.7, 'ADJ': 0.2, 'DET': 0.1},
    'VERB': {'DET': 0.6, 'NOUN': 0.4},
    'ADJ': {'NOUN': 0.8, 'VERB': 0.2},
    '.': {'NOUN': 0.4, 'VERB': 0.4, 'ADJ': 0.2}
}
tagged_words = []
prev_tag = 'START'
for word in corpus:
    if word == ".":
            prev_tag = 'START' 
    possible_tags = list(transition_matrix.get(prev_tag, {}).keys())

    if not possible_tags:
        current_tag = random.choice(list(transition_matrix.keys()))
    else:
        current_tag = random.choices(possible_tags, [transition_matrix[prev_tag][tag] for tag in possible_tags])[0]
    tagged_words.append((word, current_tag))
    prev_tag = current_tag
for word, tag in tagged_words:
    print(f"{word} ({tag})")
