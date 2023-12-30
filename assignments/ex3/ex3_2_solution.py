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
        if i==0 or i==1: #first two numbers are: 1 and 1
            fib_seq.append(1)
            continue
        fib_seq.append(fib_seq[-1] + fib_seq[-2]) #append new term with Fibonacci rule

    return fib_seq





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
    

    return input_list[::2] #only element with even index (0, 2, 4,..)




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
    

    return input_list[1::2]  #only element with even index (1, 3, 5,..)





if __name__ == "__main__":
    n = int(sys.argv[1])
    print(f"Fibonacci sequence up to the {n}-th term:")

    fib_list = fibonacci(n)
    print(fib_list)

    print('Element with odd index:')
    print(test_odd(fib_list))

    print('Element with even index:')
    print(test_even(fib_list))

