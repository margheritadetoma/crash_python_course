##############################
#######  EX 4 SOLUTION  ######
##############################

The Rational() class takes in input a float x and a precision p.

The __init__ calls the method continued_fraction_approx() that converts x into a fraction (num/den) up to the given precision (p) using the continued fraction method.
The function preliminarly stores the sign and also checks if x is an int (eventually it returns num=x, den=1). Then the iterative continued fraction algorithm returns the numerator and denominator. Then the method simplify_common_factors() simplifies the common factor between num and den using the decomposion in prime factors. The method first calls the function decomposition_prime_factors() importing it from assignments.ex3.ex3_5_solution. decomposition_prime_factors() finds the decomposition in prime factors of x and y and returns them as lists (x_dec, y_dec). Note that it is the full decomposition, not only the prime numbers which are divisible by the input value (e.g. 12 would be [2,2,3]).
Then some side cases are checked (x=1, y=1, x=0, y=0). A loop then removes from x_dec and y_dec all the values that are in common. The new numerator (num) will be the product of the remaining x_dec and the denominator (den) the product of the remaining y_dec. The function returns the numerator (sign * num) and the denominator (den). 


The class contains also some dundler methods:
- __str__: print num/den

- __repr__: print Rational( input_float, precision=1.e-5)

- __abs__: compute the absolute value

- __add__(): makes the addition between the rational representation up to the specified precision of two float numbers

- __sub__(): makes the subtraction between the rational representation up to the specified precision of two float numbers

- __mul__(): makes the product between the rational representation up to the specified precision of two float numbers

- __truediv__(): makes the division between the rational representation up to the specified precision of two float numbers

- __eq__(): tests if two numbers are equal checking their rational representation up to the specified precision

- __gt__(): tests if the first number is greater than the second one checking their rational representation up to the specified precision

- __lt__(): tests if the first number is lesser than the second one checking their rational representation up to the specified precision

- __hash__(): uses the Cantor pairing function to make the a unique number from the numerator d denominator of the rational representation




#############################
#######   TEST EX 4   #######
#############################

The class TestRational is used to implement some tests for the Rational class inheriting the unittest.TestCase class provided by the unittest module.
The number that are used are pi (taken with 7 digits, 3.1415926) and the Nepero number e (taken with 7 digits, 2.7182818):
- r1 = Rational(3.1415927);
- r2 = Rational(3.1415927);
- r3 = Rational(2.7182818);
- r4 = Rational(-2.7182818).

** test_edge_case: tests how a int number is treated (e.g. 1) and check the 0.

** test_continued_fraction_approx: 355/113 is the fraction representing pi up to the fifth digit. The function tests if the method of the Rational class succeeds in recovering those two number as num and den.

** test_simplify_common_factors: the function tests if 30/12 is correctly simplified as 5/2.

** test_str: the function tests if str(self.r1) is '355/113'.

** test_repr: the function tests if repr(self.r1) corresponds to the string 'Rational(3.1415929203539825, precision=1e-05)'.

** test_abs: the function tests if the absolute value of pi is pi (up to the fifth digit) and if the absolute value of -e is e (up to the fifth digit).

** test_add: the function tests that the sum of two different Rationals (pi+pi) is the Rational(pi+pi) (up to the fifth digit).

** test_sub: the function tests that the difference of two different Rationals (pi+pi) is the Rational(0) (up to the fifth digit).

** test_mul: the function tests that the product of two different Rationals (pi \dot pi) is the Rational(2pi) (up to the fifth digit).

** test_div: the function tests that the division of two different Rationals (pi/pi) is the Rational(1) (up to the fifth digit).

** test_eq: the function tests the equality operator.

** test_gt: the function tests the 'grater than' operator.

** test_lt: the function tests the 'lesser than' operator.

** test_hash: he function tests the hash of a Rational is an int and that the hash of pi and pi are the same.







