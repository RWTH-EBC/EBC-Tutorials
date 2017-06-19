#  I am a function (defined by 'def')
def square_int_number(number):
    """
    Returns squared value of input number.

    Parameter
    ---------
    number : int
        Integer input value

    Returns
    -------
    squared_nb : int
        Squared integer output value

    Examples
    --------
    >>> square_int_number(2)
    4
    >>> square_int_number(0)
    0
    >>> square_int_number(-2)
    4
    """
    #  Assert function. Checks if input parameter is of type integer
    assert isinstance(number, int), 'Input is not of type integer!'
    squared_nb = number ** 2  # Square input number
    return squared_nb

if __name__ == '__main__':
    #  Execute function
    input_number = 2  # Input parameter
    #  Function call
    result_number = square_int_number(input_number)
    #  Print statement
    print('Squared number is:', result_number)
