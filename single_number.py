def solution(nums):
    dict_nums = {}
    value = 0
    for i in range(len(nums)):
        if nums[i] not in dict_nums:
            dict_nums[nums[i]] = 1
        else:
            dict_nums[nums[i]] += 1

    print(dict_nums)
    for k, v in dict_nums.items():
        if v <= 1:
            return value
        
    # return value

arr = [1, 2, 2, 3, 3]
print(solution(arr))