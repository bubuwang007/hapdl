from .._api import _api, Processor

class TITLE(_api):
    '''Defines a main title.'''
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
    def set_title(title: str, check=True) -> str:
        '''
        title:

        Input up to 72 alphanumeric characters. Parameter substitution may be forced within the title by enclosing the parameter name or parametric expression within percent (%) signs.
        '''
        if check:
            if len(title) > 72:
                raise ValueError("The length of the string for /TITLE is more than 72 characters.")
        return f"/TITLE,'{title}'"