from .._api import _api, Processor

class ET(_api):
    '''Defines a local element type from the element library.'''
    processor = Processor.prep7

    @classmethod
    def _check(cls, command):
        raise NotImplementedError

    @staticmethod
    def et(id: int, ename: str):
        return f"ET,{id},{ename}"

    @staticmethod
    def et_complex(id: int, ename, *keyopts, noprint=False):
        if len(keyopts) > 6:
            raise ValueError("Too many keyopts")
        else:
            keyopts.extend([""] * (6 - len(keyopts)))
        return f"ET,{id},{ename},{','.join([str(i) for i in keyopts])},{1 if noprint else 0}"
