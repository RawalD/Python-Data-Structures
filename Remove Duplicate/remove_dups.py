# def removeDuplicates(nums_list):

#     if len(nums_list) == 0 or len(nums_list) == 1:
#         return nums_list

#     new_list = []

#     for el in nums_list:
#         if el not in new_list:
#             new_list.append(el)

#     return new_list


# print(removeDuplicates([1, 1, 2, 4]))

# print(removeDuplicates([4, 1, 1, 9]))

# print(removeDuplicates([1]))

# Return lenght of modified array
def removeDuplicates(nums_list):

    if nums_list == 0:
        return 0
    elif nums_list == 1:
        return 1

    el = 1

    for el_two in range(1, len(nums_list)):

        if (nums_list[el_two] != nums_list[el]):
            el += 1
            nums_list[el] = nums_list[el_two]

    return el + 1


print(removeDuplicates([4, 1, 1, 9]))
print(removeDuplicates([4, 1, 1, 9, 9, 9, 7]))
