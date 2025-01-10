import unittest
from hapdl.apdl.api.BASIC import Number

class Test_Number(unittest.TestCase):

    def setUp(self):
        self.a = Number("a")
        self.b = Number("b")
        self.c = Number("c")

    def test_add(self):
        self.assertEqual(str(self.a + self.b), "a+b")
        self.assertEqual(str(self.a + 1.56), "a+1.56")
        self.assertEqual(str(self.a + self.b + self.c), "a+b+c")
        self.assertEqual(str(1.56 + self.a), "1.56+a")

    def test_sub(self):
        self.assertEqual(str(self.a - self.b), "a-b")
        self.assertEqual(str(self.a - 1.56), "a-1.56")
        self.assertEqual(str(self.a - self.b - self.c), "a-b-c")
        self.assertEqual(str(1.56 - self.a), "1.56-a")

    def test_mul(self):
        self.assertEqual(str(self.a * self.b), "a*b")
        self.assertEqual(str(self.a * 1.56), "a*1.56")
        self.assertEqual(str(self.a * self.b * self.c), "a*b*c")
        self.assertEqual(str(1.56 * self.a), "1.56*a")

    def test_truediv(self):
        self.assertEqual(str(self.a / self.b), "a/b")
        self.assertEqual(str(self.a / 1.56), "a/1.56")
        self.assertEqual(str(self.a / self.b / self.c), "a/b/c")
        self.assertEqual(str(1.56 / self.a), "1.56/a")

    def test_neg(self):
        self.assertEqual(str(-self.a), "-a")
        self.assertEqual(str(-self.a+1), "-a+1")
        self.assertEqual(str(1+-self.a), "1+-a")

    def test_pow(self):
        self.assertEqual(str(self.a ** self.b), "a**b")
        self.assertEqual(str(self.a ** 1.56), "a**1.56")
        self.assertEqual(str(self.a ** self.b ** self.c), "a**b**c")
        self.assertEqual(str(1.56 ** self.a), "1.56**a")
        t1 = self.a +5
        self.assertEqual(str(t1** (self.b + self.c)), "(a+5)**(b+c)")

    def test_compound(self):
        t1 = self.a + 5
        t2 = t1 * self.b
        t3 = t2 / self.c
        t4 = -t3 ** self.a
        self.assertEqual(str(t4), "-((a+5)*b/c)**a")

    def test_change_pre(self):
        Number.change_pre("p")
        a = Number("a")
        self.assertEqual(str(a), "pa")
        Number.change_pre("")

    def test_set(self):
        self.assertEqual(str(self.a.set(5)), "a=5")
        self.assertEqual(str(self.a << 5), "a=5")

    def test_delete(self):
        self.assertEqual(str(self.a.delete()), "a=")

    def test_eq(self):
        self.assertEqual(str(self.a == 5), "a,EQ,5")

    def test_ne(self):
        self.assertEqual(str(self.a != 5), "a,NE,5")

    def test_lt(self):
        self.assertEqual(str(self.a < 5), "a,LT,5")

    def test_gt(self):
        self.assertEqual(str(self.a > 5), "a,GT,5")

    def test_le(self):
        self.assertEqual(str(self.a <= 5), "a,LE,5")

    def test_ge(self):
        self.assertEqual(str(self.a >= 5), "a,GE,5")

if __name__ == "__main__":
    unittest.main()