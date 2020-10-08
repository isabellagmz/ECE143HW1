# Isabella Gomez A15305555
# ECE143 HW 1

# Instructions:
# Write a function that takes a single string character (i.e., 'a','b','c')
# as input and returns True or False if that character represents a valid
# integer in base 10.


##############################################################################
# Will take an input of a single character string and return True if it is a #
# base 10 integer.                                                           #
##############################################################################
def is_string_integer(input_string):

    """check if input is string and single character string"""
    assert isinstance(input_string, str)
    assert len(input_string) == 1

    # return true if it is digit, false if it is not digit
    if input_string.isdigit():
        return True
    else:
        return False

