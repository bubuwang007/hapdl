from .._api import _api, Processor

class AADD(_api):
    processor = Processor.prep7

    @classmethod
    def _check(cls, command: str) -> bool:
        paras = cls._get_all_paras(command)

        if len(paras) == 0:
            return False

        if paras[0] != "AADD":
            return False
        
        if paras[1]=='P' or paras[1]=='ALL':
            return True

        if len(paras) > 10 or len(paras) < 3:
            return False

        return True
    
    @classmethod
    def by_pick(cls) -> str:
        '''
        If P1 = P, graphical picking is enabled and all remaining arguments are ignored (valid only in the GUI).
        '''
        return "AADD,P"
    
    @classmethod
    def by_all(cls) -> str:
        '''
        If P1 = ALL, all keypoints are selected.
        '''
        return "AADD,ALL"
    
    @classmethod
    def by_areas(cls, *areas) -> str:
        '''
        The areas must be coplanar. The original areas (and their corresponding lines and keypoints) will be deleted by default.See the BOPTN command for the options available to Boolean operations. Element attributes and solid model boundary conditions assigned to the original entities will not be transferred to the new entities generated. Concatenated entities are not valid with this command.
        '''
        if len(areas) < 2 :
            raise ValueError("At least 2 area is required")
        elif len(areas) > 9:
            raise ValueError("At most 9 areas are allowed")
        return f"AADD,{','.join(map(str, areas))}"