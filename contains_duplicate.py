"""
Problem: Write a function that checks if array A contains ducplicates.
Two implementations of check_duplicates function

"""
def contains(nums):
    # check if the array is empty   
    if len(nums) == 0:
        return False
    # Sort the array of integers 
    nums.sort()
    start_index = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == start_index:
            return True
        else:
            start_index = nums[i]    
    return False


def checkDuplicate(array):
    # Solved using a heah table /frequency table 
    count = {}
    # iiterate over the list 
    for item in array:
        # check if the item already exists in table
        if item in count:
            return True, count
        else:
            count[item] = 1
    return False


print(checkDuplicate([1, 2, 1, 3, 5]))
# print(contains([1, 2, 1, 3, 5]))
