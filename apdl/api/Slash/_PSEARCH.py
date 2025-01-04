from .._api import _api, Processor

class PSEARCH(_api):
    '''
    Specifies the pathname of a directory for file searches when reading "unknown command" macro files. The search for the files is typically from the ANSYS directory, then from the user home directory, and then from the current working directory. This command allows the middle directory searched to be other than the user home directory.
    This command is valid only at the Begin Level.
    '''
    processor = Processor.begin

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
    def only_workdir() -> str:
        '''
        Search only the ANSYS and current working directories
        '''
        return "/PSEARCH,OFF"

    @staticmethod
    def set_search_path(str, check=True) -> str:
        '''
        Path name (64 characters maximum, and must include the final delimiter) of the middle directory to be searched. Defaults to the user home directory.
        '''
        if check:
            if len(str) > 64:
                raise ValueError("The length of the string for \PSEARCH is more than 64 characters.")
        return f"/PSEARCH,'{str}'"

    @staticmethod
    def list_search_path() -> str:
        '''
        List the current middle directory and show the ANSYS_MACROLIB setting.
        '''
        return "/PSEARCH,STAT"