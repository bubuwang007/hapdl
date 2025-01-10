from ._E import EEND
from ._APDLCommands import APDL_Commands

FSTART = EEND + 1

class F(APDL_Commands):
    pass

EEND = FSTART + len(F.__members__) - 1