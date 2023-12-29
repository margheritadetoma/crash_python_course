import sys

def sieve_of_Eratosthenes(n):
	n = int(n)

	from collections import Counter
	import numpy as np

	prime_numbers = list(np.arange(2, int(n)+1, 1))

	index = 0

	if n>2:
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


	else:
		return [2]


if __name__ == "__main__":
	n = sys.argv[1]
	print(sieve_of_Eratosthenes(n))




