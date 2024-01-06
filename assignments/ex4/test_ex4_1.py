import unittest
from assignments.ex4.ex4_1_solution import Rational



class TestRational(unittest.TestCase):

    def setUp(self):
        self.r = Rational(3.1415926)
        self.r2 = Rational(3.1415926)

    def test_edge_case(self):
        r_test = Rational(1)
        self.assertEqual(r_test.num, 1)
        self.assertEqual(r_test.den, 1)
    
    def test_num_den(self): 
        self.assertEqual(self.r.num, 355)
        self.assertEqual(self.r.den, 113)


    def test_continued_fraction_approx(self):
        pass


    def test_simplify_common_factors(self):
        pass


    def test_str(self):
        self.assertEqual(str(self.r), '355/113')


    def test_repr(self): #355/113=3.1415929203539825
        self.assertEqual(repr(self.r) ,'Rational(3.1415929203539825, precision=1e-05)')

    
    def test_add(self):
        self.assertEqual(self.r+self.r2, Rational(6.2831852))


    def test_mul(self):
        pass

    def test_eq(self):
        pass

    def test_hash(self):
        pass



if __name__ == '__main__':
    unittest.main()