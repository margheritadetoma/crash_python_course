import math
import sys
from assignments.ex3.ex3_5_solution import decomposition_prime_factors


class Rational() :

    """
    A class for converting a float into a rational number with
    a given precision.


    Attributes
    ----------
    num : float
        the number to be handled
    precision : float
        the precision of the conversion into rational


    Methods
    -------
    continued_fraction_approx(x, p)
        Converts the float 'x' into a fraction up to the
        precision 'p' using the continued fraction method

    simplify_common_factors(x, y)
        Simplifies the common factors of the 
        decomposition in prime factors of x and y


    __round__(self, ndigits=5):
        Round the input number up to ndigits
    
    __str__():
        Prints as a string the number given as rational

    __repr__():
        Prints a string containing info about the float
        input number and the requested precision
    
    __abs__(self):
        Returns the absolute value

    __add__():
        Makes the addition between the rational representation
        up to the specified precision of two float numbers

    __sub__():
        Makes the subtraction between the rational representation
        up to the specified precision of two float numbers

    __mul__():
        Makes the product between the rational representation
        up to the specified precision of two float numbers

    __truediv__():
        Makes the division between the rational representation
        up to the specified precision of two float numbers

    __eq__():
        Tests if two numbers are equal checking their rational 
        representation up to the specified precision

    __gt__():
        Tests if the first number is greater than the
        second one checking their rational representation
        up to the specified precision

    __lt__():
        Tests if the first number is lesser than the
        second one checking their rational representation
        up to the specified precision

    __hash__():
        Uses the Cantor pairing function to make the a unique
        number from the numerator and denominator of the rational
        representation

    """



    def __init__(self, x, precision=1.e-5):
        self.num, self.den = self.continued_fraction_approx(x, precision)
        self.precision = precision



    def continued_fraction_approx(self, x, p):
        
        '''
        Converts the float 'x' into a fraction up to the
        precision 'p' using the continued fraction method

        Parameters
        ----------
        x : float
            float input number
        p : float
            float number for the requested precision

        Returns
        -------
        (sgn * numerator, denominator) : sgn*int, int
            numerator (with sign) and denominator of the
            fraction that cannot be decomposed more
        '''

        #Store the sign 
        sgn = +1
        if x < 0:
            x = -x
            sgn = -1

        # Check if the number is a int. Eventually,
        # returns num = x and den = 1
        if isinstance(x, int):
            return x, 1


        ai = math.floor(x)
        xi = x - ai
        nj, ni = 1, ai   #j=i-1
        dj, di = 0, 1

        while (abs(ni / di - x) > p):
            ai = math.floor(1 / xi)
            xi = 1 / xi - ai
            ni, nj = ai * ni + nj, ni
            di, dj = ai * di + dj, di

        ni, di = self.simplify_common_factors(ni, di)

        return sgn*ni, di



    def simplify_common_factors(self, x, y):

        '''
        Simplifies the common factors of the 
        decomposition in prime factors of x and y.

        !! Warning !!:
        x is assumed to be the numerator
        and y the denominator

        Parameters
        ----------
        x : int
            int number
        y : int
            int number

        Returns
        -------
        num, den : int, int
            x,y after simplify the common factors
        '''

        x_dec = decomposition_prime_factors(x)
        y_dec = decomposition_prime_factors(y)


        if x==1:
            return 1, y

        if y==1:
            return x, 1

        if x==0:
            return 0, 1

        if y==0:
            print('Divison by zero.')
            return None, None
        
   
        for element in x_dec[:]:  # Use x_dec[:] to create a copy of the list
            if element in y_dec:
                x_dec.remove(element)
                y_dec.remove(element)

        # Do the product of the decomposition factors
        num = 1
        for i in range(0, len(x_dec)):
            num *= x_dec[i]

        den = 1
        for i in range(0, len(y_dec)):
            den *= y_dec[i]

        return num, den



    def __round__(self, ndigits=5):

        '''
        Round the input number up to ndigits

        Parameters
        ----------

        Returns
        -------
        float :
            rounded input float
        '''

        return round(self.num/self.den, 5)



    def __str__(self):

        '''
        Prints as a string the number given as rational

        Parameters
        ----------

        Returns
        -------
        str : num/den
        '''

        return f'{self.num}/{self.den}'



    def __repr__(self):

        '''
        Prints a string containing info about the float
        input number and the requested precision

        Parameters
        ----------

        Returns
        -------
        str : num/den, precision( )
        '''

        return f'Rational({self.num/self.den}, precision={self.precision})'



    def __abs__(self):

        '''
        Returns the absolute value

        Parameters
        ----------

        Returns
        -------
        Rational : 
            absolute value of the rational
        '''

        return Rational(abs(self.num) / self.den)



    def __add__(self, other):

        '''
        Makes the addition between the rational representation
        up to the specified precision of two float numbers

        Parameters
        ----------
        other : class Rational()

        Returns
        -------
        r_sum : class Rational()
            sum of two rational numbers (still a rational)
        '''

        return Rational(self.num/self.den + other.num/other.den)



    def __sub__(self, other):

        '''
        Makes the subtraction between the rational representation
        up to the specified precision of two float numbers

        Parameters
        ----------
        other : class Rational()

        Returns
        -------
        r_sum : class Rational()
            subtraction of two rational numbers (still a rational)
        '''

        return Rational(self.num/self.den - other.num/other.den)



    def __mul__(self, other):

        '''
        Makes the product between the rational representation
        up to the specified precision of two float numbers

        Parameters
        ----------
        other : class Rational()

        Returns
        -------
        r_prod : class Rational()
            product of two rational numbers (still a rational)
        '''

        return Rational(self.num * other.num / (self.den * other.den))


    def __truediv__(self, other):

        '''
        Makes the division between the rational representation
        up to the specified precision of two float numbers

        Parameters
        ----------
        other : class Rational()

        Returns
        -------
        r_div : class Rational()
            division of two rational numbers (still a rational)
        '''

        return Rational(self.num * other.den / (self.den * other.num))



    def __eq__(self, other):

        '''
        Tests if two numbers are equal checking their rational 
        representation up to the specified precision

        Parameters
        ----------
        other : class Rational()

        Returns
        -------
        boolean: True/False
            True: the two rational numbers are equal
            False: the two rational numbers are different
        '''

        return (self.num == other.num and self.den == other.den)



    def __gt__(self, other):

        '''
        Tests if the first number is greater than the
        second one checking their rational representation
        up to the specified precision

        Parameters
        ----------
        other : class Rational()

        Returns
        -------
        boolean: True/False
            True: first number greater than second one
            False: first number lesser than second one
        '''

        return (self.num/self.den > other.num/other.den)



    def __lt__(self, other):

        '''
        Tests if the first number is lesser than the
        second one checking their rational representation
        up to the specified precision

        Parameters
        ----------
        other : class Rational()

        Returns
        -------
        boolean: True/False
            True: first number lesser than second one
            False: first number greater than second one
        '''

        return (self.num/self.den < other.num/other.den)


    
    def __hash__(self):

        '''
        Uses the Cantor pairing function to make the a unique
        number from the numerator and denominator of the rational
        representation

        Parameters
        ----------

        Returns
        -------
        float: Cantor pairing value
        '''

        return (self.num + self.den) * (self.num + self.den + 1) // 2 + self.num 





if __name__=='__main__':
    r1 = Rational(3.1415926)
    r2 = Rational(3.1415926)
    r3 = Rational(3.1415926 ** 2)

    print(r1)

