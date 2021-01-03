# Implementing binary search

# The list of things must be sorted in order to implement binary search

"""
Example list
[0,1,21,33,45,45,61,71,72,73]

Step one: Split the list into the middle

Step two: Create L and R pointer (the first and last element in the list)

Step three: Grab the INDEX of these numbers

Step four: Middle = 0 + 9 // 2
The first element and the last element (this will ofcourse vary) then do integer division
Middle would then equal to 4
4th element in the list
[45]

Step five: Is M greater than or less then R pointer ?
If so we move our right pointer behind the middle ground as chances of the number being there are higher

Step six:
[0,1,21,33,45,45,61,71,72,73]
            ---------------- Eliminated all these numbers as choices
Recalculate the middle ground in the range
[0,1,21,33]
L        R
Middle = (0 + 3) // 2
Middle = 1
Middle = [1]

Step seven: Is number searched for greater than or less than middle
In this case greater than
Move L pointer AHEAD of middle ground to eliminate other choices
[0,1,21,33]
   M  L  R

Step eight:
New middle ground
Middle = (2 + 3) // 2
Middle = [21]

Step nine:
Is number checked for less than or greater than middle ground
In this case no so L pointer moves forward
L and R are overlapping

Keep calculating middle ground and eliminating list elements
When L is greater than R , number has not been found

Time = O(log(N))
Eliminating half the input at every middle point
Space = Binary should be iterative O(1)
"""

"""
def binary_search(lst, number):

    # Implement recursion
    return binary_search_helper_func(lst, number, 0, len(lst) - 1)


def binary_search_helper_func(lst, number, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    check_if_target = lst(middle)

    if number == check_if_target:
        return middle

    elif number < check_if_target:
        # Move right pointer to behind the middle element
        return binary_search_helper_func(lst, number, left, middle - 1)

    else:
        # Move left pointer to infront of middle element
        return binary_search_helper_func(lst, number, middle + 1, right)

# Iterative is the preffered way of using Binary search.
# Will prevent memory stack filling up with the use of recursion
# Recursion unnessary here either way
"""


def binary_search(lst, number):
    # Arguments: The list, the number to check against, left-most [0] element, right-most [last-element]
    return binary_search_helper(lst, number, 0, len(lst) - 1)


def binary_search_helper(lst, number, left, right):
    # While the left most element is less than or equal to the right keep loop running
    while left <= right:
        #middle is found
        middle = (left + right) // 2
        # set possible matching number
        match = lst[middle]

        if number == match:
            return middle
        elif number < match:
            # Move the middle element back one, eliminating half the list
            right = middle - 1
        else:
            # Move the element front one, eliminating half the lsit
            left = middle + 1

    # Outside of while loop
    return -1


print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 70))  # -1

print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 355))  # 10

print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 354))  # -1

print(binary_search([1, 5, 23, 111], 3))  # -1

print(binary_search([1, 5, 23, 111], 1))  # 0

print(binary_search([4, 5, 1, 451, 200], 1))  # 2
