import sys


def divisibility_check(n: int) -> list[int]:

	'''
	Checks of the integer value from input is
	divisible by 2,3,5 or 7.

    Parameters
    ----------
    n : int
        a number

    Returns
    -------
    divisors : list
    	list of divisors

    '''

	divisors = [2, 3, 5, 7]  # Divisors to be checked
	divisible_by = []

	for div in divisors:
		if n % div == 0:  # If this is true, n is divisible by div
			print(f'{n} is divisible by {div}')
			# Append div to the list of divisible numbers
			divisible_by.append(div)


	return divisible_by



def division(x, y):

	'''
	Checks if x is divisible by y

	Parameters
    ----------
    x : int
        a number
    y : int
        a number

    Returns
    -------
    bool :
    	True if divisible
    	False if not divisible
	'''

	if x%y==0:  # Check if x is divisible by y
		print(f'{x} is divisible by {y}')
		return True
	if y%x==0:  # Check if y is divisible by x
		print(f'{y} is divisible by {x}')
		return True
	else: 
		print(f'{x},{y} are not divisible by each other')
		return False





if __name__ == "__main__" :
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(divisibility_check(x))
    print(divisibility_check(y))
    print(division(x,y))
