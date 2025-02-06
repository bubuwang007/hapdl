import unittest
from hapdl.apdl.api.S._SECTYPE import SECTYPE

class TestSectype(unittest.TestCase):
   
   def test_beam(self):
        self.assertEqual(SECTYPE.beam.rect(1), "SECTYPE,1,BEAM,RECT,,0")
        self.assertEqual(SECTYPE.beam.quad(1), "SECTYPE,1,BEAM,QUAD,,0")
        self.assertEqual(SECTYPE.beam.csolid(1), "SECTYPE,1,BEAM,CSOLID,,0")
        self.assertEqual(SECTYPE.beam.ctube(1), "SECTYPE,1,BEAM,CTUBE,,0")
        self.assertEqual(SECTYPE.beam.chan(1), "SECTYPE,1,BEAM,CHAN,,0")
        self.assertEqual(SECTYPE.beam.i(1), "SECTYPE,1,BEAM,I,,0")
        self.assertEqual(SECTYPE.beam.z(1), "SECTYPE,1,BEAM,Z,,0")
        self.assertEqual(SECTYPE.beam.l(1), "SECTYPE,1,BEAM,L,,0")
        self.assertEqual(SECTYPE.beam.t(1), "SECTYPE,1,BEAM,T,,0")
        self.assertEqual(SECTYPE.beam.hats(1), "SECTYPE,1,BEAM,HATS,,0")
        self.assertEqual(SECTYPE.beam.hrec(1), "SECTYPE,1,BEAM,HREC,,0")
        self.assertEqual(SECTYPE.beam.asec(1), "SECTYPE,1,BEAM,ASEC,,0")
        self.assertEqual(SECTYPE.beam.mesh(1), "SECTYPE,1,BEAM,MESH,,0")      
    


if __name__ == "__main__":
    unittest.main()