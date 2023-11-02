class PluralizationMachine:
    def __init__(self):
        self.transitions = {
            'singular': {'s': 'plural_s', 'x': 'plural_es'},
            'plural_s': {},
            'plural_es': {}
        }
        self.current_state = 'singular'

    def pluralize(self, word):
        for letter in word[::-1]:
            if letter in self.transitions[self.current_state]:
                self.current_state = self.transitions[self.current_state][letter]
            else:
                return word + 's'  # Default to adding 's' if no rule applies

        return word + 'es' if self.current_state == 'plural_es' else word + 's'

pluralizer = PluralizationMachine()

nouns = ["cat", "dog", "dish", "bus", "kiss", "fox"]

for noun in nouns:
    plural_form = pluralizer.pluralize(noun)
    print(f"{noun} -> {plural_form}")
