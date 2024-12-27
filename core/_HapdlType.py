from typing import Callable
from ._Frame import Frame
from ._NumberMethods import NumberMethods
from ._HapdlObject import HapdlObject


class HapdlType:

    type_name: str
    destructor: Callable[[Frame, HapdlObject], None] | None
    getattr_func: Callable[[Frame, HapdlObject, str], HapdlObject] | None
    setattr_func: Callable[[Frame, HapdlObject, str, HapdlObject], HapdlObject] | None
    number_methods: NumberMethods
    sequence_methods: None
    compare_methods: None

    def __init__(self, type_name: str) -> None:
        self.type_name = type_name

HAPDLTYPE = HapdlType("HapdlType")
HAPDLTYPE.destructor = None
HAPDLTYPE.getattr_func = None
HAPDLTYPE.setattr_func = None
HAPDLTYPE.number_methods = None