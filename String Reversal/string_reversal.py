def reverse_string(string):

    if len(string) == 0:
        return "Empty String"

    string = string.strip()

    string = string.split(" ")

    return_string = string[::-1]

    return return_string


print(reverse_string("  space here"))
