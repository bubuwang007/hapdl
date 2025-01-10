from .._api import _api, Processor

class VIEW(_api):
    '''Defines the viewing direction for the display.'''
    processor = Processor.any

    @classmethod
    def _check(cls, command):
        raise NotImplementedError
    
    @classmethod
    def call(cls, *args) -> str:
        return f"/{cls.__name__},{','.join(args)}"
    
    @staticmethod
    def along_line_from_xyz_to_origin(x: float, y: float, z: float, window: int = 1):
        '''Specifies the viewing direction along a line from the specified XYZ location to the origin.'''
        return f"/VIEW,{window},{x},{y},{z}"
    
    @staticmethod
    def along_x_positive(window: int = 1):
        '''Specifies the viewing direction along the positive X axis.'''
        return f"/VIEW,{window},-1,0,0"

    @staticmethod
    def along_x_negative(window: int = 1):
        '''Specifies the viewing direction along the negative X axis.'''
        return f"/VIEW,{window},1,0,0"

    @staticmethod
    def along_y_positive(window: int = 1):
        '''Specifies the viewing direction along the positive Y axis.'''
        return f"/VIEW,{window},0,-1,0"
    
    @staticmethod
    def along_y_negative(window: int = 1):
        '''Specifies the viewing direction along the negative Y axis.'''
        return f"/VIEW,{window},0,1,0"
    
    @staticmethod
    def along_z_positive(window: int = 1):
        '''Specifies the viewing direction along the positive Z axis.'''
        return f"/VIEW,{window},0,0,-1"
    
    @staticmethod
    def along_z_negative(window: int = 1):
        '''Specifies the viewing direction along the negative Z axis.'''
        return f"/VIEW,{window},0,0,1"
