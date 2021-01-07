def integer_add(num):

    if num == 0:
        return 0

    else:
        return num + integer_add(num - 1)


print(integer_add(4))
