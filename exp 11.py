class SimpleParser:
    def __init__(self, input_string):
        self.tokens = iter(input_string.split())
        self.current_token = next(self.tokens, None)

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.current_token = next(self.tokens, None)
        else:
            raise SyntaxError(f"Expected {expected_token}, found {self.current_token}")

    def parse_E(self):
        self.parse_T()
        while self.current_token == '+':
            self.match('+')
            self.parse_T()

    def parse_T(self):
        self.parse_F()
        while self.current_token == '*':
            self.match('*')
            self.parse_F()

    def parse_F(self):
        if self.current_token == '(':
            self.match('(')
            self.parse_E()
            self.match(')')
        elif self.current_token.isidentifier():
            self.match(self.current_token)
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

    def parse(self):
        self.parse_E()
        if self.current_token is not None:
            raise SyntaxError(f"Unexpected token at the end: {self.current_token}")

# Example usage
input_string = "id + id * ( id )"
parser = SimpleParser(input_string)
try:
    parser.parse()
    print("Parsing successful!")
except SyntaxError as e:
    print(f"Syntax error: {e}")
