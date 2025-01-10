from .._api import _api, Processor

class AUTO(_api):
    '''Resets the focus and distance specifications to "automatically calculated."'''
    processor = Processor.any

    @classmethod
    def _check(cls, command):
        raise NotImplementedError
    
    @classmethod
    def call(cls, *args) -> str:
        return f"/{cls.__name__},{','.join(args)}"
    
    @staticmethod
    def auto(window: int = 1):
        return f"/AUTO,{window}"
    