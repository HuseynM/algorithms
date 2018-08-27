def print_to_N():
    '''
    Write a program that prints on the console the numbers from 1 to N.
    The number N should be read from the standard input.
    :return:
    '''

    n = int(input('Enter value: '))

    for i in range(0, n):
        print('Hello world')


def print_not_divisible_by_3_7():
    '''
    Write a program that prints on the console the numbers from 1 to N,
    which are not divisible by 3 and 7 simultaneously. The number N
    should be read from the standard input.
    :return:
    '''

    n = int(input('Enter value: '))

    for i in range(0, n):
        if i % 3 != 0 and i % 7 != 0:
            print(i)


def find_smallest():
    '''
    Write a program that reads from the console a series of integers and
    prints the smallest of them.
    :return:
    '''

    n = int(input('Enter count: '))
    arr = []
    min = 0

    for i in range(0, n):
        j = int(input('Enter value: '))
        arr.append(j)
        if min > j:
            min = j

    return min


def find_largest():
    '''
    Write a program that reads from the console a series of integers and
    prints the largest of them.
    :return:
    '''
    n = int(input('Enter count: '))
    arr = list()
    max = 0

    for i in range(0, n):
        j = int(input('Enter value: '))
        arr.append(j)
        if max < j:
            max = j

    return max


def fibonacci(n):
    '''
    the first N members of the Fibonacci sequence:
    :param n:
    :return:
    '''
    a = 0
    b = 1

    for i in range(0, n):
        temp = a
        a = b
        b = temp + b

    return a


def sum_of_fibonacci(n):
    '''
    Write a program that reads from the console number N and print the sum
    of the first N members of the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8,
    13, 21, 34, 55, 89, 144, 233, 377, …
    :param n:
    :return:
    '''
    sum = 0
    for i in range(0, n):
        sum += fibonacci(i)

    return sum


def factorial(n):
    '''
    Write a program that calculates N!
    :param n:
    :return:
    '''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_1(n, k):
    '''
    Write a program that calculates N!/K! for given N and K (1<K<N).
    :param n:
    :param k:
    :return:
    '''
    if n > k > 1:
        return factorial(n) / factorial(k)


def factorial_2(n, k):
    '''
    Write a program that calculates N!*K!/(N-K)! for given N and K
    (1<K<N).
    :param n:
    :param k:
    :return:
    '''
    if n > k > 1:
        return factorial(n) * factorial(k) / factorial(n - k)
