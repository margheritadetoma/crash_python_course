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
        a list with the Fibonacci sequence

    '''

    fib_seq = [0, 1]

    if int(n) < 0:
        print('Error: {} < 0'.format(n))
    
    elif n==0:
        return [0]
    
    elif n==1:
        return fib_seq
    
    
    while True:
        new_term = fib_seq[-1] + fib_seq[-2]
        if new_term > int(n):
            return fib_seq
        fib_seq.append(new_term)





def test_odd(input_list):
    '''
    Take only the odd elements of the input list.

    Parameters
    ----------
    input_list : list 
        Input list to be tested

    Returns
    -------
    odd_elements: list
        a list of the odd elements
        contained in input_list

    '''

    odd_elements = [elem for elem in input_list if elem % 2 != 0]

    return odd_elements




def test_even(input_list):
    '''
    Take only the even elements of the input list.

    Parameters
    ----------
    input_list : list 
        Input list to be tested

    Returns
    -------
    even_elements: list
        a list of the even elements
        contained in input_list

    '''

    even_elements = [elem for elem in input_list if elem % 2 == 0]

    return even_elements





if __name__ == "__main__":
    n = sys.argv[1]
    print("Fibonacci sequence up to {}:".format(n))

    fib_list = fibonacci(n)
    
    print(fib_list)
    print('Even numbers of {} is: {}'.format(fib_list, test_even(fib_list)))
    print('Odd numbers of {} is: {}'.format(fib_list, test_odd(fib_list)))

