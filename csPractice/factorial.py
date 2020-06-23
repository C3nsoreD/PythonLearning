import random

def factorial(n):
    if n == 0:
        return 1
    if res[n] != None:
        return res[n]
    res[n] = n*fact(n-1)
    return res[n]
	
# factorial(3)
previous = {0:1, 1:1}
def fibonacci(n):
	if previous.__contains__(n) # Not sure if this is legal
		return previous[n]
	else:
		newValue = fibonacci(n-1) + fibonacci(n-2)
		previous[n] = newValue
		return newValue

print([fibonacci(n) for n in range(10)])


# A function that finds the char in a string 		
def find(str, ch, index):
	while index < len(str):
		if str[index] == ch:
			return index
		index = index + 1
	return -1

# fibonacci(91)
# print(fibonacci(9))

# s = "A random string"
# print(len(s)-1)
# print(find(s, 'g', 1))
def inBucket(t, low, high):
	count = 0
	for num in t:
		if low<num<high:
			count+=1
	return count

def func(numBuckets, t):
	buckets =[0]*numBuckets
	bucketwidth = 1/numBuckets
	for i in t:
		index = int(i*numBuckets)
		# print(i, index)
		buckets[index] = buckets[index]+1
		# print(buckets[index])
	return buckets

t = [random.random() for i in range(10)]
rnd = func(8, t)
# print(rnd)

def avg(t):
	return sum(t)/len(t)

# print(avg(rnd))

#Raandom
N = int(input())
def fact(n):
    f = [0]*(N+1)
    f[0] = 1
    for i in range(1, N+1):
        f[i] = n*f[i-1]
    return f[n]

res = [None]*(N+1)
arr = [int(input()) for i in range(N)]
for i in arr:
    print(fact(i))

