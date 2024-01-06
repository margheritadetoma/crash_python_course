import sys
from assignments.ex3.ex3_4_solution import prime_numbers_eratosthenes


def decomposition_prime_factors(n):

    '''
    A function that finds the decomposition
    in prime factors of a positive integer number.

    Parameters
    ----------
    n : int
        a positive number

    Returns
    -------
    decomposition: list
        decomposition
        in prime factors

    '''

    if not isinstance(n, int):
        raise ValueError('n must be an int')

    if n==1:
        print('Warning: n=1 has no decomposition in prime numbers. Returning [1]')
        return [1]


    prime_numbers = prime_numbers_eratosthenes(n)
    decomposition = []

    for prime_num in prime_numbers:
        while n%prime_num==0:
            decomposition.append(prime_num)
            n = n / prime_num

    return decomposition




def check_decomposition(decomposition, n):
    n = int(n)

    '''
    A function that test if the decomposition
    in prime numbers is correct.

    Parameters
    ----------
    decomposition: list
        a list of the prime numbers decomposition to test

    n: int
        the number that has been decomposed


    Returns
    -------
    boolean: True/False
        True: correct decomposition
        False: uncorrect decomposition
    '''


    product = 1
    for i in range(0, len(decomposition)):
        product = product *  decomposition[i]

    if product==n:
        print('Correct decomposition')
        return True

    else:
        print('Uncorrect decomposition')
        return False











if __name__ == "__main__":
    n = int(sys.argv[1])

    print('Decomposition of {} in prime factors:'.format(n))
    decomposition = decomposition_prime_factors(n)
    print(decomposition)

    #Check the decomposition
    print('Decomposition test result:')
    check_decomposition(decomposition, n)
    







