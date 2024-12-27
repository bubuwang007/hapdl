import unittest
from hapdl.apdl.commands._APDLCommands import APDL_Commands
from hapdl.apdl.commands._A import A, ASTART, AEND
from hapdl.apdl.commands._B import B, BSTART, BEND
from hapdl.apdl.commands._C import C, CSTART, CEND
from hapdl.apdl.commands._D import D, DSTART, DEND

class TestCommand(unittest.TestCase):

    def test_command(self):
        self.assertTrue(APDL_Commands)

    def test_a(self):
        self.assertEqual(A.A.value, ASTART)
        self.assertEqual(A.AADD.value, ASTART+1)
        self.assertEqual(A.AWAVE.value, AEND)
        self.assertEqual(A.get_command(A.A), "A")
        self.assertEqual(A.is_apdl_command("A"), True)
        self.assertEqual(AEND, ASTART + len(A.__members__)-1)

    def test_b(self):
        self.assertEqual(B.BCSOPTION.value, BSTART)
        self.assertEqual(B.BETAD.value, BSTART+1)
        self.assertEqual(B.BUCOPT.value, BEND)
        self.assertEqual(B.get_command(B.BCSOPTION), "BCSOPTION")
        self.assertEqual(B.is_apdl_command("BCSOPTION"), True)
        self.assertEqual(BEND, BSTART + len(B.__members__)-1)

    def test_c(self):
        self.assertEqual(C.CSTARSTARSTAR.value, CSTART)
        self.assertEqual(C.CNVTOL.value, CSTART+53)
        self.assertEqual(C.CZMESH.value, CEND)
        self.assertEqual(C.get_command(C.CSTARSTARSTAR), "C***")
        self.assertEqual(C.is_apdl_command("C***"), True)
        self.assertEqual(CEND, CSTART + len(C.__members__)-1)

    def test_d(self):
        self.assertEqual(D.D.value, DSTART)
        self.assertEqual(D.DTRAN.value, DSTART+53)
        self.assertEqual(D.DYNOPT.value, DEND)
        self.assertEqual(D.get_command(D.D), "D")
        self.assertEqual(D.is_apdl_command("D"), True)
        self.assertEqual(DEND, DSTART + len(D.__members__)-1)

if __name__ == '__main__':
    unittest.main()