def contains(nums):
    nums.sort()
    
    if len(nums) == 0:
        return False

    prev = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == prev:
            return True
        else:
            prev = nums[i]
    
    return False


def checkDuplicate():
    count = {}
    for item in lst:
        if item not in count:
            count[item] = 1
        else:
            return True
    return False