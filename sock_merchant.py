from collections import defaultdict
"""
Peter works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n = 9 socks with colors ar = [10, 20, 20, 10, 10, 30, 50, 10, 20] 
"""
def sockMerchant(n, ar):
    
    unpair = 0
    freq = {}

    for item in ar:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    for k, v in freq.items():
        if v % 2 != 0:
            unpair += 1 
        
    return (n - unpair)//2 # returns the number of pairs 

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(9, ar))