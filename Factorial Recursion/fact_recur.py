def fact(n):

    # Base case
    if n == 0:
        return 1

    # Recursion call
    else:
        return n * fact(n-1)
