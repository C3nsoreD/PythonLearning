# A naive Python implementation of LIS problem

"""
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence 
 of a given sequence such that all elements of the subsequence are sorted in increasing order.
"""

global maximun

def _lis(arr, n):
    global maximum
    # Base Case 
    if n == 1:
        return 1
    
    maxEnd = 1
    for i in range(1, n):
        # print(i)
        res = _lis(arr, i)
        if arr[i - 1] < arr[n-1] and res+1 > maxEnd:
            maxEnd = res + 1
    maximum = max(maximum, maxEnd)

    return maxEnd

def lis(arr):
    global maximum
    n = len(arr)
    maximum = 1

    _lis(arr, n)

    return maximum

# lis returns length of the longest increasing subsequence 
# in arr of size n 
def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and initialize LIS 
    # values for all indexes 
    lis = [1]*n 
  
    # Compute optimized LIS values in bottom up manner 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
  
    # Initialize maximum to 0 to get the maximum of all 
    # LIS 
    maximum = 0
  
    # Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum , lis[i]) 
  
    return maximum 
# end of lis function 
arr = [10 , 22 , 9, 33 , 21 , 50 ,60 , 41] 
# arr = [10 , 22 , 9]
n = len(arr) 
