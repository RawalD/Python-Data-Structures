def compress_string(string):

    return_string = ""
    length = len(string)

    if length == 0:
        return ''

    if length == 1:
        return f"{string}1"

    count = 1
    el = 1

    while el < length:
        if string[el] == string[el-1]:
            count += 1

        else:
            return_string = f"{return_string + string[el-1]}{count}"
            count = 1

        el += 1
    return_string = f"{return_string + string[el-1]}{count}"

    return return_string


print(compress_string('AABBCC'))
print(compress_string('AAABCCDDDDD'))
