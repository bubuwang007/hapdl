from .._api import _api, Processor

class CLEAR(_api):
    '''
    The /CLEAR command resets the database to the conditions present at the beginning of the problem.
    The command is typically used between multiple analyses in the same run, or between passes of a multipass analysis (such as between substructure generation, use, and expansion passes).
    The command sets the import and Boolean options back to the default, deletes all items from the database, and sets memory values to zero for items derived from database information. (All files remain intact.) The command also resets the jobname to match the currently open session .LOG and .ERR files, returning the jobname to its original value or to the most recent value specified via /FILNAME with KEY = 1.
    Additional commands cannot be stacked (via the $ separator) on the same line as the /CLEAR command.
    Use caution when placing the /CLEAR command within branching constructs (for example, those using *DO or *IF commands), as the command deletes all parameters including the looping parameter for do-loops. (To preserve your iteration parameter, issue a PARSAV command prior to /CLEAR, then follow /CLEAR with a PARRES command.)
    '''
    processor = Processor.any

    @classmethod
    def call(cls, *args) -> str:
        return f"/{cls.__name__},{','.join(args)}"

    @classmethod
    def _check(cls, command: str) -> bool:
        paras = cls._get_all_paras(command)

        if len(paras) == 1:
            return True
        
        if len(paras) != 2:
            return False

        if paras[1] not in ["START", "NOSTART"]:
            return False

        return True

    @staticmethod
    def start() -> str:
        '''
        Reread start.ans file (default).
        '''
        return "/CLEAR,START"
    
    @staticmethod
    def nostart() -> str:
        '''
        Do not reread start.ans file.
        '''
        return "/CLEAR,NOSTART"