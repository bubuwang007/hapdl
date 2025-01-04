from .._api import _api, Processor

class IOPTN(_api):
    '''Controls options relating to importing a model.'''
    processor = Processor.aux15

    @classmethod
    def _check(cls, command):
        raise NotImplementedError
    
    @staticmethod
    def stat():
        '''List overall status of import facilities, including current option values. VAL1 is ignored.'''
        return "IOPTN,STAT"

    @staticmethod
    def set_default():
        '''Set default values for all import options.'''
        return "IOPTN,DEFA"

    @staticmethod
    def auto_merge(flag: bool = True):
        '''Entity merge option.
        
        flag:
            True: Automatic merging is performed (default).
            False: No merging of entities.
        '''
        return f"IOPTN,MERG,{'YES' if flag else 'NO'}"

    @staticmethod
    def cteate_solid(flag: bool = True):
        '''Solid option.
        
        flag:
            True: Solid is created automatically (default).
            False: No solid created.
        '''
        return f"IOPTN,SOLID,{'YES' if flag else 'NO'}"

    @staticmethod
    def iges_stat():
        '''List status of IGES related options in the output window.'''
        return "IOPTN,IGES,STAT"

    @staticmethod
    def iges_smooth():
        '''Use more robust IGES revision 5.2 import function (default)'''
        return "IOPTN,IGES,SMOOTH"

    @staticmethod
    def set_default_tolerance():
        '''Use system defaults (default).'''
        return "IOPTN,GTOLER,DEFA"
    
    @staticmethod
    def set_file_tolerance():
        '''Use tolerance from the imported file.'''
        return f"IOPTN,GTOLER,FILE"
    
    @staticmethod
    def set_user_tolerance(tol: float):
        '''Set user-defined tolerance value.'''
        return f"IOPTN,GTOLER,{tol}"

    @staticmethod
    def del_small_area(flag: bool = True):
        '''Delete small area option.

        flag:
            True: Small areas are deleted (default).
            False: Small areas are retained.
        '''
        return f"IOPTN,SMALL,{'YES' if flag else 'NO'}"