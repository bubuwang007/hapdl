from .._api import _api, Processor

class SECWRITE(_api):
    '''Creates an ASCII file containing user mesh section information.

    Before creating a user mesh file, first create a model using 2-D meshing. Use PLANE183 or MESH200 with KEYOPT(1) = 7 (quadrilateral with 8 nodes option) to model the cells. SECWRITE creates an ASCII file that contains information about the nodes and cells that describe a beam section. 
    '''

    processor = Processor.prep7

    @staticmethod
    def write(fname, elem_type: str):
        '''Creates an ASCII file containing user mesh section information.'''
        return f"SECWRITE,{fname},,{elem_type}"