'''
Largest prime number for a prime factor
'''

import math
def maxPf(n):
    MaxPrime = -1
    while n %2 == 0:
        maxPrime = 2
        n >> 1

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
        
    return int(maxPrime)
n = 15
print(maxPf(n))
n = 600851475143
print(maxPf(n))

