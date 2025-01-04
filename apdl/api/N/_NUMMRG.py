from .._api import _api, Processor


class NUMMRG(_api):
    '''Merges coincident or equivalently defined items.
    
    The NUMMRG command does not change a model's geometry, only the topology.
    After issuing the command, the area and volume sizes (ASUM and VSUM) may give slightly different results. In order to obtain the same results as before, use /FACET, /NORMAL, and ASUM / VSUM.

    The merge operation is useful for tying separate but coincident parts of a model together. If not all items are to be checked for merging, use the select commands (NSEL, ESEL, etc.) to select items. Only selected items are included in the merge operation for nodes, keypoints, and elements.

    By default, the merge operation retains the lowest numbered coincident item.Higher numbered coincident items are deleted. Set Switch to HIGH to retain the highest numbered coincident item after the merging operation.Applicable related items are also checked for deleted item numbers and if found, are replaced with the retained item number. For example, if nodes are merged, element connectivities (except superelements), mesh item range associativity, coupled degrees of freedom, constraint equations, master degrees of freedom, gap conditions, degree of freedom constraints, nodal force loads, nodal surface loads, and nodal body force loads are checked. Merging material numbers (NUMMRG,ALL or NUMMRG,MAT) does not update the material number referenced:

    * By temperature-dependent film coefficients as part of convection load or a temperature-dependent emissivity as part of a surface-to-surface radiation load (SF, SFE, SFL, SFA)

    * By real constants for multi-material elements (such as SOLID65)

    When merging tapered beam or pipe sections, the program first uses the associated end sections for merging. If the merge is successful, the program replaces the tapered section database with the end section data.

    If a unique load is defined among merged nodes, the value is kept and applied to the retained node. If loads are not unique (not recommended), only the value on the lowest node (or highest if Switch = HIGH) is kept (except for "force" loads for which the values are summed if they are not defined via tabular boundary conditions).
    ...
    '''
    processor = Processor.any

    @classmethod
    def _check(cls, command):
        raise NotImplementedError

    @staticmethod
    def node(toler: float = 1e-4,):
        return f"NUMMRG,NODE,{toler}"

    @staticmethod
    def kp(toler: float = 1e-4,):
        return f"NUMMRG,KP,{toler}"

    @staticmethod
    def elem(toler: float = 1e-4,):
        return f"NUMMRG,ELEM,{toler}"
    



    
    