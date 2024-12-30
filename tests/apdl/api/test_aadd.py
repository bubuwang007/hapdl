import unittest
from hapdl.apdl.api.A import AADD


class TestAADD(unittest.TestCase):

    def test_call(self):
        self.assertEqual(AADD.call("a", "b"), "AADD,a,b")

    def test_check(self):
        self.assertEqual(AADD._check("AADD,P"), True)
        self.assertEqual(AADD._check("AADD,P,,,,,,"), True)
        self.assertEqual(AADD._check("AADD,ALL"), True)
        self.assertEqual(AADD._check("AADD,1,2,3,4"), True)
        self.assertEqual(AADD._check("AADD,1,2,3,4,5,6,7,8,9,10,11"), False)
        self.assertEqual(AADD._check(" AADD, P,1"), True)
        self.assertEqual(AADD._check("AADD,1,2,"), True)
        self.assertEqual(AADD._check("AADD,1,"), False)

    def test_by_pick(self):
        self.assertEqual(AADD.by_pick(), "AADD,P")
        self.assertEqual(AADD.by_all(), "AADD,ALL")

    def test_by_all(self):
        self.assertEqual(AADD.by_all(), "AADD,ALL")

    def test_by_areas(self):
        self.assertEqual(AADD.by_areas(1, 2), "AADD,1,2")
        self.assertEqual(AADD.by_areas(1, 2, 3), "AADD,1,2,3")
        with self.assertRaises(ValueError):
            AADD.by_areas(1)
        with self.assertRaises(ValueError):
            AADD.by_areas(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

if __name__ == '__main__':
    unittest.main()