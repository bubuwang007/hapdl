import enum

class APDL_Commands(enum.Enum):

    @classmethod
    def is_apdl_command(cls, command: str) -> bool:
        return (
            command.strip().replace("*", "STAR").replace("/", "SLASH").upper()
            in cls.__members__
        )

    @staticmethod
    def get_command(command: "APDL_Commands") -> str:
        return command.name.replace("STAR", "*").replace("SLASH", "/")
