from .._api import _api, Processor

class FILNAME(_api):
    '''Changes the Jobname for the analysis.'''
    processor = Processor.begin

    @classmethod
    def call(cls, *args) -> str:
        return f"/{cls.__name__},{','.join(args)}"
    
    @classmethod
    def _check(cls, command: str) -> bool:
        paras = cls._get_all_paras(command)

        if len(paras) != 3:
            return False

        return True

    @staticmethod
    def set_filename(filename: str, key: int = 0, check=True) -> str:
        '''
        filename:

        Name (32 characters maximum) to be used as the Jobname. 

        key:

        Specify whether to use the existing log, error, lock, page, and output files (.LOG, .ERR, .LOCK, .PAGE and .OUT) or start new files.

        0 - Continue using current log, error, lock, page, and output files.

        1 - Start new log, error, lock, page, and output files (old log and error files are closed and saved, but old lock, page, and output files are deleted). Existing log and error files are appended.

        '''
        if check:
            if len(filename) > 32:
                raise ValueError("The length of the string for /FILNAME is more than 32 characters.")

            if key not in [0, 1]:
                raise ValueError("The key for /FILNAME is not 0 or 1.")

        return f"/FILNAME,'{filename}',{key}"