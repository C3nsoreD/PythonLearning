"""Given an array, rotate the array to the right by k steps, where k is non-negative."""
def solution_one(nums, k):
    for _ in range(k):
        previous = nums[-1]
        for i in range(len(nums)):
            nums[i], previous = previous, nums[i]
            
    return nums

def solution_two(nums, k):
    n = len(nums)

    temp_arr = [0] * n
    for i in range(n):
        temp_arr[(i +  k) % n] = nums[i]

    nums[:] = temp_arr
    return nums

def soultion_three(nums, k):
    n = len(nums)
    k %= n
    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1
            print(current) # test 
            if start == current:
                print("breaiking %s" % current) # test 
                break
        start += 1



array = [1, 2, 1, 4, 9, 0]
print(soultion_three(array, 2))