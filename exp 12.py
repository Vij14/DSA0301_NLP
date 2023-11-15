class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar

    def predict(self, state, chart):
        next_symbol = state.next_symbol
        if next_symbol in self.grammar:
            for rule in self.grammar[next_symbol]:
                chart[state.origin].append(State(rule, 0, state.origin))

    def scan(self, state, token, chart):
        next_symbol = state.next_symbol
        if next_symbol == token:
            chart[state.origin + 1].append(State(state.rule, state.dot + 1, state.origin))

    def complete(self, state, chart):
        for st in chart[state.origin]:
            next_symbol = st.next_symbol
            if next_symbol == state.rule[0] and st.dot < len(st.rule) and st not in chart[state.origin + 1]:
                chart[state.origin + 1].append(State(st.rule, st.dot + 1, st.origin))

    def parse(self, input_tokens):
        chart = {i: [] for i in range(len(input_tokens) + 1)}
        chart[0].append(State(('S', ['E']), 0, 0))

        for i in range(len(input_tokens) + 1):
            while True:
                for state in chart[i]:
                    (self.predict if not state.complete() and state.next_symbol in self.grammar
                     else self.scan if i < len(input_tokens) else self.complete)(state, chart)
                if all(s in chart[i] for s in chart[i]):
                    break

        return any(s.rule == ('S', ['E']) and s.complete() and s.origin == 0 for s in chart[len(input_tokens)])


class State:
    def __init__(self, rule, dot, origin):
        self.rule = rule
        self.dot = dot
        self.origin = origin

    def complete(self):
        return self.dot == len(self.rule[1])

    @property
    def next_symbol(self):
        return self.rule[1][self.dot] if self.dot < len(self.rule[1]) else None


# Example usage
grammar = {
    'S': [('E',)],
    'E': [('E', '+', 'T'), ('T',)],
    'T': [('T', '*', 'F'), ('F',)],
    'F': [('(', 'E', ')'), ('id',)],
}

input_tokens = ['id', '+', 'id', '*', '(', 'id', ')']

result = EarleyParser(grammar).parse(input_tokens)
print("Parsing successful!" if result else "Syntax error!")
