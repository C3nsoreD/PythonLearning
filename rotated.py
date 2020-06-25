'''
Given 2 arrays is 1 array a rotation of another return True/False
same size and elements but start index is different
BigO(n) we are going through each arrays 2x but O(n) = O(n) since infinite sized lists,
constants means nada

'''

def rotate(list1, list2):
    # Assuming that list1 is sorted
    # Check if the lists are the same size
    if len(list1) != len(list2):
        return False

    key = list1[0]
    key_index = 0
    # loop over list2 and check which index contains the key
    for i in range(len(list1)):
        if list2[i] == key:
            key_index = i
            break

    if key_index == 0:
        return False

    for x in range(len(list1)):
        list2_index = (key_index + x) % len(list1)
        if list1[x] != list2[list2_index]:
            return False
    return True


print(rotate([1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3]))
