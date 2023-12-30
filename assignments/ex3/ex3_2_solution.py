import sys

def fibonacci(n: int):

    '''
    A function that calculates the Fibonacci sequence up to the n-th term

    Parameters
    ----------
    n : int 
        n-th term of the sequence

    Returns
    -------
    fib_sew: list
        a list with the Fibonacci sequence

    '''

    fib_seq = []

    if n <= 0:
        print(f'Error: {n} < 0')
    
    
    for i in range(n):
        if i==0 or i==1:
            fib_seq.append(1)
            continue
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq





def test_odd(input_list):
    '''
    Take only the odd index values of the input list.

    Parameters
    ----------
    input_list : list 
        Input list to be tested

    Returns
    -------
    odd_index_elements: list
        a list of the odd index elements

    '''
    

    return input_list[::2]




def test_even(input_list):
    '''
    Take only the even index values of the input list.

    Parameters
    ----------
    input_list : list 
        Input list to be tested

    Returns
    -------
    even_index_elements: list
        a list of the even index elements

    '''
    

    return input_list[1::2]





if __name__ == "__main__":
    n = int(sys.argv[1])
    print(f"Fibonacci sequence up to the {n}-th term:")

    fib_list = fibonacci(n)
    print(fib_list)
    
    print(test_odd(fib_list))
    print(test_even(fib_list))

