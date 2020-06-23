#Gabriel *c3nsored*

'''
Find all possible arragments of the string `s` of length n
Using recusrion
'''



# def BitStr(s, n):
# 	if n == 1:
# 		print(s)
# 		return 
# 	_e = ""

# 	for i in range(len(s)):
# 		temp = _e + s[i]
# 		BitStr(temp, n-1) # Missing the initital input
#		

# 	# return [digit + bits for digit in BitStr(s, 1) for bits in BitStr(s, n-1)]

# print(BitStr('abc', 3))

def infunc(s, n):

	return BitStr(s, "", len(s), n)

def BitStr(s, prefix, k, n):
	#bsae case
	if n==0:
		print(prefix)
		return
	#recursion case	
	for i in range(k):
		_prefix = prefix + s[i]
		BitStr(s, _prefix, k, n-1)


infunc("abc", 3)