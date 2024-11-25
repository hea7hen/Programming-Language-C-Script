# CONSTANTS
DIGITS = '0123456789'
STRINGS = 'qwertyuiopasdfghjklzxcvbnm'

#TYPES
TYPE_INT = 'INT'
TYPE_STR = 'STR'
TYPE_FLOAT = 'FLOAT'
TYPE_PLUS = 'PLUS'
TYPE_MINUS = 'MINUS'
TYPE_MUL = 'MUL'
TYPE_DIV = 'DIV'
TYPE_LPAREN = 'LPAREN'
TYPE_RPAREN = 'RPAREN'

class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    
    def advance(self):    
        self.pos+=1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_token(self):
        token = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                token.append(self.make_num())

            elif self.current_char == '+':
                token.append(Token(TYPE_PLUS))
                self.advance()

            elif self.current_char == '-':
                token.append(Token(TYPE_MINUS))
                self.advance()

            elif self.current_char == '*':
                token.append(Token(TYPE_MUL))
                self.advance()

            elif self.current_char == '/':
                token.append(Token(TYPE_DIV))
                self.advance()

            elif self.current_char == '(':
                token.append(Token(TYPE_LPAREN))
                self.advance()

            elif self.current_char == ')':
                token.append(Token(TYPE_RPAREN))
                self.advance()
            
            else:
                cur  = self.current_char
                self.advance()
                return [], IllegalCharError("'"+cur+"'")
        
        return token, None


    def make_num(self):
        num = ''
        dot = 0

        while self.current_char  != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot == 1: break
                dot+=1
                num+='.'
            else:
                num+=self.current_char
            self.advance()
        if dot == 0:
            return Token(TYPE_INT, int(num))
        else:
            return Token(TYPE_FLOAT, float(num))

# RUN
def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_token()
    return tokens, error