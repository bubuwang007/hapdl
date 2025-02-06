from .._api import _api, Processor

class _BEAM:
    '''Defines a beam section.
    REFINEKEY:
        Sets mesh refinement level for thin-walled beam sections. Valid values are 0 (the default - no mesh refinement) through 5 (high level of mesh refinement). This value has meaning only when Type = BEAM.
    '''
    @staticmethod
    def _general(id:int, subtype:str, name:str, refinekey:int):
        return f"SECTYPE,{id},BEAM,{subtype},{name},{refinekey}"
    
    @staticmethod
    def rect(id:int, name="", refinekey: int=0):
        '''矩形'''
        return _BEAM._general(id, "RECT", name, refinekey)

    @staticmethod
    def quad(id:int, name="", refinekey: int=0):
        '''四边形'''
        return _BEAM._general(id, "QUAD", name, refinekey)

    @staticmethod
    def csolid(id:int, name="", refinekey: int=0):
        '''圆形实心'''
        return _BEAM._general(id, "CSOLID", name, refinekey)

    @staticmethod
    def ctube(id:int, name="", refinekey: int=0):
        '''圆形管'''
        return _BEAM._general(id, "CTUBE", name, refinekey)

    @staticmethod
    def chan(id:int, name="", refinekey: int=0):
        '''槽形'''
        return _BEAM._general(id, "CHAN", name, refinekey)

    @staticmethod
    def i(id:int, name="", refinekey: int=0):
        '''工字形'''
        return _BEAM._general(id, "I", name, refinekey)

    @staticmethod
    def z(id:int, name="", refinekey: int=0):
        '''Z形'''
        return _BEAM._general(id, "Z", name, refinekey)

    @staticmethod
    def l(id:int, name="", refinekey: int=0):
        '''L形'''
        return _BEAM._general(id, "L", name, refinekey)

    @staticmethod
    def t(id:int, name="", refinekey: int=0):
        '''T形'''
        return _BEAM._general(id, "T", name, refinekey)

    @staticmethod
    def hats(id:int, name="", refinekey: int=0):
        '''帽形'''
        return _BEAM._general(id, "HATS", name, refinekey)

    @staticmethod
    def hrec(id:int, name="", refinekey: int=0):
        '''空心矩形'''
        return _BEAM._general(id, "HREC", name, refinekey)

    @staticmethod
    def asec(id:int, name="", refinekey: int=0):
        '''任意截面'''
        return _BEAM._general(id, "ASEC", name, refinekey)

    @staticmethod
    def mesh(id:int, name="", refinekey: int=0):
        '''用户定义网格'''
        return _BEAM._general(id, "MESH", name, refinekey)

class _TAPER:
    '''Defines a tapered beam or pipe section. The sections at the end points must be topologically identical.'''
    pass

class _GENB:
    '''Defines a composite (temperature-dependent) beam section.'''
    pass

class _PIPE:
    '''Defines a pipe section.'''
    pass

class _LINK:
    '''Defines a link section.'''
    pass

class _AXIS:
    '''Define the axis for a general axisymmetric section.'''
    pass

class _SHELL:
    '''Defines a shell section.'''
    pass

class _PRETENSION:
    '''Defines a pretension section.'''
    pass

class _JOINT:
    '''Defines a joint section.'''
    pass

class _REINF:
    '''Defines a reinforced section.'''
    pass

class _CONTACT:
    '''Defines a contact section.'''
    pass

class SECTYPE(_api):
    '''Associates section type information with a section ID number.'''
    processor = Processor.prep7

    beam = _BEAM