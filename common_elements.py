"""
Common elements in two sorted arrays
    return the common elements as an array between 2 sorted arrays of integers
"""


def common_elements(a, b):
    """
    Using the pointer approach
    """
    # assign indexes for both arrays

    i, j = 0, 0

    result = []
    # compare the lengths
    while i < len(a) and j < len(b):
        # check commonality
        if a[i] == b[i]:
            # appenc/add the final list if true
            result.append(a[i])
            i += 1
            j += 1
        # if element in a is larger than b move position in b
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1

    return result


print(common_elements([1,0,3,6,4], [1,2,3,5,9,0]))
