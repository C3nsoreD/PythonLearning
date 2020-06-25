'''
Take an aray with positive and negative integers 
and find the largerst continous sum of the array
'''

def largest(arr):
    # check empty 
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


print(largest([1, 2, -1, -3, 12, 4, -5, 21, 3]))
