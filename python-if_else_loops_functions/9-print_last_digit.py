#!/usr/bin/python3
def print_last_digit(number):

    mdl_neg = number % -10 * -1
    mdl_pos = number % 10

    if number > 0:
        print(mdl_pos, end="")
        return mdl_pos
    elif number == 0:
        print(mdl_pos, end="")
        return mdl_pos
    elif number < 0:
        print(mdl_neg, end="")
        return mdl_neg
