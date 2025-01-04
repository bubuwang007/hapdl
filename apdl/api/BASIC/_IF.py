from .._Commands import Commands

class IF:
    
    def __init__(self):
        self.state = None
        self.commands = Commands()

    def THEN(self, expr1, op, expr2, check=True):
        if self.state is not None:
            raise ValueError("THEN command must be after IF command.")
        if check:
            if op not in ['EQ', 'NE', 'LT', 'LE', 'GT', 'GE', 'ABGT', 'ABLT']:
                raise ValueError("Operator must be one of EQ, NE, LT, LE, GT, GE, ABGT, ABLT.")
        self.commands << f"*IF,{expr1},{op},{expr2},THEN"
        self.state = 'then'
        self.commands.indent_up()
        return self.commands

    def ELSEIF(self, expr1, op, expr2, check=True):
        if self.state != 'then':
            raise ValueError("ELSEIF must be after THEN.")
        if check:
            if op not in ['EQ', 'NE', 'LT', 'LE', 'GT', 'GE', 'ABGT', 'ABLT']:
                raise ValueError("Operator must be one of EQ, NE, LT, LE, GT, GE, ABGT, ABLT.")
        self.commands.indent_down()
        self.commands << f"*ELSEIF,{expr1},{op},{expr2}"
        self.commands.indent_up()
        self.state = 'then'
        return self.commands

    def ELSE(self):
        if self.state not in ['then', 'else']:
            raise ValueError("ELSE must be after THEN or ELSE command.")
        self.commands.indent_down()
        self.commands << "*ELSE"
        self.commands.indent_up()
        self.state = 'else'
        return self.commands

    def ENDIF(self):
        if self.state not in ['then', 'else']:
            raise ValueError("ENDIF must be after THEN or ELSE command.")
        self.commands.indent_down()
        self.commands << "*ENDIF"
        self.state = 'close'

    def GOTO(self, expr1, op, expr2, label:str, check=True):
        if check:
            if op not in ['EQ', 'NE', 'LT', 'LE', 'GT', 'GE', 'ABGT', 'ABLT']:
                raise ValueError("Operator must be one of EQ, NE, LT, LE, GT, GE, ABGT, ABLT.")

            if not label.startswith(':'):
                raise ValueError("Label must start with ':'.")

            if  len(label) > 8:
                raise ValueError("Label must be up to 8 characters.")

        self.commands << f"*IF,{expr1},{op},{expr2},{label}"
        self.state = 'close'
    
    def STOP(self, expr1, op, expr2, check=True):
        if check:
            if op not in ['EQ', 'NE', 'LT', 'LE', 'GT', 'GE', 'ABGT', 'ABLT']:
                raise ValueError("Operator must be one of EQ, NE, LT, LE, GT, GE, ABGT, ABLT.")
        self.commands << f"*IF,{expr1},{op},{expr2},STOP"
        self.state = 'close'

    def EXIT(self, expr1, op, expr2, check=True):
        if check:
            if op not in ['EQ', 'NE', 'LT', 'LE', 'GT', 'GE', 'ABGT', 'ABLT']:
                raise ValueError("Operator must be one of EQ, NE, LT, LE, GT, GE, ABGT, ABLT.")
        self.commands << f"*IF,{expr1},{op},{expr2},EXIT"
        self.state = 'close'

    def CYCLE(self, expr1, op, expr2, check=True):
        if check:
            if op not in ['EQ', 'NE', 'LT', 'LE', 'GT', 'GE', 'ABGT', 'ABLT']:
                raise ValueError("Operator must be one of EQ, NE, LT, LE, GT, GE, ABGT, ABLT.")
        self.commands << f"*IF,{expr1},{op},{expr2},CYCLE"
        self.state = 'close'

    def apdl(self):
        if self.state != 'close':
            raise ValueError("IF command must be closed.")
        return self.commands