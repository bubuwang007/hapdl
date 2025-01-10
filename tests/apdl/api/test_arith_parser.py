import unittest
from hapdl.apdl.api.BASIC._Number import Number as num
from hapdl.apdl.api.arith_parser._Node_Types import *


class Test_Node_Types(unittest.TestCase):

    def setUp(self):
        self.a = NUMBER(num("a"))
        self.b = NUMBER(num("b"))
        self.c = NUMBER(num("c"))
        self.d = EXPRESSION("ABS(-5)")

    def test_plus(self):
        plus = PLUS(self.a, self.b)
        self.assertEqual(str(plus), "a+b")

    def test_minus(self):
        minus = MINUS(self.a, self.b)
        self.assertEqual(str(minus), "a-b")

    def test_times(self):
        times = TIMES(self.a, self.b)
        self.assertEqual(str(times), "a*b")

    def test_divide(self):
        divide = DIVIDE(self.a, self.b)
        self.assertEqual(str(divide), "a/b")

    def test_expression(self):
        self.assertEqual(str(EXPRESSION("ABS(-5)")), "ABS(-5)")

    def test_number_plus_expression(self):
        plus = PLUS(self.a, self.d)
        self.assertEqual(str(plus), "a+ABS(-5)")

    def test_plus_times(self):
        expr1 = PLUS(self.a, TIMES(self.b, self.c))
        expr2 = TIMES(PLUS(self.a, self.b), self.c)
        expr3 = TIMES(PLUS(self.a, self.b), PLUS(self.a, self.b))
        self.assertEqual(str(expr1), "a+b*c")
        self.assertEqual(str(expr2), "(a+b)*c")
        self.assertEqual(str(expr3), "(a+b)*(a+b)")

    def test_minus_times(self):
        expr1 = MINUS(self.a, TIMES(self.b, self.c))
        expr2 = TIMES(MINUS(self.a, self.b), self.c)
        expr3 = TIMES(MINUS(self.a, self.b), MINUS(self.a, self.b))
        self.assertEqual(str(expr1), "a-b*c")
        self.assertEqual(str(expr2), "(a-b)*c")
        self.assertEqual(str(expr3), "(a-b)*(a-b)")

    def test_power(self):
        expr1 = POWER(self.a, self.b)
        expr2 = POWER(PLUS(self.a, self.b), self.c)
        expr3 = POWER(self.a, PLUS(self.b, self.c))
        expr4 = POWER(PLUS(self.a, self.b), PLUS(self.a, self.b))

        self.assertEqual(str(expr1), "a**b")
        self.assertEqual(str(expr2), "(a+b)**c")
        self.assertEqual(str(expr3), "a**(b+c)")
        self.assertEqual(str(expr4), "(a+b)**(a+b)")

    def test_neg(self):
        neg = NEG(self.a)
        neg1 = NEG(self.d)
        neg2 = NEG(PLUS(self.a, self.b))
        neg3 = NEG(POWER(self.a, self.b))
        self.assertEqual(str(neg), "-a")
        self.assertEqual(str(neg1), "-ABS(-5)")
        self.assertEqual(str(neg2), "-(a+b)")
        self.assertEqual(str(neg3), "-a**b")

    def test_eqeq(self):
        eqeq = EQEQ(self.a, self.b)
        eqeq1 = EQEQ(PLUS(self.a, self.b), self.c)
        self.assertEqual(str(eqeq), "a,EQ,b")
        self.assertEqual(str(eqeq1), "a+b,EQ,c")

    def test_gt(self):
        gt = GT(self.a, self.b)
        gt1 = GT(PLUS(self.a, self.b), self.c)
        self.assertEqual(str(gt), "a,GT,b")
        self.assertEqual(str(gt1), "a+b,GT,c")

    def test_ge(self):
        ge = GE(self.a, self.b)
        ge1 = GE(PLUS(self.a, self.b), self.c)
        self.assertEqual(str(ge), "a,GE,b")
        self.assertEqual(str(ge1), "a+b,GE,c")

    def test_lt(self):
        lt = LT(self.a, self.b)
        lt1 = LT(PLUS(self.a, self.b), self.c)
        self.assertEqual(str(lt), "a,LT,b")
        self.assertEqual(str(lt1), "a+b,LT,c")

    def test_le(self):
        le = LE(self.a, self.b)
        le1 = LE(PLUS(self.a, self.b), self.c)
        self.assertEqual(str(le), "a,LE,b")
        self.assertEqual(str(le1), "a+b,LE,c")

    def test_neq(self):
        neq = NEQ(self.a, self.b)
        neq1 = NEQ(PLUS(self.a, self.b), self.c)
        self.assertEqual(str(neq), "a,NE,b")
        self.assertEqual(str(neq1), "a+b,NE,c")  

if __name__ == '__main__':
    unittest.main()