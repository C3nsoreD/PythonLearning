"""
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N' 
using the sum of the given three numbers.
"""
import sys
#Recursive solution
def func(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return func(n-1)+func(n-3)+func(n-5)

#Implement Memoization
lookup = [-1]*101
def func1(n, lookup):
    #base case 
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    if lookup[n] != -1:
        return lookup[n]
    
    lookup[n] = func(n-1) + func(n-3) + func(n-5)
    
    return lookup[n]

# print(func1(12, lookup))

# Factorial Bottom up 
def fact(n):
    f = [0]*(n+1)
    f[1] = 1
    for i in range(2, n+1):
        f[i] = i*f[i-1]
    return f[n]
print(fact(1000))
