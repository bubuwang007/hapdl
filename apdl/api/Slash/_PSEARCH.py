from .._api import _api

class PSEARCH(_api):

    @classmethod
    def call(cls, *args) -> str:
        return f"/{cls.__name__},{','.join(args)}"

    @classmethod
    def _check(cls, command: str) -> bool:
        paras = cls._get_all_paras(command)

        
        
        if len(paras) != 2:
            return False

        if paras[1] not in ["ALL", "NONE"]:
            return False

        return True