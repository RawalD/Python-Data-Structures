def check_unique(string):

    uniques = set()

    for char in string:
        if char in uniques:
            return False
        else:
            uniques.add(char)
            # print(uniques)
    return True


print(check_unique(""))
print(check_unique("goo"))
print(check_unique("abcdefg"))
