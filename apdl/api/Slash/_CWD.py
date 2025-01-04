import os
from .._api import _api, Processor

class CWD(_api):
    '''Changes the current working directory.

    After issuing the /CWD command, all new files opened with no default directory specified (via the FILE, /COPY, or RESUME commands, for example) default to the new DIRPATH directory.
    '''
    processor = Processor.any

    @classmethod
    def call(cls, *args) -> str:
        return f"/{cls.__name__},{','.join(args)}"

    @classmethod
    def _check(cls, command: str) -> bool:
        paras = cls._get_all_paras(command)

        if len(paras) != 2:
            return False

        return True

    @staticmethod
    def set_cwd(path: str) -> str:
        '''
        path: The full path name of the new working directory.
        '''
        path = os.path.abspath(path)
        return f"/CWD,'{path}'"
