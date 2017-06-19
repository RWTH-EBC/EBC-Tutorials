#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import pytest

#  ATTENTION: Regulary, you should NOT copy the code, but import the module
#  to access the function, you would like to test. We only copy the code for
#  the purpose of demonstration.

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


class Test_Squaring(object):
    """
    I am a test class for example_1.py based on pytest
    """

    def test_positve_int(self):
        """
        Testing method for positive integer inputs
        """
        assert square_int_number(2) == 4

    def test_zero(self):
        """
        Testing method for input zero
        """
        assert square_int_number(0) == 0

    def test_negative_int(self):
        """
        Testing method for negative integer inputs
        """
        assert square_int_number(-2) == 4
