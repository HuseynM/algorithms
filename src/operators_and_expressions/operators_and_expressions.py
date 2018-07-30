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
    Prints on the console the number in reversed order: abcd-dcba
    :param n:
    :return:
    '''

    reversed = 0
    while n > 0:
        reversed *= 10
        reversed += n % 10
        n = n // 10
    return reversed


def get_digit_count(n):
    '''
    Get count of given number
    :param n:
    :return:
    '''

    i = 0
    while n > 0:
        n = n // 10
        i = i + 1
    return i


def put_last_in_first(n):
    i = get_digit_count(n)
    _local = n % 10
    _local *= pow(10, i - 1)
    _local += n // 10

    return _local


def exchange_digits(n):
    '''
    Exchanges the second and the third digits: abcd->acbd (right to left)
    :param n:
    :return:
    '''

    second_digit = (n // 10) % 10
    third_digit = (n // 100) % 10

    n = n - third_digit * 100
    n = n + second_digit * 100

    n = n - second_digit * 10
    n = n + third_digit * 10

    return n


def print_bit_position(n, p):
    '''
    We are given a number n and a position p. Write a sequence of
    operations that prints the value of the bit on the position p in the
    number (0 or 1). Example: n=35, p=5 -> 1. Another example: n=35,
    p=6 -> 0.
    :param n:
    :param p:
    :return:
    '''

    bit = n & (1 << (p - 1))
    return 0 if bit == 0 else 1


def check_bit_position(n, p):
    '''
    Write a Boolean expression that checks if the bit on position p in the
    integer v has the value 1. Example v=5, p=1 -> false.
    :param n:
    :param p:
    :return:
    '''

    bit = n & (1 << (p - 1))
    return False if bit == 0 else True


def change_bit_position(n, v, p):
    '''
    We are given the number n, the value v (v = 0 or 1) and the position p.
    write a sequence of operations that changes the value of n, so the bit on
    the position p has the value of v. Example: n=35, p=5, v=0 -> n=3.
    Another example: n=35, p=2, v=1 -> n=39.
    :param n:
    :param v:
    :param p:
    :return:
    '''

    return n | (1 << (p - 1)) if v == 1 else n & ~(1 << (p - 1))











