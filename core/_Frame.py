import enum
from ._Scope import Scope

class FrameType(enum.Enum):
    FILE = 0
    CLASS = 1

class Frame:
    type: FrameType
    builtin_scope: Scope
    global_scope: Scope
    local_scope: Scope
