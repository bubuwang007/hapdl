from .._api import _api, Processor
from .get._ACTIVE import ACTIVE
from .get._CMD import CMD


class GET(_api):
    '''Retrieves a value and stores it as a scalar parameter or part of an array parameter.
    *GET, Par, Entity, ENTNUM, Item1, IT1NUM, Item2, IT2NUM
    '''
    processor = Processor.any

    active: ACTIVE = ACTIVE
    cmd: CMD = CMD