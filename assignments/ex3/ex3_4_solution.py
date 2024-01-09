import sys


def prime_numbers_eratosthenes(n, n_max=100):
    
    '''
    Finds the list of prime integer numbers smaller than 100

    Parameters
    ----------
    n : int 
        the n-th term of the sequence

    Returns
    -------
    fib_seq: list
        a list with the Fibonacci sequence
    '''

    if n < 2:
        print(f'No prime numbers < {n}')
        return 

    if n > n_max:
        print(f'Error: {n} > {n_max}')
        return


    prime_numbers = list(range(2, n+1))

    index = 0
    while index < len(prime_numbers):
        prime = prime_numbers[index]

        aux_index = index + 1
        while aux_index < len(prime_numbers):
            if prime_numbers[aux_index] % prime == 0:
                del prime_numbers[aux_index]
            else:
                # increment index only if no elements deleted
                aux_index += 1

        index += 1
        
    return prime_numbers


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(prime_numbers_eratosthenes(n))
