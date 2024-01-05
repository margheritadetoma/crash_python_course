import math

class Rational() :

    """Documentation of the class
    """

    def __init__(self, num, precision=1.e-5):
        print(self.continued_fraction_approx(num, precision))


    def continued_fraction_approx(self, x, p): #x=num, p=precision

        '''
        1. Initialisation of variables:
         * Let $x$ be the real number you want to approximate
         * Set $a_0 = \floor{x} (the floor function gives the greatest integer less than or equal to $x$)
         * Let $x_1 = x - a_0$
        2. Generate continued fractions by iterating the following steps until the required precision (e.g. $p=10^{-5}$) is not met:
         * Let $a_i$ be the floor of $1/x_i$
         * update $x_{i+1} = \dfrac{1}{x_i} - a_i$
         * check that $|\dfrac{n_i}{d_i}-x|>p$ if not, stop the iterations.
           ($n_i$ and $d_i$ are the numerator and denominator of the approximate fraction at step $i$)
        

        > **Note that**
        > * $n_0 = 1$ and $n_1 = a_0$
        > * $d_0 = 0$ and $d_1 = 1$
        > * $n_i = a_i \cdot n_{i-1} + n_{i-2}$
        > * $d_i = a_i \cdot d_{i-1} + d_{i-2}$
        '''

        sgn = +1
        if x < 0:
            x = -x
            sgn = -1


        ai = math.floor(x)
        xi = x - ai
        nj, ni = 1, ai   #j=i-1
        dj, di = 0, 1

        while (abs(ni / di - x) > p):
            print(ai, xi, ni, nj, di, dj)
            ai = math.floor(1 / xi)
            xi = 1 / xi - ai

            ni, nj = ai * ni + nj, ni
            di, dj = ai * di + dj, di

        return sgn*ni, di



    def __str__(self):
    	pass
    def __repr__(self):
    	pass
    def __add__(self):
    	pass
    # [ ... ] overload all the arithmetic operators
    def __eq__(self) :
    	pass
    # [ ... ] overload all the comparison operators

    ####################################################
    # Optional functions:
    
    def __hash__(self) :
    	pass
    def to_integer_low(self):
    	"""Documentation of function `to_integer_low`"""
    	pass
    def to_integer_upp(self):
    	"""Documentation of function `to_integer_upp`"""
    	pass



if __name__=='__main__':
    r = Rational(3.1415926)





