import unittest
from hapdl.apdl.api.A import A


class TestA(unittest.TestCase):

    def test_call(self):
        self.assertEqual(A.call("a", "b"), "A,a,b")

    def test_check(self):
        self.assertEqual(A._check("A,P"), True)
        self.assertEqual(A._check("A,P,,,,,,"), True)
        self.assertEqual(A._check("A,1,1,2,3"), True)
        self.assertEqual(A._check("A,1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18"), False)
        self.assertEqual(A._check(" A, P,1"), True)
        self.assertEqual(A._check("A,1,2,"), False)

    def test_by_pick(self):
        self.assertEqual(A.by_pick(), "A,P")

    def test_by_points(self):
        self.assertEqual(A.by_points(1, 2, 3), "A,1,2,3")
        self.assertEqual(A.by_points(1, 2, 3, 4), "A,1,2,3,4")
        with self.assertRaises(ValueError):
            A.by_points(1, 2)
        with self.assertRaises(ValueError):
            A.by_points(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

if __name__ == '__main__':
    unittest.main()