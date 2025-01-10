from .._api import _api, Processor

class GO(_api):
    '''Reactivates suppressed printout.'''
    processor = Processor.any

    @classmethod
    def _check(cls, command):
        raise NotImplementedError

    @classmethod
    def call(cls, *args) -> str:
        return f"/{cls.__name__},{','.join(args)}"

    @staticmethod
    def go():
        return f"/GO"
