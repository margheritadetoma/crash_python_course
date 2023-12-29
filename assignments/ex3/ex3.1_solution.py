import sys



def divisibility_check(n):

	'''
	Check of the integer value from input is
	divisible by 2,3,5 or 7.
	It collects then these values in the
	divisible_by array with their frequency
	of divisibility.

    Parameters
    ----------
    n : int
        a number

    Returns
    -------
    divisible_by: list of integers
        the numbers that pass the
        divisibility check with
        multiplicity

    '''

	n = int(n)

	divisors = [2, 3, 5, 7]
	divisible_by = []
	array_of_powers = []

	for div in divisors:
		m = n
		while m%div == 0:
			if m==n:
				print('{} is divisible by {}'.format(n,div))
			divisible_by.append(div)
			m = m / div
		if (m ==n):
			print('{} is not divisible by {}'.format(n,div))



	return divisible_by





def division(x, y):

	'''
	It uses the function divisibility_check()
	to get the lists of the divisors: A and B.
	Then it makes a "difference" element by element
	of A and B: this will be the list C.
	The result of x/y will be the product of the
	element of C.

	Parameters
    ----------
    x : int
        a number
    y : int
        a number

    Returns
    -------
    division: int
    	a number: x/y 
	'''

	from collections import Counter

	A = divisibility_check(x)
	B = divisibility_check(y)


	counter_A = Counter(A)
	counter_B = Counter(B)


	C = list((counter_A - counter_B).elements()) #simplify all the same elements in common between A and B

	if len(C)>0: #If this condition is not satisfied, x and y are not divisible
		from functools import reduce
		import operator
		division = reduce(operator.mul, C) #multiply all the element of C
		print('{} dividied by {} is:'.format(x,y))
		return division

	else:
		return print('{} is not divisible by {}'.format(x,y))



if __name__ == "__main__" :
    x = sys.argv[1]
    y = sys.argv[2]
    #print(x,y)
    #print(divisibility_check(x))
    #print(divisibility_check(y))
    print(division(x,y))
