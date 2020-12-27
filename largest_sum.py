'''
Take an aray with positive and negative integers and find the largerst continous sum of the array.
'''

def largest(arr):
    # check for empty array
    if len(arr) == 0:
        return 0
    # For 1 element in the array 
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        # store the largest of the 2 sums
        max_sum = max(current_sum, max_sum)
    return max_sum

print(largest([3,-1, -1, -1, 2]))
