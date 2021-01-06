def anagram(one, two):

    # Removes spaces and lower cases
    one = one.replace(" ", "").lower()
    two = two.replace(" ", "").lower()

    # If length of the first is not the same as the second immediate return False
    if len(one) != len(two):
        return False

    else:
        # Create counter variable and set to empty dictionary
        counter = {}

        # For every letter in first word
        for letter in one:
            # If the letter is in the counter dictionary then add letter to counter with an additional one
            if letter in counter:
                # If the letter exists then add one to the key
                counter[letter] += 1
            # Else set the counter[letter] to a just 1
            else:
                counter[letter] = 1

        for letter in two:
            if letter in counter:
                counter[letter] -= 1
            else:
                counter[letter] = 1

        # If letter in counter is not equal to 0 then return false
        for letter in counter:
            if counter[letter] != 0:
                return False

    return True


print(anagram('dog', 'god'))
print(anagram('aa', 'bb'))
print(anagram('clint eastwood', 'old west action'))

# Simplified version


def anagram_two(one, two):

    # Removes spaces and lower cases
    one = one.replace(" ", "").lower()
    two = two.replace(" ", "").lower()

    return sorted(one) == sorted(two)


print(anagram_two('dog', 'god'))
print(anagram_two('aa', 'bb'))
print(anagram_two('clint eastwood', 'old west action'))
