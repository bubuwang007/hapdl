def group(*args):
    return "(" + "|".join(args) + ")"

def any(*args):
    return group(*args) + "*"

def some(*args):
    return group(*args) + "+"

def optional(*args):
    return group(*args) + "?"

BLANK = r"\s"
EVERY = r"(.*)"
BLANK_ANY = r"(\s*(.*?)\s*)"
NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"
NUMBER = r"([0-9]*)"
EXPONENT = r"[eE][-+]?[0-9](?:[0-9])*"
POINTFLOAT = group(r"[0-9](?:[0-9])*\.([0-9](?:[0-9])*)?", r"\.[0-9](?:[0-9])*")

# TODO