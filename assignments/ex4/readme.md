##############################
#######  EX 4 SOLUTION  ######
##############################

I created a Rational() class that takes as input the float x.
The init call the module continued_fraction_approx() that converts writes x as a ration between num and den up to the given precision. 

The function continued_fraction_approx() uses the continued fraction method to convert x into a fraction up to the precision p. The function preliminarly stores the sign and also checks if the input number is an int. Then it does the cycle in the while loop accordingly to the algorithm. The module simplify_common_factors() simplifies the common factor between num and den using the decomposion in prime factors. The function returns the sign (with sign) and the den. 
The function simplify_common_factors(x,y) first calls the function decomposition_prime_factors() importing it from assignments.ex3.ex3_5_solution. Decomposition_prime_factors() finds the decomposition in prime factors of x and y and returns them as lists (x_dec, y_dec). Note that it is the full decomposition, not only the prime numbers which are divisible by the input value (e.g. 12 would be [2,2,3]).
Then I check some side cases (x=1, y= 1, x=0, y=0). The loop then remove from x_dec and y_dec all the common values. Then the new numerator (num) is the product of all the x_dec and the denominator (den) is the product of all the y_dec.

The class contains also some dundler methods:
- __str__: print num/den
- __repr__: print Rational( input_float, precision=1.e-5)
- __abs__: compute the absolute value