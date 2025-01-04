from .._api import _api, Processor

class IGESIN(_api):
    '''Transfers IGES data from a file into ANSYS.
    
    Reads a file containing IGES data and transfers it into the ANSYS database.You can import multiple files into a single database, but you must use the same import option (set with the IOPTN command) for each file.
    '''
    processor = Processor.aux15

    @classmethod
    def _check(cls, command):
        raise NotImplementedError

    @staticmethod
    def import_file(filename: str, ext: str = ""):
        '''Transfers IGES data from a file into ANSYS.
        
        filename:
            The name of the file to import.

        ext:
            The extension of the file to import (eight-character maximum).
        '''
        return f"IGESIN,{filename},{ext}"