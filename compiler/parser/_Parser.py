from ..lexer import Lexer

class Parser:

    def __init__(self, lexer: Lexer):
        self.lexer = lexer

    def parse(self):
        toke_stream = self.lexer.token_get()

    def parse_module(self):
        pass
        
