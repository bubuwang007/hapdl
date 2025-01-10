from .._api import _api, Processor

class CM(_api):
    '''Groups geometry items into a component.'''
    processor = Processor.any

    @classmethod
    def _check(cls, command):
        raise NotImplementedError

    @staticmethod
    def create(name: str, entity_type: str, check: bool = True):
        '''An alphanumeric name used to identify this component. Cname may be up to 32 characters, beginning with a letter and containing only letters, numbers, and underscores.

        name:
            Name of the component.
        entity_type:
            Type of the entities.
            VOLU | AREA | LINE | KP | ELEM | NODE
        check:
            Check if the component already exists.
        '''
        if check:
            if len(name) > 32:
                raise ValueError("Name of the component must be up to 32 characters.")
            if entity_type.upper() not in ['VOLU', 'AREA', 'LINE', 'KP', 'ELEM', 'NODE']:
                raise ValueError("Type of the entities must be one of VOLU, AREA, LINE, KP, ELEM, NODE.")
        return f"CM,{name},{entity_type}"
    
    @staticmethod
    def create_volu(name: str, check: bool = True):
        '''Create a component for volumes.'''
        return CM.create(name, 'VOLU', check)
    
    @staticmethod
    def create_area(name: str, check: bool = True):
        '''Create a component for areas.'''
        return CM.create(name, 'AREA', check)
    
    @staticmethod
    def create_line(name: str, check: bool = True):
        '''Create a component for lines.'''
        return CM.create(name, 'LINE', check)
    
    @staticmethod
    def create_kp(name: str, check: bool = True):
        '''Create a component for keypoints.'''
        return CM.create(name, 'KP', check)
    
    @staticmethod
    def create_elem(name: str, check: bool = True):
        '''Create a component for elements.'''
        return CM.create(name, 'ELEM', check)
    
    @staticmethod
    def create_node(name: str, check: bool = True):
        '''Create a component for nodes.'''
        return CM.create(name, 'NODE', check)