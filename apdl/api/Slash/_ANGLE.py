from .._api import _api, Processor


class ANGLE(_api):
    """Rotates the display about an axis."""

    processor = Processor.any

    @classmethod
    def _check(cls, command):
        raise NotImplementedError

    @classmethod
    def call(cls, *args) -> str:
        return f"/{cls.__name__},{','.join(args)}"

    @staticmethod
    def rotate(
        angle: float = "", axis: str = "", cumulate: bool = False, window: int = 1
    ):
        """Rotates the display about an axis defined by the specified XYZ location and the specified angle.
        
        angle:
            Angle (degrees) for changing display orientation (positive, counterclockwise about specified axis).
        
        axis:
            Rotation axis: XS, YS, or ZS (default) for the screen axes; XM, YM, or ZM for the global Cartesian model axes. ZS is normal to the screen; all axes pass through the focus point.

        cumulate:
            False: Do not use cumulative successive rotations.
            True: Use cumulative rotations. Rotations are relative to the previous rotation. View settings (/VIEW) are recalculated.
        
        """
        return f"/ANGLE,{window},{angle},{axis},{1 if cumulate else 0}"

    @staticmethod
    def rotate_about_screen_x(angle, cumulate: bool = False, window: int=1):
        '''Rotates the display about the screen X axis.'''
        return f"/ANGLE,{window},{angle},XS,{1 if cumulate else 0}"

    @staticmethod
    def rotate_about_screen_y(angle, cumulate: bool = False, window: int=1):
        '''Rotates the display about the screen Y axis.'''
        return f"/ANGLE,{window},{angle},YS,{1 if cumulate else 0}"

    @staticmethod
    def rotate_about_screen_z(angle, cumulate: bool = False, window: int=1):
        '''Rotates the display about the screen Z axis.'''
        return f"/ANGLE,{window},{angle},ZS,{1 if cumulate else 0}"

    @staticmethod
    def rotate_about_global_x(angle, cumulate: bool = False, window: int=1):
        '''Rotates the display about the global X axis.'''
        return f"/ANGLE,{window},{angle},XM,{1 if cumulate else 0}"
    
    @staticmethod
    def rotate_about_global_y(angle, cumulate: bool = False, window: int=1):
        '''Rotates the display about the global Y axis.'''
        return f"/ANGLE,{window},{angle},YM,{1 if cumulate else 0}"
    
    @staticmethod
    def rotate_about_global_z(angle, cumulate: bool = False, window: int=1):
        '''Rotates the display about the global Z axis.'''
        return f"/ANGLE,{window},{angle},ZM,{1 if cumulate else 0}"
    