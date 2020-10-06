# Isabella Gomez A15305555
# ECE143 HW 1

# Instructions:
# Write a function that computes the sum of all non-negative
# integers (i.e. >=0) up to and including a specified value, n.


##############################################################################
# will make the sum of all non negative numbers from 0 up to n value         #
##############################################################################
def compute_sum_to_n(n):

    # make sure n is non-negative integer
    assert type(n) == int
    assert n >= 0

    # make the non-negative sum
    sum = 0
    while n != 0:
        sum = sum + n
        n = n - 1

    return sum
