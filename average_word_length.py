# Isabella Gomez A15305555
# ECE143 HW 1

# Instructions:
# Write a compute_average_word_length(instring,unique=False) function
# to compute the average length of the words in the input string
# (instring). If the unique option is True, then exclude duplicated
# words. For example, in the example input text above, the word 'the'
# should be counted exactly once for the average word length if
# unique=True. Note that the words are case sensitive. Remember to
# carefully validate your inputs using assert statements.

##############################################################################
# Will compute the average word length of an input string. It will exclude   #
# duplicated words in its calculation.                                       #
##############################################################################
def compute_average_word_length(instring,unique=False):

    # check type string and that string is not empty with assert
    assert type(instring) == str
    assert len(instring) >= 1

    # split string by spaces into a list of words
    list_duplicates = instring.split()

    # check that instring actually has words
    assert len(list_duplicates) >= 1

    # remove duplicates by making it a set if unique is true
    if unique:
        split_string = set(list_duplicates)
    else:
        split_string = list_duplicates

    # add the word lengths together into sum_of_lengths
    sum_of_lengths = 0
    for word in split_string:
        word_length = len(word)
        sum_of_lengths = word_length + sum_of_lengths

    # make sure I am not dividing by zero
    assert len(split_string) != 0

    # calculate the average by dividing sum_of_lengths by amount of words
    average_word_length = sum_of_lengths / len(split_string)

    return average_word_length

