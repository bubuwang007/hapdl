import enum
from ._func import get_comp

class COMP_TYPE(enum.Enum):
    NODES = 1
    ELEMENTS = 2
    KEYPOINTS = 6
    LINES = 7
    AREAS = 8
    VOLUMES = 9
    SUB1 = 11
    SUB2 = 12
    SUB3 = 13
    SUB4 = 14
    SUB5 = 15

class COMP:

    @staticmethod
    def component_number(par: str):
        '''Total number of components and assemblies currently defined.'''
        return get_comp(par, 0, "NCOMP")

    @staticmethod
    def name(par: str, entnum):
        '''Name of the Nth item (component or assembly) in the list of components and assemblies. A character parameter is returned.'''
        return get_comp(par, entnum, "NAME")

    @staticmethod
    def type(par: str, entnum):
        '''Type of the Nth item (component or assembly) in the list of components and assemblies. A character parameter is returned.'''
        return get_comp(par, entnum, "TYPE")
    
    @staticmethod
    def type_entity(par: str, entnum):
        '''Type of the Nth item (component or assembly) in the list of components and assemblies. A character parameter is returned.'''
        return COMP_TYPE(COMP.type(par, entnum))

    @staticmethod
    def number_of_subcomponents(par: str, entnum):
        '''Number of subcomponents in the Nth item (component or assembly) in the list of components and assemblies. An integer parameter is returned.'''
        return get_comp(par, entnum, "NSCOMP")

# print(COMP.component_number("n"))