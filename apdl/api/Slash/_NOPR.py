from .._api import _api, Processor

class NOPR(_api):

    processor = Processor.any

    @classmethod
    def _check(cls, command):
        raise NotImplementedError
    
    @staticmethod
    def noprint():
        '''Suppresses all output to the screen and the output file. Use /NOPRINT to suppress all output to the screen and the output file. Use /NOPRINT,ON to suppress all output to the screen and the output file. Use /NOPRINT,OFF to resume output to the screen and the output file.'''
        return "/NOPR"