from .._api import _api, Processor

class _Type:
    # items = {
    #     'LINE': [''], # Line number.
    #     'EXT': [''], # Line numbers on exterior of selected area (ignore remaining fields).
    #     'LOC': ['X', 'Y', 'Z'], # X, Y, or Z center location in the active coordinate system.
    # }

    def __init__(self, tp):
        self.tp = tp

    def _check(self, paras):
        raise NotImplementedError

    def pick(self):
        return f"LSEL,{self.tp},P"

    def line_number(self, start, end='', step=''):
        '''Select lines by line number range.'''
        return f"LSEL,{self.tp},LINE,,{start},{end},{step}"

    def loc_x(self, start, end=''):
        '''Select lines by X location range.'''
        return f"LSEL,{self.tp},LOC,X,{start},{end}"

    def loc_y(self, start, end=''):
        '''Select lines by Y location range.'''
        return f"LSEL,{self.tp},LOC,Y,{start},{end}"

    def loc_z(self, start, end=''):
        '''Select lines by Z location range.'''
        return f"LSEL,{self.tp},LOC,Z,{start},{end}"

    def ext(self):
        '''Select lines on exterior of selected area.'''
        return f"LSEL,{self.tp},EXT"

    def tangent_x_at_beginning(self, start, end=''):
        '''Select lines by unit vector component of outward tangent at beginning of line.

        start or end: -1~1
        '''
        return f"LSEL,{self.tp},TAN1,X,{start},{end}"

    def tangent_y_at_beginning(self, start, end=''):
        '''Select lines by unit vector component of outward tangent at beginning of line.

        start or end: -1~1
        '''
        return f"LSEL,{self.tp},TAN1,Y,{start},{end}"

    def tangent_z_at_beginning(self, start, end=''):
        '''Select lines by unit vector component of outward tangent at beginning of line.

        start or end: -1~1
        '''
        return f"LSEL,{self.tp},TAN1,Z,{start},{end}"

    def tangent_x_at_end(self, start, end=''):
        '''Select lines by unit vector component of outward tangent at end of line.

        start or end: -1~1
        '''
        return f"LSEL,{self.tp},TAN2,X,{start},{end}"

    def tangent_y_at_end(self, start, end=''):
        '''Select lines by unit vector component of outward tangent at end of line.

        start or end: -1~1
        '''
        return f"LSEL,{self.tp},TAN2,Y,{start},{end}"

    def tangent_z_at_end(self, start, end=''):
        '''Select lines by unit vector component of outward tangent at end of line.

        start or end: -1~1
        '''
        return f"LSEL,{self.tp},TAN2,Z,{start},{end}"

    def number_of_divisions(self, start, end='', step=''):
        '''Select lines by number of divisions within the line.'''
        return f"LSEL,{self.tp},NDIV,,{start},{end},{step}"
    
    def space_ratio(self, start, end=''):
        '''Select lines by spacing ratio of line divisions.'''
        return f"LSEL,{self.tp},SRAT,,{start},{end}"

    def material(self, start, end='', step=''):
        '''Select lines by material number associated with the line.'''
        return f"LSEL,{self.tp},MAT,,{start},{end},{step}"
    
    def element_type(self, start, end='', step=''):
        '''Select lines by element type number associated with the line.'''
        return f"LSEL,{self.tp},TYPE,,{start},{end},{step}"

    def real_constant(self, start, end='', step=''):
        '''Select lines by real constant number associated with the line.'''
        return f"LSEL,{self.tp},REAL,,{start},{end},{step}"

    def element_coordinate_system(self, start, end='', step=''):
        '''Select lines by element coordinate system associated with the line.'''
        return f"LSEL,{self.tp},ESYS,,{start},{end},{step}"

    def section(self, start, end='', step=''):
        '''Select lines by cross section ID number.'''
        return f"LSEL,{self.tp},SEC,,{start},{end},{step}"

    def length(self, start, end=''):
        '''Select lines by length of the line.'''
        return f"LSEL,{self.tp},LENGTH,,{start},{end}"
    
    def radius(self, start, end=''):
        '''Select lines by radius of the line.'''
        return f"LSEL,{self.tp},RADIUS,,{start},{end}"

    def hard_points(self, start, end='', step=''):
        '''Select lines by associated hard points.'''
        return f"LSEL,{self.tp},HPT,,{start},{end},{step}"

    def lcca(self, start, end='', step=''):
        '''Select concatenated lines (selects only lines that were created by concatenation [LCCAT]).'''
        return f"LSEL,{self.tp},LCCA,,{start},{end},{step}"

