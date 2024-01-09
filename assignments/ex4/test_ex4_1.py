import unittest
from assignments.ex4.ex4_1_solution import Rational



class TestRational(unittest.TestCase):

    
    def setUp(self):
        self.r1 = Rational(3.1415926)
        self.r2 = Rational(3.1415926)


    def test_edge_case(self):
        r_test = Rational(1)
        self.assertEqual(r_test.num, 1)
        self.assertEqual(r_test.den, 1)
    

    def test_num_den(self):
        self.assertEqual(self.r1.num, 355)
        self.assertEqual(self.r1.den, 113)


    def test_continued_fraction_approx(self):
        self.assertEqual(self.r1.continued_fraction_approx(3.1415926, 1e-5), (355,113))


    def test_simplify_common_factors(self):
        self.assertEqual(self.r1.simplify_common_factors(30,12), (5,2))


    def test_str(self):
        self.assertEqual(str(self.r1), '355/113')


    def test_repr(self): #355/113=3.1415929203539825
        self.assertEqual(repr(self.r1) ,'Rational(3.1415929203539825, precision=1e-05)')


    def test_add(self):
        self.assertEqual(self.r1 + self.r2, Rational(2*3.1415926))


    def test_sub(self):
        self.assertEqual(self.r1 - self.r2, Rational(0))
        

    def test_mul(self):
        self.assertEqual(self.r1 * self.r2, Rational(3.1415926**2))


    def test_div(self):
        #self.assertEqual(self.r1 / self.r2, Rational(1))
        pass


    def test_eq(self):
        self.assertEqual(self.r1 == self.r2, True)


    def test_gt(self):
        self.assertEqual(self.r1 > self.r2, True)


    def test_lt(self):
        self.assertEqual(self.r1 < self.r2, True)


    def test_hash(self):
        self.assertEqual(isinstance(hash(self.r1), int), True)
        self.assertEqual(hash(self.r1), hash(self.r2))



if __name__ == '__main__':
    unittest.main()