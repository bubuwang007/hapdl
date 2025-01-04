from .._api import _api, Processor


class _Type:

    def __init__(self, tp):
        self.tp = tp

    def _check(self, paras):
        raise NotImplementedError

    def pick(self):
        return f"ASEL,{self.tp},P"

    def area_number(self, start, end='', step=''):
        '''Selects areas by number range.'''
        return f"ASEL,{self.tp},NUM,{start},{end},{step}"

    def loc_x(self, start, end=''):
        '''Selects areas by X location range.'''
        return f"ASEL,{self.tp},LOC,X,{start},{end}"

    def loc_y(self, start, end=''):
        '''Selects areas by Y location range.'''
        return f"ASEL,{self.tp},LOC,Y,{start},{end}"

    def loc_z(self, start, end=''):
        '''Selects areas by Z location range.'''
        return f"ASEL,{self.tp},LOC,Z,{start},{end}"

    def ext(self):
        '''Select areas on exterior of selected volumes.'''
        return f"ASEL,{self.tp},EXT"

    def hard_points(self, start, end='', step=''):
        '''Select areas by associated hard points.'''
        return f"ASEL,{self.tp},HPT,,{start},{end},{step}"

    def material(self, start, end='', step=''):
        '''Select areas by material number associated with the area.'''
        return f"ASEL,{self.tp},MAT,,{start},{end},{step}"

    def element_type(self, start, end='', step=''):
        '''Select areas by element type number associated with the area.'''
        return f"ASEL,{self.tp},TYPE,,{start},{end},{step}"    

    def real_constant(self, start, end='', step=''):
        '''Select areas by real constant number associated with the area.'''
        return f"ASEL,{self.tp},REAL,,{start},{end},{step}"
    
    def section(self, start, end='', step=''):
        '''Select areas by section number associated with the area.'''
        return f"ASEL,{self.tp},SECN,,{start},{end},{step}"

    def element_coordinate_system(self, start, end='', step=''):
        '''Select areas by element coordinate system number associated with the area.'''
        return f"ASEL,{self.tp},ESYS,,{start},{end},{step}"

    def acca(self, start, end='', step=''):
        '''Select areas by associated element coordinate system number.'''
        return f"ASEL,{self.tp},ACCA,,{start},{end},{step}"


class S(_Type):

    def __init__(self):
        super().__init__('S')

    def pick(self, kwsp: int = 0):
        return f"ASEL,{self.tp},P,,,,,{kwsp}"
    
    def area_number(self, start, end='', step='', kwsp: int = 0):
        '''Selects areas by number range.'''
        return f"ASEL,{self.tp},NUM,{start},{end},{step},{kwsp}"
    
    def loc_x(self, start, end='', kwsp: int = 0):
        '''Selects areas by X location range.'''
        return f"ASEL,{self.tp},LOC,X,{start},{end},,{kwsp}"
    
    def loc_y(self, start, end='', kwsp: int = 0):
        '''Selects areas by Y location range.'''
        return f"ASEL,{self.tp},LOC,Y,{start},{end},,{kwsp}"
    
    def loc_z(self, start, end='', kwsp: int = 0):
        '''Selects areas by Z location range.'''
        return f"ASEL,{self.tp},LOC,Z,{start},{end},,{kwsp}"
    
    def ext(self, kwsp: int = 0):
        '''Select areas on exterior of selected volumes.'''
        return f"ASEL,{self.tp},EXT,,,,,{kwsp}"
    
    def hard_points(self, start, end='', step='', kwsp: int = 0):
        '''Select areas by associated hard points.'''
        return f"ASEL,{self.tp},HPT,,{start},{end},{step},{kwsp}"
    
    def material(self, start, end='', step='', kwsp: int = 0):
        '''Select areas by material number associated with the area.'''
        return f"ASEL,{self.tp},MAT,,{start},{end},{step},{kwsp}"
    
    def element_type(self, start, end='', step='', kwsp: int = 0):
        '''Select areas by element type number associated with the area.'''
        return f"ASEL,{self.tp},TYPE,,{start},{end},{step},{kwsp}"
    
    def real_constant(self, start, end='', step='', kwsp: int = 0):
        '''Select areas by real constant number associated with the area.'''
        return f"ASEL,{self.tp},REAL,,{start},{end},{step},{kwsp}"
    
    def section(self, start, end='', step='', kwsp: int = 0):
        '''Select areas by section number associated with the area.'''
        return f"ASEL,{self.tp},SECN,,{start},{end},{step},{kwsp}"
    
    def element_coordinate_system(self, start, end='', step='', kwsp: int = 0):
        '''Select areas by element coordinate system number associated with the area.'''
        return f"ASEL,{self.tp},ESYS,,{start},{end},{step},{kwsp}"
    
    def acca(self, start, end='', step='', kwsp: int = 0):
        '''Select areas by associated element coordinate system number.'''
        return f"ASEL,{self.tp},ACCA,,{start},{end},{step},{kwsp}"


class ASEL(_api):
    '''Selects a subset of areas.'''
    processor = Processor.any

    S = S()
    R = _Type('R')
    A = _Type('A')
    U = _Type('U')

    @classmethod
    def _check(cls, command):
        raise NotImplementedError
    
    @staticmethod
    def all():
        '''Selects all areas.'''
        return "ASEL,ALL"

    @staticmethod
    def none():
        '''Unselect the full set.'''
        return "ASEL,NONE"
    
    @staticmethod
    def inve():
        '''Invert the current set (selected becomes unselected and vice versa).'''
        return "ASEL,INVE"
    
    @staticmethod
    def stat():
        '''Display the current select status.'''
        return "ASEL,STAT"