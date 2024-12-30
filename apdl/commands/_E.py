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
    EDCONTACT = ESTART + 14 # Specifies contact surface controls for an explicit dynamics analysis.
    EDCPU = ESTART + 15     # Specifies CPU time limit for an explicit dynamics analysis.
    EDCRB = ESTART + 16     # Constrains two rigid bodies to act as one in an explicit dynamics analysis.
    EDCSC = ESTART + 17     # Specifies whether to use subcycling in an explicit dynamics analysis.
    EDCTS = ESTART + 18     # Specifies mass scaling and scale factor of computed time step for an explicit dynamics analysis.
    EDCURVE = ESTART + 19   # Specifies data curves for an explicit dynamic analysis.
    EDDAMP = ESTART + 20    # Defines mass weighted (Alpha) or stiffness weighted (Beta) damping for an explicit dynamics model.
    EDDBL = ESTART + 21     # Selects a numerical precision type of the explicit dynamics analysis.
    EDDC = ESTART + 22      # Deletes or deactivates/reactivates contact surface specifications in an explicit dynamic analysis.
    EDDRELAX = ESTART + 23  # Activates initialization to a prescribed geometry or dynamic relaxation for the explicit analysis.
    EDDUMP = ESTART + 24    # Specifies output frequency for the explicit dynamic restart file (d3dump).
    EDELE = ESTART + 25     # Deletes selected elements from the model.
    EDENERGY = ESTART + 26  # Specifies energy dissipation controls for an explicit dynamics analysis.
    EDFPLOT = ESTART + 27   # Allows plotting of explicit dynamics forces and other load symbols.
    EDGCALE = ESTART + 28   # Defines global ALE controls for an explicit dynamic analysis.
    EDHGLS = ESTART + 29    # Specifies the hourglass coefficient for an explicit dynamics analysis.
    EDHIST = ESTART + 30    # Specifies time-history output for an explicit dynamic analysis.
    EDHTIME = ESTART + 31   # Specifies the time-history output interval for an explicit dynamics analysis.
    EDINT = ESTART + 32     # Specifies number of integration points for explicit shell and beam output.
    EDIPART = ESTART + 33   # Defines inertia for rigid parts in an explicit dynamics analysis.
    EDIS = ESTART + 34      # Specifies stress initialization in an explicit dynamic full restart analysis.
    EDLCS = ESTART + 35     # Defines a local coordinate system for use in explicit dynamics analysis.
    EDLOAD = ESTART + 36    # Specifies loads for an explicit dynamics analysis.
    EDMP = ESTART + 37      # Defines material properties for an explicit dynamics analysis.
    EDNB = ESTART + 38      # Defines a nonreflecting boundary in an explicit dynamic analysis.
    EDNDTSD = ESTART + 39   # Allows smoothing of noisy data for explicit dynamics analyses and provides a graphical representation of the data.
    EDNROT = ESTART + 40    # Applies a rotated coordinate nodal constraint in an explicit dynamics analysis.
    EDOPT = ESTART + 41     # Specifies the type of output for an explicit dynamics analysis.
    EDOUT = ESTART + 42     # Specifies time-history output (ASCII format) for an explicit dynamics analysis.
    EDPART = ESTART + 43    # Configures parts for an explicit dynamics analysis.

EEND = ESTART + len(E.__members__) - 1