class S(_Type):
    def __init__(self):
        super().__init__('S')

    def pick(self, kswp: int=0):
        '''Selects a single line.

        kswp: 0 or 1
        '''
        if kswp not in [0, 1]:
            raise ValueError("The kswp for LESL is not 0 or 1.")
        return f"LSEL,{self.tp},P,,,,,{kswp}"

    def line_number(self, start, end='', step='', kswp=0):
        '''Select lines by line number range.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},LINE,,{start},{end},{step},{kswp}"
    
    def loc_x(self, start, end='', kswp=0):
        '''Select lines by X location range.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},LOC,X,{start},{end},,{kswp}"
    
    def loc_y(self, start, end='', kswp=0):
        '''Select lines by Y location range.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},LOC,Y,{start},{end},,{kswp}"
    
    def loc_z(self, start, end='', kswp=0):
        '''Select lines by Z location range.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},LOC,Z,{start},{end},,{kswp}"
    
    def ext(self, kswp=0):
        '''Select lines on exterior of selected area.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},EXT,,,,,{kswp}"
    
    def tangent_x_at_beginning(self, start, end='', kswp=0):
        '''Select lines by unit vector component of outward tangent at beginning of line.

        start or end: -1~1
        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},TAN1,X,{start},{end},,{kswp}"
    
    def tangent_y_at_beginning(self, start, end='', kswp=0):
        '''Select lines by unit vector component of outward tangent at beginning of line.

        start or end: -1~1
        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},TAN1,Y,{start},{end},,{kswp}"
    
    def tangent_z_at_beginning(self, start, end='', kswp=0):
        '''Select lines by unit vector component of outward tangent at beginning of line.

        start or end: -1~1
        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},TAN1,Z,{start},{end},,{kswp}"
    
    def tangent_x_at_end(self, start, end='', kswp=0):
        '''Select lines by unit vector component of outward tangent at end of line.

        start or end: -1~1
        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},TAN2,X,{start},{end},,{kswp}"
    
    def tangent_y_at_end(self, start, end='', kswp=0):
        '''Select lines by unit vector component of outward tangent at end of line.

        start or end: -1~1
        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},TAN2,Y,{start},{end},,{kswp}"
    
    def tangent_z_at_end(self, start, end='', kswp=0):
        '''Select lines by unit vector component of outward tangent at end of line.

        start or end: -1~1
        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},TAN2,Z,{start},{end},,{kswp}"
    
    def number_of_divisions(self, start, end='', step='', kswp=0):
        '''Select lines by number of divisions within the line.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},NDIV,,{start},{end},{step},{kswp}"
    
    def space_ratio(self, start, end='', kswp=0):
        '''Select lines by spacing ratio of line divisions.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},SRAT,,{start},{end},,{kswp}"
    
    def material(self, start, end='', step='', kswp=0):
        '''Select lines by material number associated with the line.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},MAT,,{start},{end},{step},{kswp}"
    
    def element_type(self, start, end='', step='', kswp=0):
        '''Select lines by element type associated with the line.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},TYPE,,{start},{end},{step},{kswp}"
    
    def real_constant(self, start, end='', step='', kswp=0):
        '''Select lines by real constant number associated with the line.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},REAL,,{start},{end},{step},{kswp}"
    
    def element_coordinate_system(self, start, end='', step='', kswp=0):
        '''Select lines by element coordinate system associated with the line.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},ESYS,,{start},{end},{step},{kswp}"
    
    def section(self, start, end='', step='', kswp=0):
        '''Select lines by cross section ID number.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},SEC,,{start},{end},{step},{kswp}"
    
    def length(self, start, end='', kswp=0):
        '''Select lines by length of the line.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},LENGTH,,{start},{end},,{kswp}"
    
    def radius(self, start, end='', kswp=0):
        '''Select lines by radius of the line.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},RADIUS,,{start},{end},,{kswp}"
    
    def hard_points(self, start, end='', step='', kswp=0):
        '''Select lines by associated hard points.

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},HPT,,{start},{end},{step},{kswp}"
    
    def lcca(self, kswp=0):
        '''Select concatenated lines (selects only lines that were created by concatenation [LCCAT]).

        kswp: 0 or 1
        '''
        return f"LSEL,{self.tp},LCCA,,,,,{kswp}"

class LSEL(_api):
    '''Selects a subset of lines.'''
    processor = Processor.any

    S = S()
    R = _Type('R')
    A = _Type('A')
    U = _Type('U')

    @classmethod
    def _check(cls, command):
        paras = cls._get_all_paras(command)
        pass

    @staticmethod
    def all():
        '''Selects all lines.'''
        return "LSEL,ALL"
    
    @staticmethod
    def none():
        '''Unselect the full set.'''
        return "LSEL,NONE"

    @staticmethod
    def inve():
        '''Invert the current set (selected becomes unselected and vice versa).'''
        return "LSEL,INVE"
    
    @staticmethod
    def stat():
        '''Display the current select status.'''
        return "LSEL,STAT"