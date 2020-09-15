# -*- coding: utf-8 -*-
"""RTS Labs Code Exercises

Author: Brandon Simmers

This module serves as a response to the RTS Labs Code Exercise.
Exercises #1 and #2 are demonstrated in the code, and the response
to exercise #3 is shown in the docstring at the end.

Prompt:
    #1  Print the number of integers in an array that are above the given input
    and the number that are below, e.g. for the array [1, 5, 2, 1, 10] with input 6,
    print “above: 1, below: 4”.

    #2  Rotate the characters in a string by a given input and have the overflow
    appear at the beginning, e.g. “MyString” rotated by 2 is “ngMyStri”.

    #3  If you could change 1 thing about your favorite framework/language/platform
    (pick one), what would it be?

    Let us know if you have any questions!
    If you're good to go, please send us back your exercise at your convenience
    (please upload your response to a public git repository, such as Github).


Example (Python 3):
    $ python code_exercise.py
"""

def prompt_user_for_int(prompt):
    """Prompts for the user's input and checks if an integer

    Args:
        prompt: A sentence to prompt the user to input an integer.

    Returns:
        num_in: The entered integer.
    """
    valid_input = False
    while not valid_input:
        num_in = input(prompt)
        try:
            num_in = int(num_in)
            valid_input = True
        except ValueError:
            print('Invalid input. Please only input an integer.')

    return num_in

def compare_int_to_array(num_in, my_array):
    """ Counts the amount of numbers in the array above and below the input integer

    Args:
        num_in: A given integer.
        my_array: An array of integers.

    Returns:
        above: The amount of integers in the array above the input integer.
        below: The amount of integers in the array below the input integer.
    """
    above, below = (0, 0)
    for num in my_array:
        if num < num_in:
            below += 1
        elif num > num_in:
            above += 1
        else:
            continue

    return above, below

def rotate_string(rotate_amount, my_string):
    """Rotates a given string by the input amount

    Args:
        rotate_amount: A given integer
        my_string: A string

    Returns:
        result: The rotated string.
    """

    # string repeats after rotating the length of the string,
    # so get the remaining rotations after the repeats
    new_rotate_amount = rotate_amount % len(my_string)

    # splits string starting from the right and going left input number of spaces
    first_part = my_string[-new_rotate_amount:]
    second_part = my_string[:-new_rotate_amount] # splits remaining characters
    result = first_part + second_part # adds overlap to beginning of string

    return result

if __name__ == '__main__':
    MY_ARRAY = [1,5,2,1,10]
    MY_STRING = "MyString"

    # First exercise
    input_number = prompt_user_for_int('Please input an integer to compare to the array: ')
    num_above, num_below = compare_int_to_array(input_number, MY_ARRAY)
    print(f'above: {num_above}, below: {num_below}')

    # Second Exercise
    input_number = prompt_user_for_int('Please input an integer amount to rotate MyString: ')
    new_string = rotate_string(input_number, MY_STRING)
    print(new_string)

    """ Third Question Answer
    In the past, when using Django, I've run into issues using their Sites model from
    django.contrib.sites.models. After a successful database migration the first time,
    I have to manually remove sites from future migration files so it will stop throwing
    a ValueError saying it is unable to serialize the website. I'd like to change that to
    check if the Site has previously been successfully serialized to curcumvent this issue.
    """
