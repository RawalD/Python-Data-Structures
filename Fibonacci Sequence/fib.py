"""
Nth Fibonacci

"""


def getNthFib(n):
    # One of three known fibonacci sequences
    if n == 2:
        return 1
    # One of three known fibonacci sequences
    elif n == 1:
        return 0
    # One of three known fibonacci sequences
    else:
        # Else return recursively nth - 1 + nth - 2
        return getNthFib(n - 1) + getNthFib(n - 2)


print(getNthFib(1))
print(getNthFib(2))
print(getNthFib(3))
print(getNthFib(4))
print(getNthFib(5))
