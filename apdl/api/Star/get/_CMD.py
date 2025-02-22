from ._func import get_cmd

class CMD:
    '''The following items are valid for all commands except star (*) commands and non-graphics slash (/) commands.'''

    @staticmethod
    def status(par: str):
        '''Status of previous command: 0=found, 1=not found (unknown).'''
        return get_cmd(par, "STAT")

    @staticmethod
    def nargs(par: str):
        '''Number of arguments in the previous command.'''
        return get_cmd(par, "NARGS")

    @staticmethod
    def field(par: str, num: int):
        '''Numerical value of the Nth field on the previous command. Field 1 is the command name (not available)'''
        return get_cmd(par, "FIELD", num)