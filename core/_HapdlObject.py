import typing
from ._Frame import Frame
if typing.TYPE_CHECKING:
    from ._HapdlType import HapdlType

class HapdlObject:
    name: str
    type: HapdlType
    frame: Frame

    def __init__(self, name: str, type: HapdlType, frame: Frame = None) -> None:
        self.name = name
        self.type = type
        self.frame = frame

    def __str__(self) -> str:
        return f"{self.name} ({self.type})"