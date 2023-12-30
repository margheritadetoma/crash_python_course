import sys


def divisibility_check(n: int) -> list[int]:

	'''
	Check of the integer value from input is
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


	divisors = [2, 3, 5, 7]
	divisible_by = []

	for div in divisors:
		if n%div==0:
			print(f'{n} is divisible by {div}')
			divisible_by.append(div)


	return divisible_by






def division(x, y):

	'''
	Function that checks if x is divisible by y.

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

	if x%y==0:
		print(f'{x} is divisible by {y}')
		return True
	if y%x==0:
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
