import math
from assignments.ex3 import ex4_5_solution


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
        decomposition in prime factors

    __str__():
        Print as a string the number as rational

    __repr__():
        Print a string containing info about the float
        input number and the requested precision

    __add__():
        Makes the addition between the rational representation
        up to the specified precision of two float numbers

    __mul__():
        Makes the product between the rational representation
        up to the specified precision of two float numbers

    __eq__():
        Tests if two numbers are equal checking their rational 
        representation up to the specified precision

    __hash__():
        Uses the Cantor pairing function to make the a unique
        number from the numerator and denominator of the rational
        representation

    """


    def __init__(self, num, precision=1.e-5):
        self.num, self.den = self.continued_fraction_approx(num, precision)
        self.num, self.den = self.simplify_common_factors(self.num, self.den)
        self.precision = precision


    def continued_fraction_approx(self, x, p): #x=num, p=precision

        #Store the sign 
        sgn = +1
        if x < 0:
            x = -x
            sgn = -1

        ai = math.floor(x)
        xi = x - ai
        nj, ni = 1, ai   #j=i-1
        dj, di = 0, 1

        while (abs(ni / di - x) > p):
            ai = math.floor(1 / xi)
            xi = 1 / xi - ai

            ni, nj = ai * ni + nj, ni
            di, dj = ai * di + dj, di

        ni, di = self.simplify_common_factors(int(ni), int(di))

        return sgn*ni, di


    def simplify_common_factors(self, x, y):
        x_dec = ex4_5_solution.decomposition_prime_factors(int(x))
        y_dec = ex4_5_solution.decomposition_prime_factors(int(y))
        
        for i in range(len(x_dec)):
            for j in range(len(y_dec)):
                if x_dec[i]==y_dec[j]:
                    del y_dec[j]

        num = 1
        for i in range(0, len(x_dec)):
            num = num *  x_dec[i]

        den = 1
        for i in range(0, len(y_dec)):
            den = den *  y_dec[i]

        return num, den


    def __str__(self):
        return f'{self.num}/{self.den}'


    def __repr__(self):
        return f'Rational({self.num/self.den}, precision={self.precision})'


    def __add__(self, r2): #r2 = second rational
        r_sum = Rational(1)
        r_sum.num, r_sum.den = self.simplify_common_factors(self.num * r2.den + self.den * r2.num, self.den * r2.den)
        return r_sum


    def __mul__(self, r2):
        r_prod = Rational(1) 
        r_prod.num, r_prod.den = self.simplify_common_factors(self.num * r2.num, self.den * r2.den)
        return r_prod


    def __eq__(self, r2):
        return (self.num == r2.num and self.den == r2.den)

    
    def __hash__(self):
        return (self.num + self.den) * (self.num + self.den + 1) // 2 + self.num 




if __name__=='__main__':
    r1 = Rational(3.1415926)
    r2 = Rational(3.14159)

    #print(r1+r2)
    #print(r1*r2)
    #print(r1==r2)


    #print({1:r1, 2:r2})
    #print({r1:1, r2:2})
    print(r1.decomposition_prime_factors())

