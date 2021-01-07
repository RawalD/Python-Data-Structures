def sum_numbers(num):

    # Base case
    if len(str(num)) == 1:
        return num

    # Recursion
    else:
        return num % 10 + sum_numbers(num / 10)


print(sum_numbers(432))
