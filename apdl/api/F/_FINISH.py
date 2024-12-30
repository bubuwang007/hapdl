from .._api import _api

class FINISH(_api):

    @classmethod
    def _check(cls, command: str) -> bool:
        paras = cls._get_all_paras(command)

        if len(paras) > 1:
            return False

        return True

    @classmethod
    def finish(cls) -> str:
        '''
        Exits normally from a processor.
        '''
        return "FINISH"