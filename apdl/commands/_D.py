from ._C import CEND
from ._APDLCommands import APDL_Commands

DSTART = CEND + 1

class D(APDL_Commands):
    D = DSTART              # Defines degree-of-freedom constraints at nodes.
    DA = DSTART + 1         # Defines degree-of-freedom constraints on areas.
    DADELE = DSTART + 2     # Deletes degree-of-freedom constraints on an area.
    DALIST = DSTART + 3     # Lists the DOF constraints on an area.
    DAMORPH = DSTART + 4    # Move nodes in selected areas to conform to structural displacements.
    DATA = DSTART + 5       # Reads data records from a file into a variable.
    DATADEF = DSTART + 6    # Specifies "Directly defined data status" as the subsequent status topic.
    DCGOMG = DSTART + 7     # Specifies the rotational acceleration of the global origin.
    DCUM = DSTART + 8       # Specifies that DOF constraint values are to be accumulated.
    DCVSWP = DSTART + 9     # Performs a DC voltage sweep on a ROM element.
    DDASPEC = DSTART + 10   # Specifies the shock spectrum computation constants for DDAM analysis.
    DDELE = DSTART + 11     # Deletes degree-of-freedom constraints.
    DDOPTION = DSTART + 12  # Sets domain decomposer option for Distributed ANSYS.
    DEACT = DSTART + 13     # Specifies "Element birth and death" as the subsequent status topic.
    DEFINE = DSTART + 14    # Specifies "Data definition settings" as the subsequent status topic.
    DELETE = DSTART + 15    # Specifies sets in the results file to be deleted before postprocessing.
    DELTIM = DSTART + 16    # Specifies the time step sizes to be used for the current load step.
    DEMORPH = DSTART + 17   # Move nodes in selected elements to conform to structural displacements.
    DERIV = DSTART + 18     # Differentiates a variable.
    DESIZE = DSTART + 19    # Controls default element sizes.
    DESOL = DSTART + 20     # Defines or modifies solution results at a node of an element.
    DETAB = DSTART + 21     # Modifies element table results in the database.
    DFLX = DSTART + 22      # Imposes a uniform magnetic flux B on an edge-element electromagnetic model.
    DFSWAVE = DSTART + 23   # Specifies the incident planar waves with random phases for a diffuse sound field.
    DIG = DSTART + 24       # Digitizes nodes to a surface.
    DIGIT = DSTART + 25     # Specifies "Node digitizing" as the subsequent status topic.
    DISPLAY = DSTART + 26   # Specifies "Display settings" as the subsequent status topic.
    DJ = DSTART + 27        # Specifies boundary conditions on the components of relative motion of a joint element.
    DJDELE = DSTART + 28    # Deletes boundary conditions on the components of relative motion of a joint element.
    DJLIST = DSTART + 29    # Lists boundary conditions applied to joint elements.
    DK = DSTART + 30        # Defines DOF constraints at keypoints.
    DKDELE = DSTART + 31    # Deletes DOF constraints at a keypoint.
    DKLIST = DSTART + 32    # Lists the DOF constraints at keypoints.
    DL = DSTART + 33        # Defines DOF constraints on lines.
    DLDELE = DSTART + 34    # Deletes DOF constraints on a line.
    DLIST = DSTART + 35     # Lists DOF constraints.
    DLLIST = DSTART + 36    # Lists DOF constraints on a line.
    DMOVE = DSTART + 37     # Digitizes nodes on surfaces and along intersections.
    DMPEXT = DSTART + 38    # Extracts modal damping coefficients in a specified frequency range.
    DMPOPTION = DSTART + 39 # Specifies distributed memory parallel (Distributed ANSYS) file combination options.
    DMPRAT = DSTART + 40    # Sets a constant modal damping ratio.
    DMPSTR = DSTART + 41    # Sets a constant structural damping coefficient.
    DNSOL = DSTART + 42     # Defines or modifies solution results at a node.
    DOF = DSTART + 43       # Adds degrees of freedom to the current DOF set.
    DOFSEL = DSTART + 44    # Selects a DOF label set for reference by other commands.
    DOMEGA = DSTART + 45    # Specifies the rotational acceleration of the structure.
    DSCALE = DSTART + 46    # Scales DOF constraint values.
    DSET = DSTART + 47      # Sets the scale and drawing plane orientation for a digitizing tablet.
    DSPOPTION = DSTART + 48 # Sets memory option for the distributed sparse solver.
    DSUM = DSTART + 49      # Specifies the double sum mode combination method.
    DSURF = DSTART + 50     # Defines the surface upon which digitized nodes lie.
    DSYM = DSTART + 51      # Specifies symmetry or antisymmetry degree-of-freedom constraints on nodes.
    DSYS = DSTART + 52      # Activates a display coordinate system for geometry listings and plots.
    DTRAN = DSTART + 53     # Transfers solid model DOF constraints to the finite element model.
    DUMP = DSTART + 54      # Dumps the contents of a binary file.
    DVAL = DSTART + 55      # Defines values at enforced motion base.
    DVMORPH = DSTART + 56   # Move nodes in selected volumes to conform to structural displacements.
    DYNOPT = DSTART + 57    # Specifies dynamic analysis options.

DEND = DSTART + len(D.__members__) - 1