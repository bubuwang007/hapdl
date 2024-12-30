from .._api import _api, Processor

class A(_api):
    processor = Processor.prep7

    @classmethod
    def _check(cls, command: str) -> bool:
        paras = cls._get_all_paras(command)

        if len(paras) == 0:
            return False

        if paras[1]=='P':
            return True

        if len(paras) < 4 or len(paras) > 19:
            return False

        return True

    @classmethod
    def by_pick(cls) -> str:
        '''
        If P1 = P, graphical picking is enabled and all remaining argumentsare ignored (valid only in the GUI).
        '''
        return "A,P"

    @classmethod
    def by_points(cls, *points) -> str:
        '''
        Keypoints (P1 through P18) must be input in a clockwise or counterclockwise order around the area. This order also determines the positive normal direction of the area according to the right-hand rule. Existing lines between adjacent keypoints will be used; missing lines are generated "straight" in the active coordinate system and assigned the lowest available numbers.If more than one line exists between two keypoints, the shorter one will be chosen. If the area is to be defined with more than four keypoints, the required keypoints and lines must lie on a constant coordinate value in the active coordinate system (such as a plane or a cylinder). Areas may be redefined only if not yet attached to a volume. Solid modeling in a toroidal coordinate system is not recommended.
        '''
        if len(points) < 3 :
            raise ValueError("At least 3 points are required")
        elif len(points) > 18:
            raise ValueError("At most 18 points are allowed")
        return f"A,{','.join(map(str, points))}"