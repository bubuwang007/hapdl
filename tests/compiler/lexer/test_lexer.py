import os
import unittest
from hapdl.compiler.lexer import Lexer

class TestLexer(unittest.TestCase):

    def test_is_potential_identifier_start(self):
        tests = {
            "a": True,
            "A": True,
            "_": True,
            "1": False,
            " ": False,
            "\n": False,
            "\t": False,
            "*": False,
            "(": False,
            ")": False,
            "[": False,
            "]": False,
            "{": False,
            "}": False,
            "黄": True,
            "$": False,
        }
        for k, v in tests.items():
            self.assertEqual(Lexer.is_potential_identifier_start(k), v)

    def test_is_potential_identifier(self):
        tests = {
            "a": True,
            "A": True,
            "_": True,
            "1": True,
            "2": True,
            "9": True,
            " ": False,
            "\n": False,
            "\t": False,
            "*": False,
            "(": False,
            ")": False,
            "[": False,
            "]": False,
            "{": False,
            "}": False,
            "黄": True,
            "$": False,
        }
        for k, v in tests.items():
            self.assertEqual(Lexer.is_potential_identifier(k), v)

    def test_comment(self):
        lexer = Lexer.from_string("# this is a comment\n")
        tok = next(lexer.token_get())
        self.assertEqual(tok.type.value, "comment")
        self.assertEqual(tok.value, "# this is a comment")

    def test_identifier(self):
        lexer = Lexer.from_string("_a b_ c1")
        tokenizer = lexer.token_get()
        tok = next(tokenizer)
        self.assertEqual(tok.type.value, "id")
        self.assertEqual(tok.value, "_a")
        tok = next(tokenizer)
        self.assertEqual(tok.type.value, "id")
        self.assertEqual(tok.value, "b_")
        tok = next(tokenizer)
        self.assertEqual(tok.type.value, "id")
        self.assertEqual(tok.value, "c1")

    def test_string(self):
        lexer = Lexer.from_string('"this is a string"')
        tok = next(lexer.token_get())
        self.assertEqual(tok.type.value, "str")
        self.assertEqual(tok.value, 'this is a string')

        lexer = Lexer.from_string(r'"this is a \tstring\n"')
        tok = next(lexer.token_get())
        self.assertEqual(tok.type.value, "str")
        self.assertEqual(tok.value, 'this is a \tstring\n')

    def test_symbol(self):
        lexer = Lexer.from_string("...;,:.{}()[]->=>=!=!+*-/@%**//&|^<><=>=>=<=<=")
        res = ['...', ';', ',', ':', '.', '{', '}', 
               '(', ')', '[', ']', '->', '=>', '=',
               '!=', '!', '+', '*', '-', '/', '@', 
               '%', '**', '//', '&', '|', '^', '<', 
               '>', '<=', '>=', '>=', '<=', '<=']
        tokenizer = lexer.token_get()
        for r in res:
            tok = next(tokenizer)
            self.assertEqual(tok.type.value, r)
            self.assertEqual(tok.value, r)

    def test_integer(self):
        lexer = Lexer.from_string("01234567890")
        tok = next(lexer.token_get())
        self.assertEqual(tok.type.value, "int")
        self.assertEqual(tok.value, "01234567890")

    def test_float(self):
        lexer = Lexer.from_string("0.1234567890")
        tok = next(lexer.token_get())
        self.assertEqual(tok.type.value, "float")
        self.assertEqual(tok.value, "0.1234567890")

        lexer = Lexer.from_string("1234567890.0")
        tok = next(lexer.token_get())
        self.assertEqual(tok.type.value, "float")
        self.assertEqual(tok.value, "1234567890.0")

        lexer = Lexer.from_string("1234567890.1234567890")
        tok = next(lexer.token_get())
        self.assertEqual(tok.type.value, "float")
        self.assertEqual(tok.value, "1234567890.1234567890")

    def test_scientific(self):
        test = ['1e10', '1e-10', '1E+10', '1E-10', '1.0e10', '1.0e-10', '1.0E10', '1.0e+10', '1.0E-10']
        for t in test:
            lexer = Lexer.from_string(t)
            tok = next(lexer.token_get())
            self.assertEqual(tok.type.value, "float")
            self.assertEqual(tok.value, t)

    def test_imaginary(self):
        lexer = Lexer.from_string("1j 1.0j 1e10j 1.0e10j")
        res = ['1j', '1.0j', '1e10j', '1.0e10j']
        tokenizer = lexer.token_get()
        for r in res:
            tok = next(tokenizer)
            self.assertEqual(tok.type.value, "image")
            self.assertEqual(tok.value, r)

    def test_keyword(self):
        lexer = Lexer.from_string("true false none let del break continue and or import from as enum struct trait impl func inline return if else elif while for in match raise try except finally extern global pub nonlocal const")
        res = ['true', 'false', 'none', 'let', 'del', 'break', 'continue', 'and', 'or', 'import', 'from', 'as', 'enum', 'struct', 'trait', 'impl', 'func', 'inline', 'return', 'if', 'else', 'elif', 'while', 'for', 'in', 'match', 'raise', 'try', 'except', 'finally', 'extern', 'global', 'pub', 'nonlocal', 'const']
        tokenizer = lexer.token_get()
        for r in res:
            tok = next(tokenizer)
            self.assertEqual(tok.value, r)

    def test_lexer(self):
        p = os.path.abspath('./test.hapdl')
        lexer = Lexer.from_file(p)
        count = 0
        f = open('res.tok', "w", encoding="u8")
        for tok in lexer.token_get():
            print(tok, file=f)
            count += 1
        f.close()


if __name__ == '__main__':
    unittest.main()
