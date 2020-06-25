def function_two(s):
    """
    Do not return anything, modify s in-place instead.
    """
    # 2 pointer approach
    first = 0
    last = len(s) - 1

    while first < last:
        s[first], s[last] = s[last], s[first]
        first, last = first + 1, last - 1


def function_one(s):
    """ example: 'this is a normal string' """
    i = 0

    spaces = [' ']
    length = len(s)
    words = []
    # Rebuild the immutable string to a list
    while i < length:
        if s[i] not in spaces:
            start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[start:i])
        i += 1  # Change starting position

    return ' '.join(words[::-1])


print(function_one('this is a normal string'))

# print(function_two('this is a normal string'))