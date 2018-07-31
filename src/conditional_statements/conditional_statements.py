def exchange_values(a, b):
    '''
    Write an if-statement that takes two integer variables and exchanges
    their values if the first one is greater than the second one.
    :param a:
    :param b:
    :return:
    '''

    if a > b:
        a = a - b
        b = a + b
        a = b - a

    nums = [a, b]

    return nums


def find_biggest_from_three(a, b, c):
    '''
    Write a program that finds the biggest of three integers, using nested
    if statements.
    :param a:
    :param b:
    :param c:
    :return:
    '''
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return 0
