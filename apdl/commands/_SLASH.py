from ._APDLCommands import APDL_Commands

SLASHSTART = 0
class SLASH(APDL_Commands):
    pass

SLASHEND = SLASHSTART+len(SLASH.__members__)