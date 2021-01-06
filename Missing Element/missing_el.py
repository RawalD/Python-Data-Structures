def missingElement(arr_one, arr_two):

    # Our counter
    num = 0

    # Add all the numbers in array one
    for n in arr_one:
        num += n

    # Now subtract all the numbers
    for n in arr_two:

        num -= n

    return f"Missing number is {num}"


arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]
print(missingElement(arr1, arr2))

arr1 = [5, 5, 7, 7]
arr2 = [5, 7, 7]
print(missingElement(arr1, arr2))

arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]
print(missingElement(arr1, arr2))

arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
arr2 = [9, 8, 7, 5, 4, 3, 2, 1]
print(missingElement(arr1, arr2))
