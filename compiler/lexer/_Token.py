import enum

class TokenType(enum.Enum):
    ONECHAR: dict
    TWOCHAR: dict
    THREECHAR: dict

    NUMBER = 'num'
    STRING = 'str'
    KEYWORD = 'keyword'
    IDENTIFIER = 'id'
    COMMENT = 'comment'
    # NEWLINE = 'newline'

    ELLIPSIS = '...'
    SEMICOLON = ';'
    COMMA = ','
    COLON = ':'
    DOT = '.'
    LBRACE = '{'
    RBRACE = '}'
    LPAR = '('
    RPAR = ')'
    LSQB = '['
    RSQB = ']'
    MINUSARROW = '->'
    EQARROW = '=>'

    EQ = '='
    NE = '!='
    NOT = '!'

    PLUS = '+'
    MINUS = '-'
    STAR = '*'
    SLASH = '/'
    AT = '@'
    PERCENT = '%'
    DOUBLESTAR = '**'
    DOUBLESLASH = '//'
    AMPER = '&'
    VBAR = '|'
    CIRCUMFLEX = '^'

    PLUSEQ = '+='
    MINUSEQ = '-='
    STAREQ = '*='
    SLASHEQ = '/='
    ATEQ = '@='
    PERCENTEQ = '%='
    DOUBLESTAREQ = '**='
    DOUBLESLASHEQ = '//='
    AMPEREQ = '&='
    VBAREQ = '|='
    CIRCUMFLEXEQ = '^='

    LT = '<'
    GT = '>'
    LE = '<='
    GE = '>='

    def __str__(self) -> str:
        return "Token." + self.name

    @classmethod
    def get_three_char_symbol(cls, c1, c2, c3):
        try:
            return cls.THREECHAR.get(c1).get(c2).get(c3)
        except:
            return None
        
    @classmethod
    def get_two_char_symbol(cls, c1, c2):
        try:
            return cls.TWOCHAR.get(c1).get(c2)
        except:
            return None
        
    @classmethod
    def get_one_char_symbol(cls, c):
        try:
            return cls.ONECHAR.get(c)
        except:
            return None


TokenType.ONECHAR = {
    ';': TokenType.SEMICOLON,
    ',': TokenType.COMMA,
    ':': TokenType.COLON,
    '.': TokenType.DOT,
    '{': TokenType.LBRACE,
    '}': TokenType.RBRACE,
    '(': TokenType.LPAR,
    ')': TokenType.RPAR,
    '[': TokenType.LSQB,
    ']': TokenType.RSQB,
    '=': TokenType.EQ,
    '!': TokenType.NOT,
    '+': TokenType.PLUS,
    '-': TokenType.MINUS,
    '*': TokenType.STAR,
    '/': TokenType.SLASH,
    '@': TokenType.AT,
    '%': TokenType.PERCENT,
    '&': TokenType.AMPER,
    '|': TokenType.VBAR,
    '^': TokenType.CIRCUMFLEX,
    '<': TokenType.LT,
    '>': TokenType.GT,
}

TokenType.TWOCHAR = {
    '!': {'=': TokenType.NE},
    '-': {'>': TokenType.MINUSARROW},
    '=': {'>': TokenType.EQARROW},
    '+': {'=': TokenType.PLUSEQ},
    '-': {'=': TokenType.MINUSEQ},
    '*': {'=': TokenType.STAREQ,
          '*': TokenType.DOUBLESTAR},
    '/': {'=': TokenType.SLASHEQ},
    '@': {'=': TokenType.ATEQ},
    '%': {'=': TokenType.PERCENTEQ},
    '/': {'/': TokenType.DOUBLESLASH},
    '&': {'=': TokenType.AMPEREQ},
    '|': {'=': TokenType.VBAREQ},
    '^': {'=': TokenType.CIRCUMFLEXEQ},
    '<': {'=': TokenType.LE},
    '>': {'=': TokenType.GE},
}

TokenType.THREECHAR = {
    '*': {'*': {'=': TokenType.DOUBLESTAREQ}},
    '/': {'/': {'=': TokenType.DOUBLESLASHEQ}},
}
    