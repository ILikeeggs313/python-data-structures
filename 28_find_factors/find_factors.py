def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    num_list = [n for n in range(1,num// 2+ 1) if num % n == 0]
    num_list.append(num)
    return num_list

    #another way is to use a loop
    # factors = []
    # while(n <= num):
    #     if num % n == 0:
    #         factors.append(num)
    #     n += 1
    # return factors
