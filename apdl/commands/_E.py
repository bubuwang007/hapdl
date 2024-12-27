from ._D import DEND
from ._APDLCommands import APDL_Commands

ESTART = DEND + 1

class E(APDL_Commands):
    E = ESTART              # Defines an element by node connectivity.
    EALIVE = ESTART + 1     # Reactivates an element (for the birth and death capability).
    ECPCHG = ESTART + 2     # Optimizes degree-of-freedom usage in a coupled acoustic model.
    EDADAPT = ESTART + 3    # Activates adaptive meshing in an explicit dynamic analysis.
    EDALE = ESTART + 4      # Assigns mesh smoothing to explicit dynamic elements that use the ALE formulation.
    EDASMP = ESTART + 5     # Creates a part assembly to be used in an explicit dynamic analysis.
    EDBOUND = ESTART + 6    # Defines a boundary plane for sliding or cyclic symmetry.
    EDBX = ESTART + 7       # Creates a box shaped volume to be used in a contact definition for explicit dynamics.
    EDBVIS = ESTART + 8     # Specifies global bulk viscosity coefficients for an explicit dynamics analysis.
    EDCADAPT = ESTART + 9   # Specifies adaptive meshing controls for an explicit dynamic analysis.
    EDCGEN = ESTART + 10    # Specifies contact parameters for an explicit dynamics analysis.
    EDCLIST = ESTART + 11   # Lists contact entity specifications in an explicit dynamics analysis.
    EDCMORE = ESTART + 12   # Specifies additional contact parameters for a given contact definition in an explicit dynamic analysis.
    EDCNSTR = ESTART + 13   # Defines various types of constraints for an explicit dynamic analysis.


EEND = ESTART + len(E.__members__) - 1