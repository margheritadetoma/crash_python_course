##############################
#######  EX 4 SOLUTION  ######
##############################

I created a Rational() class that takes as input the float x.

The __init__ call the module continued_fraction_approx() that converts x into a fraction between num and den up to the given precision (p) using the continued fraction method.
The function preliminarly stores the sign and also checks if the input number is an int. Then it does the cycle in the while loop accordingly to the algorithm of the continued fraction giving the numerator and denominator. Then it is called the module simplify_common_factors() which simplifies the common factor between num and den using the decomposion in prime factors. It first calls the function decomposition_prime_factors() importing it from assignments.ex3.ex3_5_solution. Decomposition_prime_factors() finds the decomposition in prime factors of x and y and returns them as lists (x_dec, y_dec). Note that it is the full decomposition, not only the prime numbers which are divisible by the input value (e.g. 12 would be [2,2,3]).
Then some side cases are checked (x=1, y= 1, x=0, y=0). The loop then remove from x_dec and y_dec all the values that are in common. Then the new numerator (num) is the product of all the x_dec and the denominator (den) is the product of all the y_dec. The function returns the  numerator (num, with sign) and the denominator (den). 


The class contains also some dundler methods:
- __str__: print num/den

- __repr__: print Rational( input_float, precision=1.e-5)

- __abs__: compute the absolute value

- __add__(): Makes the addition between the rational representation up to the specified precision of two float numbers

- __sub__(): Makes the subtraction between the rational representation up to the specified precision of two float numbers

- __mul__(): Makes the product between the rational representation up to the specified precision of two float numbers

- __truediv__(): Makes the division between the rational representation up to the specified precision of two float numbers

- __eq__(): Tests if two numbers are equal checking their rational representation up to the specified precision

- __gt__(): Tests if the first number is greater than the second one checking their rational representation up to the specified precision

- __lt__(): Tests if the first number is lesser than the second one checking their rational representation up to the specified precision

- __hash__(): Uses the Cantor pairing function to make the a unique number from the numerator d denominator of the rational representation