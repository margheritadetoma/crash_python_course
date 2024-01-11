import unittest
from assignments.ex4.ex4_1_solution import Rational



class TestRational(unittest.TestCase):

    
    def setUp(self):
        self.r1 = Rational(3.1415927)
        self.r2 = Rational(3.1415927)
        self.r3 = Rational(2.7182818)
        self.r4 = Rational(-2.7182818)


    def test_edge_case(self):
        # Check an int
        r_test_1 = Rational(1)
        # Check zero
        r_test_0 = Rational(0)
        self.assertEqual(r_test_1.num, 1)
        self.assertEqual(r_test_1.den, 1)
        self.assertEqual(r_test_0.num, 0)
        self.assertEqual(r_test_0.den, 1)



    def test_continued_fraction_approx(self):
        self.assertEqual(self.r1.continued_fraction_approx(3.1415927, 1e-5), (355,113))


    def test_simplify_common_factors(self):
        self.assertEqual(self.r1.simplify_common_factors(30,12), (5,2))


    def test_str(self):
        self.assertEqual(str(self.r1), '355/113')


    def test_repr(self): #355/113=3.1415929203539825
        self.assertEqual(repr(self.r1) ,'Rational(3.1415929203539825, precision=1e-05)')


    def test_abs(self):
        self.assertAlmostEqual(abs(self.r4), self.r3, 1e-05)
        self.assertAlmostEqual(abs(self.r1), self.r1, 1e-05)


    def test_add(self):
        self.assertAlmostEqual(self.r1 + self.r2, Rational(2*3.1415927), 1e-05)


    def test_sub(self):
        self.assertAlmostEqual(self.r1 - self.r2, Rational(0), 1e-05)
        

    def test_mul(self):
        self.assertAlmostEqual(self.r1 * self.r2, Rational(3.1415927**2), 1e-05)


    def test_div(self):
        self.assertAlmostEqual(self.r1 / self.r2, Rational(1), 1e-05)


    def test_eq(self):
        self.assertEqual(self.r1 == self.r2, True)


    def test_gt(self):
        self.assertEqual(self.r1 > self.r3, True)


    def test_lt(self):
        self.assertEqual(self.r3 < self.r2, True)


    def test_hash(self):
        self.assertEqual(isinstance(hash(self.r1), int), True)
        self.assertEqual(hash(self.r1), hash(self.r2))



if __name__ == '__main__':
    unittest.main()