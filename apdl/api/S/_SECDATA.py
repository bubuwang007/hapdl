from .._api import _api, Processor

class _BEAM:
    '''Beam sections are referenced by BEAM188 and BEAM189 elements. Not all SECOFFSET location values are valid for each subtype.'''
    
    @staticmethod
    def rect(b, h, nb=2, nh=2):
        '''Rectangular beam section.'''
        return f"SECDATA,{b},{h},{nb},{nh}"

    @staticmethod
    def quad(yi, zi, yj, zj, yk, zk, yl, zl, ng=2, nh=2):
        '''Quadrilateral beam section.'''
        return f"SECDATA,{yi},{zi},{yj},{zj},{yk},{zk},{yl},{zl},{ng},{nh}"

    @staticmethod
    def csolid(r, n=8, t=2):
        '''Circular solid beam section.'''
        return f"SECDATA,{r},{n},{t}"
    
    @staticmethod
    def ctube(ri, ro, n=8):
        '''Circular tube beam section.'''
        return f"SECDATA,{ri},{ro},{n}"
    
    @staticmethod
    def chan(w1, w2, w3, t1, t2, t3):
        '''Channel beam section.'''
        return f"SECDATA,{w1},{w2},{w3},{t1},{t2},{t3}"

    @staticmethod
    def i(w1, w2, w3, t1, t2, t3):
        '''I-beam section.'''
        return f"SECDATA,{w1},{w2},{w3},{t1},{t2},{t3}"
    
    @staticmethod
    def z(w1, w2, w3, t1, t2, t3):
        '''Z-beam section.'''
        return f"SECDATA,{w1},{w2},{w3},{t1},{t2},{t3}"
    
    @staticmethod
    def L(w1, w2, t1, t2):
        '''L-beam section.'''
        return f"SECDATA,{w1},{w2},{t1},{t2}"

    @staticmethod
    def t(w1, w2, t1, t2):
        '''T-beam section.'''
        return f"SECDATA,{w1},{w2},{t1},{t2}"

    @staticmethod
    def hats(w1, w2, w3, w4, t1, t2, t3, t4, t5):
        '''Hat beam section.'''
        return f"SECDATA,{w1},{w2},{w3},{w4},{t1},{t2},{t3},{t4},{t5}"

    @staticmethod
    def hrec(w1, w2, t1, t2, t3, t4):
        '''Rectangular hollow beam section.'''
        return f"SECDATA,{w1},{w2},{t1},{t2},{t3},{t4}"

    @staticmethod
    def asec(A, Iyy, Iyz, Izz, Iw, J, CGy, CGz, SHy, SHz, TKz, TKy):
        ''' A = Area of section
            Iyy = Moment of inertia about the y axis
            Iyz = Product of inertia
            Izz = Moment of inertia about the z axis
            Iw = Warping constant
            J = Torsional constant
            CGy = y coordinate of centroid
            CGz = z coordinate of centroid
            SHy = y coordinate of shear center
            SHz = z coordinate of shear center
            TKz = Thickness along Z axis (maximum height)
            TKy = Thickness along Y axis (maximum width)
        '''
        return f"SECDATA,{A},{Iyy},{Iyz},{Izz},{Iw},{J},{CGy},{CGz},{SHy},{SHz},{TKz},{TKy}"


class SECDATA:
    '''Describes the geometry of a section.'''
    processor = Processor.prep7
    beam = _BEAM
