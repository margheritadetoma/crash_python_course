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
			print('{} is divisible by {}'.format(n,div))
			divisible_by.append(div)
			m = m / div


	return divisible_by





def division(x, y):

	from collections import Counter

	divisors_x, pow_x = divisibility_check(x)
	divisors_y, pow_y = divisibility_check(y)

	A = []
	B = []

	for i in range(0,len(divisors_x)):
		for j in range(0, pow_x[i]):
			A.append(divisors_x[i])

	for i in range(0,len(divisors_y)):
		for j in range(0, pow_y[i]):
			B.append(divisors_y[i])


	counter_A = Counter(A)
	counter_B = Counter(B)


	C = list((counter_A - counter_B).elements())

	if len(C)>0:
		from functools import reduce
		import operator
		product = reduce(operator.mul, C)
		print('{} dividied by {} is:'.format(x,y))
		return product

	else:
		return print('{} is not divisible by {}'.format(x,y))



if __name__ == "__main__" :
    x = sys.argv[1]
    y = sys.argv[2]
    #print(x,y)
    print(divisibility_check_new(x))
    #print(divisibility_check_new(y))
    print(division(x,y))
