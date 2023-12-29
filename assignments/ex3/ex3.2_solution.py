import sys

def fibonacci(n):

    '''
    A function that calculates the Fibonacci sequence up to the n-th term

    Parameters
    ----------
    n : int 
        the n-th term of the sequence

    Returns
    -------
    fib_sew: list
        a list with the Fibonacci sequenc

    '''

    fib_seq = [0, 1]

    while (len(fib_seq) < int(n)):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])


    return fib_seq


if __name__ == "__main__":
    n = sys.argv[1]
    print("Fibonacci sequence up to {}:".format(n))
    print(fibonacci(n))

