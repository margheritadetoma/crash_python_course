import sys

def prime_numbers_Eratosthenes(n):
	
	'''
    A function that finds the list of prime integer numbers smaller than 100

    Parameters
    ----------
    n : int 
        the n-th term of the sequence

    Returns
    -------
    fib_sew: list
        a list with the Fibonacci sequence

    '''


	from collections import Counter
	import numpy as np

	prime_numbers = list(np.arange(2, n+1))



	index = 0

	if n>=2:
		while index < n:
			step = prime_numbers[index]

			to_be_deleted = list(np.arange(2*step, n+1, step))
			if len(to_be_deleted)==0:
				return prime_numbers

			# Find the complement of the intersection
			prime_numbers = [x for x in prime_numbers if x not in set(prime_numbers) & set(to_be_deleted)]

			#find the new start
			index = prime_numbers.index(step) + 1
			

		return prime_numbers


	elif n>100:
		print('Error: {} > 100'.format(n))
		return 

	elif n<2:
		print('No prime numbers < {}'.format(n))
		return 






if __name__ == "__main__":
	n = int(sys.argv[1])
	print(prime_numbers_Eratosthenes(n))




