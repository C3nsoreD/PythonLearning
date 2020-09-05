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
