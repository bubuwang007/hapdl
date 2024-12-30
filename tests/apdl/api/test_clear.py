import unittest
from hapdl.apdl.api.Slash import CLEAR

class TestCLEAR(unittest.TestCase):

    def test_call(self):
        self.assertEqual(CLEAR.call("a", "b"), "/CLEAR,a,b")

    def test_check(self):
        self.assertEqual(CLEAR._check("/CLEAR"), True)
        self.assertEqual(CLEAR._check("/CLEAR,START"), True)
        self.assertEqual(CLEAR._check("/CLEAR,NOSTART"), True)
        self.assertEqual(CLEAR._check("/CLEAR,START,1"), False)
        self.assertEqual(CLEAR._check("/CLEAR,1"), False)
        self.assertEqual(CLEAR._check(" /CLEAR"), True)
        self.assertEqual(CLEAR._check("/CLEAR, START"), True)

    def test_start(self):
        self.assertEqual(CLEAR.start(), "/CLEAR,START")

    def test_nostart(self):
        self.assertEqual(CLEAR.nostart(), "/CLEAR,NOSTART")

if __name__ == '__main__':
    unittest.main()