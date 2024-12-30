from ._Exception import NotaValidAPDLCommand
from ._Processor import Processor

class _api:
    processor = Processor.begin

    @classmethod
    def _check(cls, command: str) -> bool:
        return False

    @classmethod
    def _get_all_paras(cls, command: str) -> list:
        if not isinstance(command, str):
            raise ValueError("command must be a string")
        paras = command.upper().split(",")
        paras = [p.strip() for p in paras]
        while paras[-1] == "":
            paras.pop()
        return paras

    @classmethod
    def call(cls, *args) -> str:
        return f"{cls.__name__},{','.join(args)}"

    @classmethod
    def check(cls, command: str) -> str:
        b = cls._check(command)
        if b:
            return command
        else:
            raise NotaValidAPDLCommand(f"Invalid command: {command}")