def fibonacci(n):
    """
    Return the nth value of the Fibonacci sequence.
    e.g., fibonacci(8) = 13
    """
    # Invalid input
    if n < 0:
        return "Invalid input"
    # Base cases
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    # All other cases
    else:
        # Recursively call the fibonacci command.
        return fibonacci(n-2) + fibonacci(n - 1)


def lucas(n):
    """
    Return the nth value of the Lucas numbers.
    e.g., lucas(5) = 11
    """
    # Invalid input
    if n < 0:
        return "Invalid input"
    # Base cases
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    # All other cases
    else:
        return lucas(n-2) + lucas(n-1)


def sum_series(n, a = 0, b = 1):
    """
    Calling this function with no optional parameters will produce values
    from the Fibonacci series.
    e.g., sum_series(3) -> fibonacci(3) -> 2

    Calling this function with optional arguments 2 and 1 will produce
    values from the Lucas numbers.
    e.g., sum_series(3, 2, 1) -> lucas(3) -> 4

    Calling this function with optional arguments that differ from the above
    will produce values from other series.
    e.g., sum_series(3, 5, 3) -> 11
    """
    # # Fibonacci case
    # if a == 0 and b == 1:
    #     fibonacci(n)
    # # Lucas case
    # elif a == 2 and b == 1:
    #     lucas(n)
    # # All other cases
    # else:
    # Invalid input
    if n < 0:
        return "Invalid input"
    # All other cases
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n - 2, a, b) + sum_series(n - 1, a, b)
