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


def check_third_digit(n):
    '''
    Write an expression that looks for a given integer if its third digit (right
    to left) is 7.
    1570
    :param n:
    :return:
    '''
    return (n // 100) % 10 == 7


def check_third_bit(n):
    '''
    Write an expression that checks whether the third bit in a given integer
    is 1 or 0.
    :param n:
    :return:
    ..0100 = 4
    '''
    return 0 if (n & 0B100) == 0 else 1


def sum_of_digits(n):
    '''
     Calculates the sum of the digits (in our example 2+0+1+1 = 4)
    :param n:
    :return:
    '''
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10

    return sum


def reverse(n):
    '''
    Prints on the console the number in reversed order: dcba
    :param n:
    :return:
    '''

    reversed = 0
    while n > 0:
        reversed *= 10
        reversed += n % 10
        n = n // 10
    return reversed

print(reverse(1234))
