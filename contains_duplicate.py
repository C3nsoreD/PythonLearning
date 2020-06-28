def contains(nums):
    # check if the array is empty   
    if len(nums) == 0:
        return False

    # Sort the array of integers 
    nums.sort()

    start = nums[0]
    
    for i in range(1, len(nums)):
        # compare the elemnents for equality
        if nums[i] == start:
            return True
        else:
            # change the start position
            start = nums[i]
    
    return False


def checkDuplicate(array):
    # create a frequecny
    count = {}
    # iiterate over the list 
    for item in array:
        # check the frequncy of each item
        if item not in count:
            count[item] = 1
        else:
            return True

    return False


print(checkDuplicate([1, 2, 1, 3, 5]))
