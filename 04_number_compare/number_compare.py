def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a > b:
        return f'first{a} is greater than second {b}'
    if a < b:
        return f'second{b} is greater than first{a}'
    if a == b:
        return f'numbers are equal'

number_compare(1, 1)