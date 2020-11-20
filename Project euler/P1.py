'''
Find the sum of all the multipes of 3 and 5 below 1000
'''

# Num == 1000
def multiples(num):
    result = []
    for i in range(num):
        if i % 3 == 0:
            result.append(i)
        if i % 5 == 0:
            result.append(i)
    result = set(result)


'''
Prolem 2 in the project euler problems
'''
def fib():
    a, b = 0, 1
    check = True
    fibLst = []
    while check:
        c = a + b
        a, b = b,  c
        fibLst.append(b)
        if b >= 3000000:
            check = False
    return fibLst


def main():
    fLst = fib()
    # fib number holder
    fbHld = []
    for i in fLst:
        if i % 2 == 0:
            fbHld.append(i)
    print(sum(fbHld))

main()

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


def multi(limit, n1, n2):
    multi1 = []
    multi2 = []
    temp = 1
    while True:
        res = n1 * temp
        if res < limit:
            multi1.append(res)
            temp += 1
        else:
            temp = 1
            break
    while True:
        res = n2 * temp
        if res < limit:
            multi2.append(res)
            temp += 1
        else:
            temp = 1
            break

    collection = list(set(multi1 + multi2))
    return (sum(collection))

print(multi(10000, 4,5))


def factorail(num):
    
    fact = 1
    lst = []
    for i in range(1, num + 1):
        lst.append(i)
        fact = fact*i
    collection = sum(lst)
    return fact, collection

print( factorail(10))


        

