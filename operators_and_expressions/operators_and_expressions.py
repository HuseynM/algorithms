def is_odd_or_even(n):
    '''
     Write an expression that checks whether an integer is odd or even.
    :param n:
    :return:

    0001 - 1
    '''
    return "even" if (n & 1) == 0 else "odd"


def is_divisible_both_divisor(n, divisor1, divisor2):
    '''
    Write a Boolean expression that checks whether a given integer is
                divisible by both divisor1 and divisor2, without a remainder.
    :param n:
    :param divisor1:
    :param divisor2:
    :return:
    '''
    return n % divisor1 == 0 and n % divisor2 == 0

