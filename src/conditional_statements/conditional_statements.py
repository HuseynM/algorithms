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

