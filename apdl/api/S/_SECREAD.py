import enum
from .._api import _api, Processor

class Option(enum.Enum):
    '''Options for reading a custom section library or a user-defined section mesh into ANSYS.'''
    lib = "LIBRARY"
    mesh = "MESH"

class SECREAD(_api):
    '''Reads a custom section library or a user-defined section mesh into ANSYS.'''

    processor = Processor.prep7

    def read(fname, option: Option = Option.mesh):
        return f"SECREAD,{fname},,,{option.value}"