def list_pair(num_list, number):

    pairs = 0

    for num in range(0, len(num_list)):

        for sec_num in range(num + 1, len(num_list)):

            if num_list[num] + num_list[sec_num] == number:

                pairs += 1

    return pairs


print(list_pair([1, 3, 2, 2], 4))
