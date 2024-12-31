import os
import unittest
from hapdl.compiler.lexer import Lexer

class TestLexer(unittest.TestCase):

    def test_lexer(self):
        p = os.path.abspath('./test.hapdl')
        lexer = Lexer.from_file(p)
        count = 0
        for tok in lexer.token_get():
            print(tok)
            count += 1


if __name__ == '__main__':
    unittest.main()
