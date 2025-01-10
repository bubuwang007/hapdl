from .._api import _api, Processor

class IMMED(_api):
    '''Allows immediate display of a model as it is generated.'''
    processor = Processor.prep7

    @classmethod
    def _check(cls, command):
        raise NotImplementedError

    @staticmethod
    def on():
        '''Display only upon request, i.e., no immediate display.'''
        return "IMMED,1"

    @staticmethod
    def off():
        '''Display immediately as model is generated.'''
        return "IMMED,0"